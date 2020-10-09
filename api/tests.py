import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import CompanySerializer, WorkerSerializer
from companies.models import Company, Worker


class TestAPICompanyRegistration(APITestCase):

    def test_registering_new_company(self):
        company = {
            'name': 'Company Test',
            'cnpj': 123456
        }
        response = self.client.post('/api/new_company/', company)
        self.assertEqual(response.status_code, 200)
