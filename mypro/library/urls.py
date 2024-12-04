
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.hello,name='hello'),
    path('logins',views.logins,name='logins'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('handles_logout',views.handles_logout,name='handles_logout'),
    path('categoryname',views.categoryname,name='categoryname'),
    path('books',views.books,name='books'),
    path('displayb',views.displayb,name='displayb'),
    path('updateb/<int:id>',views.updateb,name='updateb'),
    path('deleteb/<int:id>',views.deleteb,name='deleteb'),
    path('sbjct',views.sbjct,name='sbjct'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('abc',views.abc,name='abc'),
    path('displaystd',views.displaystd,name='displaystd'),
    path('booktable/<int:id>',views.booktable,name='booktable'),
    path('details',views.details,name='details'),
    path('book_return/<int:id>',views.book_return,name='book_return'),
    path('return_book',views.return_book,name='return_book'),
    path('book_accept/<int:id>',views.book_accept,name='book_accept'),
    path('details1',views.details1,name='details1'),
    path('adminpass',views.adminpass,name='adminpass'),
    path('studentpass',views.studentpass,name='studentpass'),
    path('profile',views.profile,name='profile'),
    path('forgetpass',views.forgetpass,name='forgetpass'),
    path('newpass',views.newpass,name='newpass'),
    path('setpass',views.setpass,name='setpass'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
