from django.urls import path, include


from .views import api_overview, list_of_companies, list_of_workers


urlpatterns = [
    path('', api_overview, name="api_overview"),
    path('companies/', list_of_companies, name='companies'),
    path('workers/', list_of_workers, name="workers")
]