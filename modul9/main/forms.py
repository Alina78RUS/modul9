from .models import Human
from .models import Company
from django.forms import ModelForm, TextInput, Textarea

class HumanForm(ModelForm):
	class Meta:
		model = Human
		fields = ["name", "surname","mail","telephone"]
		widgets = {
		"name": TextInput(attrs={
			'class':'form-control',
			'placeholder':'Введите имя'}),
		"surname": TextInput(attrs={
			'class':'form-control',
			'placeholder':'Введите фамилию'}),
		"mail": TextInput(attrs={
			'class':'form-control',
			'placeholder':'Введите адресс электронной почты'}),
		"telephone": TextInput(attrs={
			'class':'form-control',
			'placeholder':'Введите номер телефона'}),
		}


class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ["name_company", "list_home"]
		widgets = {
		"name_company": TextInput(attrs={
			'class':'form-control',
			'placeholder':'Введите имя компании'}),
		"list_home": Textarea(attrs={
			'class':'form-control',
			'placeholder':'Введите список домов'}),}