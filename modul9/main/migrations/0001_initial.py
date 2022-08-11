# Generated by Django 4.0.5 on 2022-08-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=50, verbose_name='Имя компании')),
                ('list_home', models.CharField(max_length=200, verbose_name='Список домов')),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('surname', models.CharField(max_length=50, verbose_name='surname')),
                ('mail', models.EmailField(max_length=50, verbose_name='mail')),
                ('telephone', models.IntegerField(verbose_name='telephone')),
            ],
        ),
    ]