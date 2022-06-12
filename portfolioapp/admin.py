from django.contrib import admin
from .models import *


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school_name', 'coursework')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'about', 'start', 'end')


class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'date')


admin.site.register(Education, EducationAdmin)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Hobbies)
admin.site.register(Awards, AwardsAdmin)
