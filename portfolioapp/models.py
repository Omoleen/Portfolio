from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# skills
# projects
# education
# experience
# hobbies
class About(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    summary = models.TextField(blank=True)
    python_resume = models.FileField(null=True, blank=True)
    javascript_resume = models.FileField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = self.last_name + ' ' + self.first_name
        if self.python_resume:
            self.python_resume.save('Omole_Emmanuel_Python_Resume.pdf', self.python_resume.file, save=False)
        if self.javascript_resume:
            self.javascript_resume.save('Omole_Emmanuel_Javascript_Resume.pdf', self.javascript_resume.file, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TechnicalSkill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill


class SoftSkill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill


class Framework(models.Model):
    framework = models.CharField(max_length=200)

    def __str__(self):
        return self.framework


class Tool(models.Model):
    tool = models.CharField(max_length=200)

    def __str__(self):
        return self.tool


class Project(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(null=True)
    languages = models.ManyToManyField(TechnicalSkill)
    tools = models.ManyToManyField(Tool, blank=True)
    link = models.URLField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    image = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    degree_type = models.CharField(max_length=200, blank=True)
    school_name = models.CharField(max_length=200)
    coursework = models.TextField()
    start_date = models.IntegerField(default=1999)
    end_date = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.school_name


class Experience(models.Model):
    position = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company_name

    def get_list(self):
        return self.about.split('\n')


class Hobbies(models.Model):
    hobbies = models.CharField(max_length=200)

    def __str__(self):
        return self.hobbies


class Award(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.DateField()
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
