# Aplicação Django e API com Django Rest Framework

[Link para a aplicação no Heroku](https://resting-with-django.herokuapp.com/)



Após ter clonado o repositório da aplicação e ativar o virtualenvironment, é necessário instalar os requisitos utilizando o *pip*.

```bash
$ pip install -r requirements.txt
```

Nesse projeto foi utilizado para gerenciar a database *resting* o PostgreSQL. É preciso fazer as migrações para a database.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



## Estrutura do projeto

A estrutura do projeto ficou no seguinte formato. `resting` é o projeto. Como um projeto pode ter várias aplicações, esse projeto possui `api` e `companies` como apps. 

```.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── companies
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── __pycache__
│   └── manage.cpython-36.pyc
├── README.md
├── requirements.txt
├── resting
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── static
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static
│   ├── admin
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   └── js
│   ├── css
│   ├── js
│   ├── rest_framework
│   └── vendor
└── templates
    ├── base.html
    ├── index.html
    ├── menu.html
    ├── new_company.html
    └── new_worker.html
```

Dentro de `resting` é onde ficam as configurações de todo o projeto.

Dentro do app `companies` é onde os modelos `Company` e `Worker` foram criados. Esses modelos podem ser adicionados tanto pelo Django Admin quanto pelo formulário front-end da aplicação. Para criar pelo Django Admin, é preciso **criar um superuser antes**.

Em `api` ficam todas as APIs criadas na aplicação e os códigos referentes a essas APIs. Nessa aplicação foi implementado todo CRUD para `Worker` e também para `Company`. Todas as URLs disponíveis na API:

```
api_urls = {
	'Companies': '/api/companies/',
    'Details about company': '/api/company/<int:id>/',
    'Edit company': '/api/edit_company/<int:id>/',
    'Create company': '/api/new_company/',
    'Delete company': '/api/delete_company/',


    'Workers': '/api/workers/',
    'Details about worker': '/api/worker/<int:id>/',
    'Edit worker': '/api/edit_worker/<int:id>/',
    'Create worker': '/api/new_worker/',
    'Delete worker': '/api/worker_delete/'
    }
```



## Exemplo de envio de informações pela API

```python
# Formato de envio de dados para Empresas
company = {
	'name': 'Company Test',
    'cnpj': 123456
}
        
# Formato de envio de dados para Trabalhadores        
worker = {
	'name': 'Worker Test',
	'address': 'Address',
	'job_description': 'This is a job description',
    'companies': [
        Company.objects.create(name='Company 1', cnpj=123456), # um objeto do tipo Company
        Company.objects.create(name='Company 2', cnpj=678910)  # outro objeto to tipo Company
        ]
}
```

Exemplo utilizando Django Rest Framework, mas que pode ser realizado com Postman:

`/api/new_company/`

![Exemplo de requisição POST com Rest Framework](/home/andressa/MEGAsync/Code/djangorest/example_create_company.png)





## Testes

Para rodar os testes da aplicação:

```bash
$ python manage.py test
```



## Rodar a aplicação localmente

```bash
$ python manage.py runserver
```



# Melhorias para uma segunda versão

- Corrigir bug no form pelo frontend.
- Dividir o app companies em dois apps: companies e workers.

- Arrumar para que apareça o nome das empresas de um trabalhador na API e não só a identificação da empresa e tornar mais user friendly no geral.
- Fazer sistema de autenticação de usuários e ajustar permissões da aplicação/api por tipo de usuário.