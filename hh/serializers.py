from rest_framework import serializers
from hh.models import Company,Vacancy

class CompanySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    description=serializers.CharField(required=True)
    city=serializers.CharField(required=True)
    address=serializers.CharField(required=True)

    def create(self, validated_data):
        company=Company.objects.create(name=validated_data.get('name'))
        # company.save()
        return company

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance

class CompanySerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    address = serializers.CharField(required=True)

    class Meta:
        model=Company
        fields=['id','name','description','city','address']

class VacancySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    description=serializers.CharField()
    salary=serializers.FloatField()
    company=CompanySerializer2()

    def create(self, validated_data):
        vacancy=Vacancy.objects.create(name=validated_data.get('name'))
        # company.save()
        return vacancy

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance
class VacancySerializer2(serializers.ModelSerializer):
    # company=CompanySerializer2(read_only=True)
    company_id= serializers.IntegerField(write_only=True)
    class Meta:
        model = Vacancy
        fields =('id','name','description','salary','company_id')


class CompanySerializerWithVacancies(serializers.ModelSerializer):
    # vacancies = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    vacancies=VacancySerializer2(many=True,read_only=True)
    class Meta:
        model=Company
        fields=('id','name','vacancies')