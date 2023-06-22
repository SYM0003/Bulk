from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
    # return HttpResponse("This is the login page from login app")
    return render(request, "login/login.html")
def reset(request):
    return render(request,"login/reset.html")

def sign_up(request):
    return render(request, "login/signUp.html")