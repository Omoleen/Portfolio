from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# skills
# projects
# education
# experience
# hobbies


class Skills(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.skill} skill"


class Projects(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    languages = models.ManyToManyField(Skills)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    coursework = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name


class Experience(models.Model):
    position = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    about = models.CharField(max_length=200, blank=True)
    start = models.DateField()
    end = models.DateField(blank=True)

    def __str__(self):
        return self.company_name


class Hobbies(models.Model):
    hobbies = models.CharField(max_length=200)

    def __str__(self):
        return self.hobbies


class Awards(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
