from django.contrib import admin
from django.urls import path, include
from .views import CVView, CompanyView, JobDescriptionView

urlpatterns = [
    path('cv/', CVView.as_view()),
    path('cv/<int:pk>/', CVView.as_view()),
    path('company/', CompanyView.as_view()),
    path('company/<int:pk>/', CompanyView.as_view()),
    path('job/', JobDescriptionView.as_view()),
    path('job/<int:pk>/', JobDescriptionView.as_view()),
]
