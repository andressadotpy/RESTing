from django.shortcuts import render
from .models import Company, Worker


def new_company(request):

    if request.POST:
        name = request.POST['name']
        cnpj = request.POST['cnpj']
        company = Company.objects.create(name=name, cnpj=cnpj)
        company.save()
    return render(request, 'new_company.html')


def new_worker(request):
    all_companies = Company.objects.all()

    companies = {
        'companies': all_companies 
    }

    if request.POST:
        name = request.POST['name']
        cpf = request.POST['cpf']
        address = request.POST['address']
        job_description = request.POST['job_description']
        companies = request.POST['companies']
        worker = Worker.objects.create(name=name, cpf=cpf, address=address, job_description=job_description, companies=companies)
        worker.save()
        return redirect('index')

    return render(request, 'new_worker.html', companies)