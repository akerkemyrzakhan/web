from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hh.models import Company,Vacancy
import json
from django.views import View
from hh.serializers import CompanySerializer,CompanySerializer2,VacancySerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CompanyListAPIView(APIView):
    def get(self,request):
        companies=Company.objects.all()
        serializer = CompanySerializer2(companies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailAPIView(APIView):
    def get_object(self,id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error':str(e)})
    def get(self,request,company_id):
        company = self.get_object(company_id)
        serializer= CompanySerializer2(company)
        return Response(serializer.data)

    def put(self,request,company_id):
        company= self.get_object(company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,company_id):
        company = self.get_object(company_id)
        company.delete()
        return Response({'deleted':True})




@api_view(['GET','POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer=CompanySerializer2(companies,many=True)
        # companies_json = [company.to_json() for company in companies]
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # body = json.loads(request.body)
        serializer=CompanySerializer2(data=request.data)
        # company= Company()
        # company.name =data.get('name','')
        # company.save()
        # return JsonResponse(company.to_json())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse({'error':'bad request'})
@api_view(['GET','PUT','DELETE'])
def company_detail(request,company_id):
    try:
        company=Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error':str(e)})

    if request.method == 'GET':
        serializer =CompanySerializer(company)
        return Response(serializer.data)
    elif request.method=='PUT':
        # body=json.loads(request.body)
        serializer=CompanySerializer(instance=company,data=request.data)
        # company.name=data.get('name',company.name)
        # company.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return JsonResponse(company.to_json())
    elif request.method=='DELETE':
        company.delete()
        return Response({'deleted':True})
    return JsonResponse({'error':'bad request'})

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancies.all()
    serializer=VacancySerializer(vacancies,many=True)
    # vacancies_json = [v.to_json() for v in vacancies]

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        pass


def vacancy_detail(request,vacancy_id):
    try:
        vacancy=Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(vacancy.to_json())

def top_vacancies(request):
    top_ten = Vacancy.objects.order_by('-salary')[:10]
    top_ten_json=[v.to_json() for v in top_ten]
    return JsonResponse(top_ten_json,safe=False)

