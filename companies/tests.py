from django.test import TestCase


from .models import Company, Worker


class TestCompanyModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='Company Test', cnpj=12345)

    
    def test_if_company_name_is_right(self):
        company = Company.objects.get(id=1)
        expected_name = f'{company.name}'
        self.assertEquals(expected_name, 'Company Test')


    def test_if_company_cnpj_is_right(self):
        company = Company.objects.get(id=1)
        expected_cnpj = company.cnpj
        self.assertEquals(expected_cnpj, 12345)    
