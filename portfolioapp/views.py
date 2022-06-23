from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from Portfolio.settings import BASE_URL


def landing(request):
    about = About.objects.get(first_name='emmanuel')
    technical = TechnicalSkill.objects.filter()
    soft = SoftSkill.objects.filter()
    framework = Framework.objects.filter()
    tools = Tool.objects.filter()
    projects = Project.objects.filter()
    education = Education.objects.filter()
    experience = Experience.objects.filter()
    hobbies = Hobbies.objects.filter()
    awards = Award.objects.filter()
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
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'base_url': BASE_URL
    }
    return render(request, 'project.html', context)