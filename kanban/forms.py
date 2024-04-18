from django import forms
from .models import TaskStatus, Task, Project, StageOfExecution, Discussion


class ChangeTaskStatusForm(forms.Form):
	status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), empty_label="Поменять статус задачи", widget=forms.Select(attrs={'class': 'task-status', 'id': 'select'}))


class ChangeTaskStageOfExecutionForm(forms.Form):
	stage_of_execution = forms.ModelChoiceField(queryset=StageOfExecution.objects.all(), empty_label="Выбрать этап выполнения", widget=forms.Select(attrs={'class':'task-status', 'id':'select'}))


class TaskCreationForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input resize-vertical', 'placeholder': 'Введите описание'}))
	status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}), empty_label='Выберите статус')
	project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}), empty_label='Выберите проект')
	class Meta:
		model = Task
		fields = ['title', 'description', 'status', 'project']


class ProjectCreationForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название проекта'}))
	class Meta:
		model = Project
		fields = ['title']


class DiscussionCreationForm(forms.ModelForm):
	data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}))
	class Meta:
		model = Discussion
		fields = ['data']