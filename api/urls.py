from django.urls import path, include


from .views import api_overview, list_of_companies, list_of_workers, details_about_worker, details_about_company


urlpatterns = [
    path('', api_overview, name="api_overview"),
    path('companies/', list_of_companies, name='companies'),
    path('workers/', list_of_workers, name="workers"),
    path('worker/<int:id>', details_about_worker, name="details_about_worker"),
    path('company/<int:id>', details_about_company, name="details_about_company"),
]