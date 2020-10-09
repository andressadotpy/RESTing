from django.test import TestCase


from .models import Company, Worker


class TestCompanyModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='Company Test', cnpj=12345)

    
    def test_if_company_name_is_right(self):
        company = Company.objects.filter(name='Company Test').get()
        expected_name = f'{company.name}'
        self.assertEquals(expected_name, 'Company Test')


    def test_if_company_cnpj_is_right(self):
        company = Company.objects.filter(cnpj=12345).get()
        expected_cnpj = company.cnpj
        self.assertEquals(expected_cnpj, 12345)    


class TestWorkerModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        companies = [
            Company.objects.create(name='Company Test 1', cnpj=12345),
            Company.objects.create(name='Company Test 2', cnpj=67891)
        ]
        worker = Worker.objects.create(name='Worker Test',
                            cpf=123456789, address='Address', job_description='This is the job description')
        
        worker.companies.set(companies)


    def test_if_worker_name_cpf_address_and_job_description_are_right(self):
        worker = Worker.objects.get(id=1)
        expected_name = f'{worker.name}'
        expected_cpf = worker.cpf
        expected_address = f'{worker.address}'
        expected_job_description = f'{worker.job_description}'
        self.assertEquals(expected_name, 'Worker Test')
        self.assertEquals(expected_cpf, 123456789)
        self.assertEquals(expected_address, 'Address')
        self.assertEquals(expected_job_description, 'This is the job description')
        