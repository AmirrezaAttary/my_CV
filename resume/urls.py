from django.urls import path

from resume.views import *

app_namw = 'resume'

urlpatterns = [
    path('', view_index, name='index'),
    path('about', view_about, name='about'),
    path('resume', view_resume, name='resume'),
    path('contact', view_contact, name='contact'),
]

