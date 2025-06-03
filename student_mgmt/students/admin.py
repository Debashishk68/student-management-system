from django.contrib import admin
from .models import Course, Section, Student # Add all your models here

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Student)
# admin.site.register(Teacher)
# Register your models here.
