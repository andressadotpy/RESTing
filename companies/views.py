from django.shortcuts import render


def new_company(request):
    return render(request, 'new_company.html')