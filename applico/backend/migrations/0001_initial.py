# Generated by Django 4.2.4 on 2023-08-08 14:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('hr_person', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('cv_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('current_position', models.CharField(max_length=100)),
                ('second_last_position', models.CharField(blank=True, max_length=100, null=True)),
                ('university', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('skills', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('job_description_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=200)),
                ('date_of_publish', models.DateField()),
                ('location_of_job', models.CharField(max_length=200)),
                ('responsibilities_of_job', models.TextField()),
                ('requirements_of_job', models.TextField()),
                ('bonuses_of_company', models.TextField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.company')),
            ],
        ),
    ]
