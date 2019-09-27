from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name='index'),
	path('', views.TesteList, name='teste-list'),
	path('newteste/', views.newTeste, name='new-teste'),
	path('teste/<int:id>', views.testeView, name='teste-view'),
	path('edit/<int:id>', views.editTeste, name='edit-teste'),
	path('changestatus/<int:id>', views.changeStatus, name='change-status'),
	path('delete/<int:id>', views.deleteTeste, name='delete-teste'),
	path('seunome/<str:name>', views.seu_nome, name='seu-nome')
]