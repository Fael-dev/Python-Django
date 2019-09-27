from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 
from django.http import HttpResponse
from .models import Teste
from .forms import TesteForm
from django.contrib import messages	
import datetime

@login_required
def TesteList(request): # MÉTODO PARA LISTAR OS OBJETOS

	search = request.GET.get('search')
	filter = request.GET.get('filter')
	# tfr = Tarefas feitas recentemente
	tfr = Teste.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
	# tf = Tarefas feitas 
	tf = Teste.objects.filter(done='done', user=request.user).count()
	# taf =Tarefas a fazer
	taf = Teste.objects.filter(done='doing', user=request.user).count()
	if search:
		test = Teste.objects.filter(title__icontains=search, user=request.user)

	elif filter:
		test = Teste.objects.filter(done=filter, user=request.user)

	else:

		test_list = Teste.objects.all().order_by('-created_at').filter(user=request.user)

		paginator = Paginator(test_list, 5)

		page = request.GET.get('page')

		test = paginator.get_page(page)  

	return render(request, 'testes/list.html', {'test': test, 'tfr': tfr, 'tf':tf, 'taf':taf})


@login_required
def testeView(request, id): # MÉTODO PARA MONTAR UM OBJETO EM UMA PÁGINA HTML
	teste = get_object_or_404(Teste, pk=id)
	return render(request, 'testes/teste.html', {'teste': teste})


@login_required
def newTeste(request): # MÉTODO PARA CADASTRAR UM NOVO OBJETO
	if request.method == 'POST':
		form = TesteForm(request.POST)
		if form.is_valid():
			teste = form.save(commit=False)
			teste.done = 'doing'
			teste.user = request.user
			teste.save()
			return redirect('/')
	else:	
		form = TesteForm()
		return render(request, 'testes/addteste.html', {'form': form})


@login_required
def editTeste(request, id): # MÉTODO PARA EDITAR OBJETOS
	teste = get_object_or_404(Teste, pk=id)
	form = TesteForm(instance=teste)

	if request.method == 'POST':
		form = TesteForm(request.POST, instance=teste)

		if(form.is_valid()):
			teste.save()
			return redirect('/')
		else:
			return render(request, 'testes/editteste.html', {'form': form, 'teste':teste})

	else:
		return render(request, 'testes/editteste.html', {'form': form, 'teste':teste})


@login_required
def deleteTeste(request, id):
	teste = get_object_or_404(Teste, pk=id)
	teste.delete()

	messages.info(request, 'Tarefa deletada com êxito')

	return redirect('/')

@login_required
def changeStatus(request, id):
	teste = get_object_or_404(Teste, pk=id)

	if(teste.done == 'doing'):
		teste.done ='done'
	
	else:
		teste.done = 'doing'
	
	teste.save()
	return redirect('/')

def index(request):
	return HttpResponse('Beleza') 

def seu_nome(request, name):
	return render(request, 'testes/seunome.html', {'name':name})