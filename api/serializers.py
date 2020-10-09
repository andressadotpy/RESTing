from rest_framework import serializers


from companies.models import Company, Worker


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'cnpj')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('name', 'job_description', 'companies')


