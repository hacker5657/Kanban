from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import Project, Task, StageOfExecution, TaskStatus
from .forms import ChangeTaskStatusForm, TaskCreationForm, ProjectCreationForm, ChangeTaskStageOfExecutionForm, DiscussionCreationForm


# Create your views here.
@login_required
def index(request):
	projects = Project.objects.all()
	return render(request, 'kanban/index.html', {'projects': projects})


@login_required
def view_project(request, project_id):
	tasks = Task.objects.filter(project__id=project_id)
	project = Project.objects.get(id=project_id)
	status_form = ChangeTaskStatusForm()
	stage_form = ChangeTaskStageOfExecutionForm()
	return render(request, 'kanban/project_view.html', {'tasks': tasks, 'status_form': status_form, 'stage_form': stage_form, 'project': project})


@login_required
def change_status(request, task_id):
	if request.method == 'POST':
		form = ChangeTaskStatusForm(data=request.POST)
		if form.is_valid():
			task = Task.objects.get(id=task_id)
			task.status = form.cleaned_data.get('status')
			if task.stage_of_execution.title == 'Выполнено':
				stage_of_execution = StageOfExecution.objects.get(title='Ожидание')
				task.stage_of_execution = stage_of_execution
			task.save()
			return redirect(request.META.get('HTTP_REFERER'))


@login_required
def create_task(request):
	if request.method == 'POST':
		form = TaskCreationForm(data=request.POST)
		form.instance.user = request.user
		if form.is_valid():
			form.save()
			return redirect(request.META.get('HTTP_REFERER'))
	else:
		form = TaskCreationForm()
	return render(request, 'kanban/create_task.html', {'form': form})


@login_required
def user_tasks(request, project_id, user_id):
	tasks = Task.objects.filter(user__id=user_id, project__id=project_id)
	project = Project.objects.get(id=project_id)
	form = ChangeTaskStatusForm()
	return render(request, 'kanban/project_view.html', {'tasks': tasks, 'form': form, 'project': project})


@login_required
def create_project(request):
	if request.method == 'POST':
		form = ProjectCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('kanban:index')
	else:
		form = ProjectCreationForm()
	return render(request, 'kanban/create_project.html', {'form': form})


@login_required
def task_executor(request, project_id, user_id):
	tasks = Task.objects.filter(executors__id=user_id, project__id=project_id)
	project = Project.objects.get(id=project_id)
	form = ChangeTaskStatusForm()
	return render(request, 'kanban/project_view.html', {'form': form, 'tasks': tasks, 'project': project})


@login_required
def add_executor(request, task_id):
	task = Task.objects.get(id=task_id)
	stage_of_execution = StageOfExecution.objects.get(title='Выполняется')
	task.executors.add(request.user)
	task.stage_of_execution = stage_of_execution
	task.save()
	return redirect(request.META.get('HTTP_REFERER'))


@login_required
def set_stage_of_execution(request, project_id, task_id):
	if request.method == 'POST':
		form = ChangeTaskStageOfExecutionForm(data=request.POST)
		if form.is_valid():
			if form.cleaned_data.get('stage_of_execution').title == 'Обсуждается':
				return redirect('kanban:add_discussion', project_id, task_id)
			else:
				task = Task.objects.get(id=task_id)
				if task.discussion:
					task.stage_of_execution = form.cleaned_data.get('stage_of_execution')
					task.save()
					task.discussion.delete()
				elif form.cleaned_data.get('stage_of_execution').title == 'Выполнено':
					task.stage_of_execution = form.cleaned_data.get('stage_of_execution')
					status = TaskStatus.objects.get(title='Завершена')
					task.status = status
					task.save()
				else:
					if task.status.title == 'Завершена':
						status = TaskStatus.objects.get(title='Срочно, важно')
						task.status = status
					task.stage_of_execution = form.cleaned_data.get('stage_of_execution')
					task.save()
				return redirect(request.META.get('HTTP_REFERER'))
		

@login_required
def add_discussion(request, project_id, task_id):
	if request.method == 'POST':
		form = DiscussionCreationForm(data=request.POST)
		if form.is_valid():
			task = Task.objects.get(id=task_id)
			if task.status.title == 'Завершена':
				status = TaskStatus.objects.get(title='Срочно, важно')
				task.status = status
			stage_of_execution = StageOfExecution.objects.get(title='Обсуждается')
			discussion = form.save()
			task.discussion = discussion
			task.stage_of_execution = stage_of_execution
			task.save()
			return redirect('kanban:view_project', project_id)
		
	project = Project.objects.get(id=project_id)
	form = DiscussionCreationForm()
	return render(request, 'kanban/add_discussion.html', {'project': project, 'form': form, 'project_id': project_id, 'task_id': task_id})