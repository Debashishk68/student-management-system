from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
        path('add/', views.add_student, name='add_student'),
        path('<int:pk>/', views.student_detail, name='student_detail'), 
        path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # path('login/', views.login_view, name='login'),
    # # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'),
    # path('profile/', views.profile_view, name='profile'),
]
