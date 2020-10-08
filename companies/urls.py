from django.urls import path
from .views import new_company, new_worker


urlpatterns = [
    path('new_company/', new_company, name='new_company'),
    path('new_worker/', new_worker, name='new_worker'),
]

