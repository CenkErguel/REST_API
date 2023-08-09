from rest_framework import serializers
from .models import CV, Company, JobDescription

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ('cv_id',
                  'first_name',
                  'last_name',
                  'street',
                  'postal_code',
                  'city',
                  'email',
                  'current_position',
                  'second_last_position',
                  'university',
                  'school',
                  'skills')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_id',
                  'company_name',
                  'hr_person')
        

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ('job_description_id',
                  'job_title',
                  'date_of_publish',
                  'company_name',
                  'location_of_job',
                  'responsibilities_of_job',
                  'requirements_of_job',
                  'bonuses_of_company',
                  'salary')
