from django.shortcuts import render
from . models import Register
def input(request):
    return  render(request,'input.html')
def insert(request):
    User=request.GET['t1']
    Pswd=request.GET['t2']
    Cpswd=request.GET['t3']
    Mobile=int(request.GET['t4'])
    Dob=request.GET['t5']
    R=Register(UserName=User,Password=Pswd,Confirmpassword=Cpswd,Mobile=Mobile,DOB=Dob)
    R.save()
    return render(request,'links.html')
def display(request):
    recs=Register.objects.all()
    return render(request,'display.html',{'records':recs})

# Create your views here.
