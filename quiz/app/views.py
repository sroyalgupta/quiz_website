from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Question
from random import randint
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import logout
from .models import Question,User_profile


# Create your views here.

def index(request):
    all = Question.objects.all()
    temp = randint(1,len(all))
    question = Question.objects.filter(q_no=temp)
    print(question)
    params= {'questions':question}
    return render(request,'app/index.html',params)

def signup(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        password = request.POST.get('password')
        team_leader_name = request.POST.get('team_leader_name')
        number = request.POST.get('number')
        
        user = User.objects.create_user(username=team_name,password=password,first_name=team_leader_name,last_name=number)
        user.save()
        return redirect("/login/")
    else:
        return render(request,"app/signup.html")

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        print(user_name,password)
        user = auth.authenticate(username=user_name,password=password)
        print(user.id)
        user_profile = User_profile.objects.get(user=user)
        print(user_profile)
        param = {"user_profile":"hello"}
        if user is not None:
            auth.login(request,user)
            return redirect("/",param)
        else:
            return HttpResponse("Please enter the valid credentials..\n Press Back to naviagate to login page..")
    return render(request,"app/login.html")

def logout_user(request):
    logout(request)
    return HttpResponse("logged out successfully..")