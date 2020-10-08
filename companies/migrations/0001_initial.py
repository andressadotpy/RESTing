# Generated by Django 3.1.2 on 2020-10-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cnpj', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cpf', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('job_description', models.TextField()),
                ('companies', models.ManyToManyField(to='companies.Company')),
            ],
        ),
    ]
