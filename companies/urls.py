from django.urls import path
from .views import new_company


urlpatterns = [
    path('new_company/', new_company, name='new_company'),
]

