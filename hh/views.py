from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from hh.models import Company,Vacancy

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        pass

def company_detail(request,company_id):
    try:
        company=Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(company.to_json())

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancies.all()
    vacancies_json = [v.to_json() for v in vacancies]

    return JsonResponse(vacancies_json, safe=False)


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

