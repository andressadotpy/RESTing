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
        print(request.POST)
        name = request.POST['name']
        print(name)
        cpf = int(request.POST['cpf'])
        print(cpf)
        address = request.POST['address']
        print(address)
        job_description = request.POST['job_description']
        print(job_description)
        print(companies)
        companies = request.POST['companies']
        print(companies)
        print(type(companies))
        worker = Worker.objects.create(name=name, cpf=cpf, address=address, job_description=job_description)
        worker.save()   
        return redirect('index')
    

    form = WorkerForm()

    companies = Company.objects.all()
    companies = {
        'companies': companies
    }

    return render(request, 'new_worker.html', companies)