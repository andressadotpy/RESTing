from django import forms
from .models import Company, Worker


class CompanyForm(forms.Form):
    
    class Meta:
        model = Company

    name = forms.CharField(max_length=200)
    cnpj = forms.IntegerField()
    


class WorkerForm(forms.Form):
    class Meta:
        model = Worker
        fields = ('name', 'cpf', 'address', 'job_description', 'companies')

