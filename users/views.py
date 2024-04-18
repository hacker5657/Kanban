from django.shortcuts import render
from .forms import UserAuthForm, UserRegisterForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	if request.method == 'POST':
		form = UserAuthForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('kanban:index'))
	else:
		form = UserAuthForm()
	return render(request, 'auth/login.html', {'form': form})

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			return HttpResponseRedirect(reverse('kanban:index'))
	else:
		form = UserRegisterForm()
	return render(request, 'auth/register.html', {'form': form})

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('users:login'))