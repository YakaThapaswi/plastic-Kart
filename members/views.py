from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth,User
from django.contrib import messages
from home import views
def login_user(request):
    if request.method=="POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("login")
            return redirect("/home")
        else:
            return redirect("login")
    return render(request,'login.html')
def signup_user(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        email=request.POST.get("email")
        password1=request.POST.get("pass1")
        lname=request.POST.get("lname")
        password2=request.POST.get("pass2")
        if(password1!=password2):
            messages.warning(request,"password incorrect")
            return redirect("signup")
        try:
            if(User.objects.get(username=lname)):
                messages.warning(request,"username already taken")
                return redirect("signup")
        except:
            pass
        try:
            if(User.objects.get(email=email)):
                messages.warning(request,"email already exists")
                return redirect("signup")
        except:
            pass
        user=User.objects.create_user(username=lname,password=password1,email=email,first_name=fname,last_name=lname)
        user.save()
        print("user created")
        return redirect('/home')
    return render(request,"register.html")
def logout_user(request):
    logout(request)
    return redirect("/home")


