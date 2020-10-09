from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company, Worker
from .forms import CompanyForm, WorkerForm


def new_company(request):

    if request.POST:
        form = CompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cnpj = form.cleaned_data['cnpj']
            company = Company.objects.create(name=name, cnpj=cnpj)
            company.save()
        return redirect('index')

    form = CompanyForm()

    return render(request, 'new_company.html')


def new_worker(request):

    if request.POST:
        form = WorkerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cpf = form.cleaned_data['cpf']
            address = form.cleaned_data['address']
            job_description = form.cleaned_data['job_description']
            companies = form.cleaned_data['companies']
            print(companies)
            worker = Worker.objects.create(name=name, cpf=cpf, address=address, job_description=job_description)
            worker.save()
            worker.companies.set(companies)
            print(worker)
            return redirect('index')
    

    form = WorkerForm()

    companies = Company.objects.all()
    companies = {
        'companies': companies
    }

    return render(request, 'new_worker.html', companies)