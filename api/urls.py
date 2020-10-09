from django.urls import path, include


from .views import api_overview, CompaniesAPIView, WorkersAPIView


urlpatterns = [
    path('', api_overview, name="api_overview"),
    path('companies/', CompaniesAPIView, name='companies'),
    path('workers/', WorkersAPIView.as_view(), name="workers")
]