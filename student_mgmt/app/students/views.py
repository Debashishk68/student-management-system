from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")
def StudentDashboardView(request):
    url={'student_dashboard':"/dashboard",'student_courses':"/student_courses",'student_logout':"/logout",'name':"John Doe",'student_profile':"/student_profile",'student_edit_profile':"/edit_student_profile"}
    return render(request, "student_dashboard.html", url)
# def EditStudentProfileView(request):
#     return render(request, "edit_student_profile.html")