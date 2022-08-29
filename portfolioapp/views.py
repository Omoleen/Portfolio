from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from Portfolio.settings import BASE_URL


def landing(request):
    about = About.objects.get(first_name='emmanuel')
    technical = TechnicalSkill.objects.all()
    soft = SoftSkill.objects.all()
    framework = Framework.objects.all()
    tools = Tool.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    hobbies = Hobbies.objects.all()
    awards = Award.objects.all()
    context = {
        'about': about,
        'technicals': technical,
        'softs': soft,
        'frameworks': framework,
        'tools': tools,
        'projects': projects,
        'education': education,
        'experiences': experience,
        'hobbies': hobbies,
        'awards': awards,
    }
    return render(request, 'index.html', context)


def project(request, pk):
    about = About.objects.get(first_name='emmanuel')
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'base_url': BASE_URL,
        'about': about
    }
    return render(request, 'project.html', context)