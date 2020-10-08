from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.IntegerField()


    def __str__(self):
        return f'{self.name} - CNPJ {self.cnpj}'


class Worker(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.IntegerField()
    address = models.CharField(max_length=300)
    job_description = models.TextField()
    companies = models.ManyToManyField(Company)

    
    def __str__(self):
        return self.name