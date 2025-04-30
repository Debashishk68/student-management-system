from django.urls import path

from . import views

urlpatterns = [
  path('dashboard/', views.StudentDashboardView, name='student_dashboard'),
    # path('profile/edit/', views.EditStudentProfileView, name='edit_student_profile'),
    # path('courses/', views.StudentCoursesView, name='student_courses'),
    ]