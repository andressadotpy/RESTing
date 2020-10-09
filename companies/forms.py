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


    name = forms.CharField(max_length=200)
    cpf = forms.IntegerField()
    address = forms.CharField(max_length=300)
    job_description = forms.CharField(max_length=500)
    companies = forms.ModelMultipleChoiceField(queryset=Company.objects.all())

