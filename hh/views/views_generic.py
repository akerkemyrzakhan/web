from rest_framework import generics
from rest_framework import mixins
from hh.models import Company,Vacancy
from hh.serializers import CompanySerializer2,VacancySerializer2,CompanySerializerWithVacancies
from rest_framework.permissions import IsAuthenticated
class CompanyListAPIView(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class = CompanySerializerWithVacancies
    # permission_classes = (IsAuthenticated,)
    # def get(self,request, *args,**kwargs):
    #     return self.list(request,*args,**kwargs)
    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)
class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Company.objects.all()
    serializer_class = CompanySerializer2
    # lookup_url_kwarg = 'company_id'
    #
    # def get(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
    #
    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)
class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer2

class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer2