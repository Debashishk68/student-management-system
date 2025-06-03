# school/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentForm # Import your StudentForm
from .models import Student # Import your Student model
from django.shortcuts import get_object_or_404
from .models import Student
from django.db.models import Q


@login_required
def add_student(request):
    """
    Handles adding a new student.
    Only accessible to logged-in users.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() # Save the new student to the database
            messages.success(request, 'Student added successfully!')
            return redirect('student_list') # Redirect to a list of students (you'd create this view)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm() # An empty form for GET requests

    context = {
        'form': form,
        'title': 'Add New Student',
    }
    return render(request, 'add_student.html', context)

# Placeholder for a student list view (needed for the redirect)
@login_required


def student_list(request):
    students = Student.objects.all()

    # Get filter params
    section = request.GET.get('section')
    search_query = request.GET.get('search')
    reset = request.GET.get('reset')

    if reset:
        # If reset button clicked, clear filters (just redirect to the same page without params)
        return redirect('student_list')  # Replace 'student_list' with your URL name

    if section and section in ['A', 'B', 'C']:
        students = students.filter(section=section)

    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) | 
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    context = {
        'students': students,
        'title': 'Student List'
    }
    return render(request, 'student_list.html', context)

@login_required
def student_detail(request, pk): # 'pk' will capture the student's primary key from the URL
    """
    Displays the details of a single student.
    Uses get_object_or_404 to return a 404 if the student is not found.
    """
    student = get_object_or_404(Student, pk=pk) # Fetch the student by primary key
    context = {
        'student': student,
        'title': f'Details for {student.first_name} {student.last_name}',
    }
    return render(request, 'student_detail.html', context)

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
@login_required    
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form})
