from django.contrib import admin

from hh.models import Company,Vacancy
# Register your models here.
admin.site.register(Company)
admin.site.register(Vacancy)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name')