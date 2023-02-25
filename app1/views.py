from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def Home(request):
    if request.user.is_anonymous:
         return redirect('/login')
    return render(request,'home.html')    

def signup_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password!=cpassword:
            return HttpResponse("Type password correctly in both the cases ")
        else:
            my_user=User.objects.create_user(username)
            my_user.set_password(password)
       
            my_user.save()
            return redirect('login')
       #print(username,password,cpassword)  

    return render(request,'signup.html')

def login_user(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
       # print(username,password)
         user=authenticate(request,username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('/')
         else:
           # return render(request,'login.html')  
            return HttpResponse('user name or password is incorrect')  
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')