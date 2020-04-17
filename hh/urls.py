from django.urls import path
from hh.views import company_list,company_detail,company_vacancies,vacancy_detail,vacancy_list,top_vacancies
# from hh.views.views_cbv import CompanyListAPIView
from hh.views.views_generic import CompanyListAPIView,CompanyDetailAPIView,VacancyDetailAPIView,VacancyListAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns=[
    path('login/',obtain_jwt_token),
    path('companies/',CompanyListAPIView.as_view()),
    path('companies/<int:pk>/',CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/',company_vacancies),
    path('vacancies/',VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/',VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/',top_vacancies)


]