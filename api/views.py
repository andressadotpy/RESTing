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

#### Company related views

@api_view(['GET'])
def list_of_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def details_about_company(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)


#### Worker related views

@api_view(['GET'])
def list_of_workers(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def details_about_worker(request, id):
    worker = Worker.objects.get(id=id)
    serializer = WorkerSerializer(worker, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_new_worker(request):
    serializer = WorkerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def edit_worker(request, id):
    worker = Worker.objects.get(id=id)
    serializer = WorkerSerializer(instance=worker, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def delete_worker(request, id):
    worker = Worker.objects.get(id=id)
    worker.delete()
        
    return Response('Worker was succesfully delete!')




