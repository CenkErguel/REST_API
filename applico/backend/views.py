from rest_framework.views import APIView
from .serializers import CVSerializer, CompanySerializer, JobDescriptionSerializer
from django.http.response import JsonResponse, Http404
from .models import CV, Company, JobDescription
from rest_framework.response import Response


#CV CRUD
class CVView(APIView):
    def get_cv(self, pk):
        try:
            cv = CV.objects.get(cv_id=pk)
            return cv
        except:
            return JsonResponse("CV does not exist", safe=False)

    def get(self, request, pk=None):
        if pk:
            data = self.get_cv(pk)
            serializer = CVSerializer(data)
        else:
            data = CV.objects.all()
            serializer = CVSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = CVSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("CV added successfully", safe=False)
        return JsonResponse("Failed to add CV")

    def put(self, request, pk=None):
        cv_to_update = CV.objects.get(cv_id=pk)
        serializer = CVSerializer(instance=cv_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("CV updated successfully", safe=False)
        return JsonResponse("Failed to update CV", safe=False)
    
    def delete(self, request, pk=None):
        cv_to_delete = CV.objects.get(cv_id=pk)
        cv_to_delete.delete()
        return JsonResponse("CV deleted successfully", safe=False)
    


#Company CRUD
class CompanyView(APIView):
    def get_company(self,pk):
        try:
            company = Company.objects.get(company_id=pk)
            return company
        except:
            return JsonResponse("Company does not exist", safe=False)
        
    def get(self, request, pk=None):
        if pk:
            data = self.get_company(pk)
            serializer = CompanySerializer(data)
        else:
            data = Company.objects.all()
            serializer = CompanySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Company added successfully", safe=False)
        return JsonResponse("Failed to add Company")

    def put(self, request, pk=None):
        company_to_update = Company.objects.get(company_id=pk)
        serializer = CompanySerializer(instance=company_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Company updated successfully", safe=False)
        return JsonResponse("Failed to update Company", safe=False)
    
    def delete(self, request, pk=None):
        company_to_delete = Company.objects.get(company_id=pk)
        company_to_delete.delete()
        return JsonResponse("Company deleted successfully", safe=False)

#JobDescription CRUD
class JobDescriptionView(APIView):
    def get_jobdescription(self,pk):
        try:
            jobdescription = JobDescription.objects.get(job_description_id=pk)
            return jobdescription
        except:
            return JsonResponse("Job description does not exist", safe=False)
        
    def get(self, request, pk=None):
        if pk:
            data = self.get_jobdescription(pk)
            serializer = JobDescriptionSerializer(data)
        else:
            data = JobDescription.objects.all()
            serializer = JobDescriptionSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Company added successfully", safe=False)
        return JsonResponse("Failed to add Company")

    def put(self, request, pk=None):
        jobdescription_to_update = JobDescription.objects.get(company_id=pk)
        serializer = JobDescriptionSerializer(instance=jobdescription_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Job description updated successfully", safe=False)
        return JsonResponse("Failed to update Job description", safe=False)
    
    def delete(self, request, pk=None):
        jobdescription_to_delete = JobDescription.objects.get(company_id=pk)
        jobdescription_to_delete.delete()
        return JsonResponse("Job description deleted successfully", safe=False) 