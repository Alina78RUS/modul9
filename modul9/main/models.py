from django.db import models


class Company(models.Model):

	name_company = models.CharField('Имя компании', max_length=50)
	list_home = models.CharField('Список домов', max_length=200)

	class Meta:
		verbose_name = 'Компания'
		verbose_name_plural = 'Компании'
		
	def __str__(self):
		return self.name_company


class Human(models.Model):
	
	name = models.CharField('name', max_length=50)
	surname = models.CharField('surname', max_length=50)
	mail = models.EmailField('mail', max_length=50)
	telephone = models.IntegerField('telephone')

	class Meta:
		verbose_name = 'Сотрудник'
		verbose_name_plural = 'Сотрудники'

	def __str__(self):
		return self.name