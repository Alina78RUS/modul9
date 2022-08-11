from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('human', views.human, name = 'human'),
	path('create', views.create, name = 'create'),
	path('company', views.company, name = 'company'),
	path('create_company', views.create_company, name = 'create_company'),


]