from django.shortcuts import render , HttpResponse

# Create your views here.
def LoginView(request):
    # return HttpResponse("Login Page")
    return render(request, 'login.html')
def LogoutView(request):
    return render(request, 'logout.html')
def RegisterView(request):
    return render(request, 'register.html')
def ProfileView(request):
    return render(request, 'profile.html')