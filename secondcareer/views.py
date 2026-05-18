from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .models import Secondcareer

# Create your views here.

def index(request):
    jobs = Secondcareer.objects.all()

    context = {
        'jobs': jobs
    }

    return render(request,
                  'home_page.html',
                  context)

def contact(request):
    return HttpResponse("contact me")
def account(request):
    return render(request,'create_account.html')

def organizer(request):
    if request.method == "POST":
        data=request.POST
        company_name=data.get('company_name')
        job_description=data.get('job_description')
        job_image=request.FILES.get('job_image')

        Secondcareer.objects.create(
            user=request.user,
            company_name=company_name,
            job_description=job_description,
            job_image=job_image
        )
        return redirect('organizer')
    queryset=Secondcareer.objects.all()
    context={'organizer':queryset}
    return render(request,'organizer_page.html',context)
    
def login_page(request):
    return render(request,'login_user.html')
def login_page1(request):
    return render(request,'login_orga.html')

def register_user(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():

            messages.error(request,
                           "Username already exists")

            return redirect('register_user')


        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,

            email=email,
            username=username
        )

        user.set_password(password)
        user.save()

        return redirect('home')   # URL name

    return render(request,'create_account.html')

def register_organizer(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            messages.error(request,
                           "Username already exists")

            return redirect('register_user')


        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )

        user.set_password(password)
        user.save()

        return redirect('organizer')   # URL name

    return render(request,'create_account.html')

def login_public(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('login')
        
        user=authenticate(username=username,password=password)
         
        if user is None:
            messages.error(request,'Inavlid Password')
            return redirect('login')
        else:
            login(request,user)
            return redirect('home')
    return render(request,'login_user.html')

def login_company(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('login')
        
        user=authenticate(username=username,password=password)
         
        if user is None:
            messages.error(request,'Inavlid Password')
            return redirect('login')
        else:
            login(request,user)
            return redirect('organizer')
    return render(request,'login_orga.html')


    


