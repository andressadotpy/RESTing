from django.urls import path, include


from .views import (api_overview, list_of_companies,
                    list_of_workers, details_about_worker,
                    details_about_company, create_new_worker,
                    edit_worker, delete_worker)


urlpatterns = [
    path('', api_overview, name="api_overview"),
    path('companies/', list_of_companies, name="companies"),
    path('company/<int:id>/', details_about_company, name="details_about_company"),


    path('workers/', list_of_workers, name="workers"),
    path('worker/<int:id>/', details_about_worker, name="details_about_worker"),
    path('new_worker/', create_new_worker, name="create_new_worker"),    
    path('edit_worker/<int:id>/', edit_worker, name="edit_worker"),
    path('delete_worker/<int:id>/', delete_worker, name="delete_worker")
]