from django.contrib import admin
from .models import CV, Company, JobDescription

models_list = [CV, Company, JobDescription]
admin.site.register(models_list)
