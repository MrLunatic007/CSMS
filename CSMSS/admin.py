from django.contrib import admin

# Import your models here
from .models import Student, Teacher, User

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(User)