from django.contrib import admin
from .models import *


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school_name', 'coursework')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'about', 'start', 'end')


class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'date')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')


admin.site.register(Education, EducationAdmin)
admin.site.register(TechnicalSkill)
admin.site.register(SoftSkill)
admin.site.register(Framework)
admin.site.register(Tool)
admin.site.register(Project)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Hobbies)
admin.site.register(Award, AwardsAdmin)
admin.site.register(About, AboutAdmin)
