from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, JsonResponse
from .models import Log
from django.db.models import Max
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now
    ctx={"time":now}
    #return HttpResponse(html)
    return render(request, "website/holaMundo.html",ctx)


def index(request):
    #return HttpResponse(html)
    maxp= Log.objects.all().aggregate(Max("points"))
    ctx={"maxp": maxp["points__max"]}
    return render(request, "website/index.html",ctx)

def chart(request):
    maxp= Log.objects.all().aggregate(Max("points"))
    pointList = Log.objects.all().order_by('date')
    ctx = {'maxp': maxp["points__max"], "pointList": pointList}
    return render(request, "website/chart.html", ctx)
# Create your views here.
def log(request):
    latest_logs = list(Log.objects.order_by('date')[:5].values())
    return JsonResponse(latest_logs,safe=False)
#-----------Autenticación-----------------------
def home(request):
    return render(request, "website/home.html")

def auth_(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, ("Usuario o contraseña incorrectas"))
            return redirect('auth') 
    return render(request, "website/auth.html")

def lout(request):
    logout(request)
    messages.success(request, ("Logout Exitoso")) 
    return redirect("home")

