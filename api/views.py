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


class CompaniesAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class WorkersAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

