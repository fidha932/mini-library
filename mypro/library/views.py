from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import datetime
# Create your views here.
def hello(request):
    m=book.objects.all()
    p={'m':m}
    return render(request,'first.html',p)

def logins(request):
  if 'id' in request.session and 'role' in request.session:
        if request.session['role']=='librarian':
            return redirect('admin_dashboard')
        elif request.session['role']=='students':
           return redirect('student_dashboard')
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    p1=librarian.objects.filter(username=username,password=password).first()
    p2=students.objects.filter(username=username,password=password).first()
    if p1:
       request.session['id']=p1.id
       request.session['role']='librarian'
       return render(request,'admin_dashboard.html')
    elif p2:
       request.session['id']=p2.id
       request.session['role']='students'
       return render(request,'student_dashboard.html')
    else:
       return HttpResponse('invalid credintial')
  return render(request,'login.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def student_dashboard(request):
    return render(request,'student_dashboard.html')
    
def handles_logout(request):
    if 'id' in request.session:
        request.session.flush()
        
    return redirect('logins')

def categoryname(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        p=category.objects.create(categoryname=categoryname)
        p.save()
        messages.info(request,'category added succefully')

    return render(request,'category.html')

def books(request):
    m=category.objects.all()
    if request.method=='POST':
        bookname=request.POST['bookname']
        categoryname=request.POST['categoryname']
        nmbrofcopies=request.POST['nmbrofcopies']
        description=request.POST['description']
        authername=request.POST['authername']
        if len(request.FILES)>0:
            m=request.FILES['file']
        else:
            m='no image'
        ab=book.objects.create(coverpage=m,bookname=bookname,category_name_id=categoryname,nmbrofcopies=nmbrofcopies,description=description,authername=authername) 
        ab.save()
        messages.info(request,'book details added succesfully')
        return redirect('displayb')
    p={'m':m}
    return render(request,'book.html',p)

def displayb(request):
    m=book.objects.all()
    p={'m':m}
    
    return render(request,'display_book.html',p) 

def updateb(request,id):
    m=get_object_or_404(book,id=id)
    if request.method=='POST':
        bookname=request.POST['bookname']
        categoryname=request.POST['categoryname']
        nmbrofcopies=request.POST['nmbrofcopies']
        description=request.POST['description']
        authername=request.POST['authername']
        if len(request.FILES)>0:
            p=request.FILES['file']
        else:
            p='no image'
        m.bookname=bookname
        m.category_name_=categoryname
        m.nmbrofcopies=nmbrofcopies
        m.description=description
        m.authername=authername
        m.coverpage=p
        m.save()
        return redirect('displayb')
    s=book.objects.filter(id=id)
    m1=category.objects.all()
    p={'m':s,'p':m1}
    return render(request,'updateb.html',p)

def deleteb(request,id):
    m=book.objects.filter(id=id)
    m.delete()
    return redirect('displayb')


def sbjct(request):
    m=request.GET['co']
    p=subject.objects.filter(course_id=m)
    print(p)
    p1={'m':p}
    return render(request,'sbjct.html',p1)

def abc(request):
    p=course.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        age=request.POST['age']
        school=request.POST['school']
        course1=request.POST['course']
        subject=request.POST['subject']
        m=students.objects.create(username=username,password=password,name=name,age=age,school=school,course_id=course1,subject_id=subject)
        m.save()
        return redirect('logins')
    else:
        messages.info(request,'invalid data')

    p1={'m':p}
    return render(request,'register.html',p1)

def displaystd(request):
    m=book.objects.all()
    p={'m':m}
    
    return render(request,'display2.html',p) 

def booktable(request,id):
    studentid=request.session['id']
    bookid=book.objects.filter(id=id)
    bookingdate=datetime.datetime.today()
    returndate="not returned"
    number=bookid[0].nmbrofcopies
    if number==0:
        messages.info(request,'the book is not available')
    else:
        m=booking.objects.create(studentid_id=studentid,bookid_id=id,bookingdate=bookingdate,returndate=returndate)
        m.save()
        ab=number-1
        m=bookid.update(nmbrofcopies=ab)
        messages.info(request,'the book added')
    return redirect('displaystd')

def details(request):
    studentid=request.session['id']
    m=booking.objects.filter(studentid_id=studentid,status='pending')
    p={'m':m}
    
    return render(request,'display_student.html',p) 

def book_return(request,id):
    studentid=request.session['id']
    returndate=datetime.datetime.today()
    bookid=booking.objects.filter(id=id).update(status="returned",returndate=returndate)
    messages.info(request,'the book retuned')
    return redirect('details')

def return_book(request):
    studentid=request.session['id']
    m=booking.objects.filter(studentid_id=studentid,status='returned')
    p={'m':m}
    return render(request,'return.html',p)  

def book_accept(request,id):
   m=get_object_or_404(booking,id=id)
   m.status='Accepted'
   m.save()
   p=get_object_or_404(book,id=m.bookid_id)
   p.nmbrofcopies+=1
   p.save()
   return redirect('return_book')


def details1(request):
    studentid=request.session['id']
    m=booking.objects.all()
    p={'m':m}
    
    return render(request,'all.html',p) 

def adminpass(request):
    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        conformpassword=request.POST['conformpassword']
        if newpassword==conformpassword:
          p=librarian.objects.filter(password=oldpassword)
          if p.count()>0:
            m=librarian.objects.filter(id=p[0].id).update(password=newpassword)
            messages.info(request,'password updated succefully')
          else:
            messages.info(request,'password not updated')
        else:
            messages.info(request,'password do not match')
    return render(request,'adminpass.html')

def studentpass(request):
    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        conformpassword=request.POST['conformpassword']
        if newpassword==conformpassword:
          p=students.objects.filter(password=oldpassword)
          if p.count()>0:
            m=students.objects.filter(id=p[0].id).update(password=newpassword)
            messages.info(request,'password updated succefully')
          else:
            messages.info(request,'password not updated')
        else:
            messages.info(request,'password do not match')
    return render(request,'studentpass.html')


def profile(request):
    studentid=request.session['id']
    m=students.objects.filter(id=studentid)
    p={'m':m}
    return render(request,'profile.html',p)

def forgetpass(request):
    if request.method=='POST':
        username=request.POST['username']
        p=students.objects.filter(username=username)
        if p.count()>0:
            request.session['newid']=p[0].id
            return redirect('newpass')
        else:
            messages.info(request,'invalid user name')
            return render(request,'forget.html')
    return render(request,'forget.html')

        
def newpass(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        school=request.POST['school']
        m=students.objects.filter(name=name,age=age,school=school)
        if m.count()>0:
            return redirect('setpass')
        else:
            messages.info(request,'invalid')
            
    return render(request,'userdetail.html')
     
def setpass(request):
    if request.method =='POST':
        newpassword=request.POST['newpass']
        id=request.session['newid']
        m=students.objects.filter(id=id).update(password=newpassword)
    return render(request,'setpass.html')



    
    