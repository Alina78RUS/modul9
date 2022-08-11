from django.shortcuts import render, redirect
from .models import Company
from .models import Human
from .forms import HumanForm
from .forms import CompanyForm



def index(request):
	compan = Company.objects.all()
	humans = Human.objects.all()
	return render(request, 'main/index.html', {'name_company': compan, 'list_home': 'Список домов'})


def company(request):
	compan = Company.objects.all()
	return render(request, 'main/company.html',
		{'name_company': compan, 'list_home': 'Список домов'})

def human(request):
	humans = Human.objects.all()
	return render(request, 'main/human.html',
		{'name': humans, 'surname': 'surname', 'mail':'mail', 'telephone':'telephone'})


def create(request):
	error = ''
	if request.method=='POST':
		form = HumanForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			error = 'Форма была неверной'
	form = HumanForm()
	context = {'form': form, 'error': error}
	return render(request, 'main/create.html',context)


def create_company(request):
	error = ''
	if request.method=='POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			error = 'Форма была неверной'
	form = CompanyForm()
	context = {'form': form, 'error': error}
	return render(request, 'main/create_company.html',context)