from django.db import models

# Create your models here.

class librarian(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    
    def __str__(self):
        return self.username
    
class category(models.Model):
    categoryname=models.CharField(max_length=30)
    
    def __str__(self):
        return self.categoryname
    
class book(models.Model):
    bookname=models.CharField(max_length=50)
    nmbrofcopies=models.IntegerField()
    description=models.CharField(max_length=50)
    authername=models.CharField(max_length=30)
    coverpage=models.FileField(upload_to='media')
    category_name=models.ForeignKey(category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bookname
    
    
    
class course(models.Model):
    course_name=models.CharField(max_length=23)
    
    def __str__(self):
        return self.course_name 
    
class subject(models.Model):
    name=models.CharField(max_length=25)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name   
    
class students(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    school=models.CharField(max_length=30)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
     
class booking(models.Model):
    studentid=models.ForeignKey(students,on_delete=models.CASCADE)
    bookid=models.ForeignKey(book,on_delete=models.CASCADE)
    returndate=models.CharField(max_length=10)
    bookingdate=models.CharField(max_length=10)
    status=models.CharField(max_length=20,default='pending')
    
    def __str__(self):
        return self.bookid.bookname
