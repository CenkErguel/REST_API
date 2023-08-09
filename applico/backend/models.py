from django.db import models
from django.core.validators import MaxValueValidator

# Table CV
class CV(models.Model):
    cv_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    postal_code = models.IntegerField(validators=[MaxValueValidator(99999)])
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    current_position = models.CharField(max_length=100)
    second_last_position = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    skills = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Table Company  
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    hr_person = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

# Table Job Description
class JobDescription(models.Model):
    job_description_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=200)
    date_of_publish = models.DateField()
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    location_of_job = models.CharField(max_length=200)
    responsibilities_of_job = models.TextField()
    requirements_of_job = models.TextField()
    bonuses_of_company = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return self.job_title