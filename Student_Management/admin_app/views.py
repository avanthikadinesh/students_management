from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect

# Create your views here.
from . models import *

def home(request):
    return HttpResponse("WELCOME")

def home_redirect(request):
    return redirect(home)

def home1(request):
    return HttpResponseRedirect('hh')

def index(request):
    return render(request,'index.html')

def data(request):
    data={'name' : 'hridhik', 'course' : 'radiographar'}
    return render(request,'data.html',data )

def students(request):
    students=['avanthika','shamila','archana','gokul','vishnu']
    return render(request,'data.html',{'stud':students})

def marks(request):
    mark=65
    return render(request,'data.html',{'mark':mark})

def index2(request):
    return render(request,'index2.html')


def teachers(request):
    teacher=Teacher.objects.all()
    return render(request,'teachers.html',{'td':teacher})

def subject(request):
    subject=Subject.objects.all()
    return render(request,'subject.html',{'sub':subject})

def students(request):
    student=Student.objects.select_related('teacher').prefetch_related('subject')
    return render(request,'students.html',{'stud':student})







