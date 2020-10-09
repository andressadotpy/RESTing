from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from companies.models import Company, Worker
from .serializers import CompanySerializer, WorkerSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Companies': '/companies/',
        'Workers': '/workers/',
        'Details about worker': '/worker/<str:name>/',
        'Details about company': '/company/<str:name>/',
        'Create company': '/company_create/',
        'Create worker': '/worker_create/',
        'Delete company': '/company_delete/',
        'Detele worker': '/worker_delete'
    }
    return Response(api_urls)


@api_view(['GET'])
def list_of_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_of_workers(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)


