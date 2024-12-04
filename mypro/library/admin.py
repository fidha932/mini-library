from django.contrib import admin

# Register your models here.

from.models import*
admin.site.register(librarian)
admin.site.register(category)
admin.site.register(book)


admin.site.register(course)
admin.site.register(subject)
admin.site.register(students)
admin.site.register(booking)