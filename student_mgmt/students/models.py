# school/models.py

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_in_months = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return f"{self.course.name} - Section {self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    student_id = models.CharField(max_length=20, unique=True, blank=True, null=True)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        ordering = ['last_name', 'first_name']
