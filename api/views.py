from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from companies.models import Company, Worker
from .serializers import CompanySerializer, WorkerSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Companies': '/companies/',
        'Details about company': '/company/<int:id>/',
        'Edit company': '/edit_company/<int:id>/',
        'Create company': '/new_company/',
        'Delete company': '/delete_company/',


        'Workers': '/workers/',
        'Details about worker': '/worker/<int:id>/',
        'Edit worker': '/edit_worker/<int:id>/',
        'Create worker': '/new_worker/',
        'Delete worker': '/worker_delete/'
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


@api_view(['POST'])
def create_new_company(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def edit_company(request, id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(instance=company, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_company(request, id):
    company = Company.objects.get(id=id)
    company.delete()

    return Response('Company was succesfully delete!')


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


@api_view(['POST'])
def edit_worker(request, id):
    worker = Worker.objects.get(id=id)
    serializer = WorkerSerializer(instance=worker, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_worker(request, id):
    worker = Worker.objects.get(id=id)
    worker.delete()

    return Response('Worker was succesfully delete!')




