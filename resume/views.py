from django.shortcuts import render
from resume.var import *

# Create your views here.


def view_index(request):
    return render(request, 'resume/index.html',index)

def view_about(request):
    return render(request, 'resume/about.html',about)

def view_resume(request):
    return render(request, 'resume/resume.html',about)

def view_contact(request):
    return render(request, 'resume/contact.html',about)