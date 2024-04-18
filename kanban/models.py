from django.db import models
from django.contrib.auth.models import User


class TaskStatus(models.Model):
	title = models.CharField('Статус', max_length=200)

	def __str__(self):
		return self.title


class Project(models.Model):
	title = models.CharField('Название', max_length=500)

	def __str__(self):
		return self.title


class StageOfExecution(models.Model):
	title = models.CharField('Название', max_length=200)

	def __str__(self):
		return self.title
	

class Discussion(models.Model):
	data = models.DateTimeField('Дата обсуждения')

	def __str__(self):
		return f'Обсуждение {self.data}'


class Task(models.Model):
	title = models.CharField("Название", max_length=500)
	description = models.TextField("Описание")
	status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	executors = models.ManyToManyField(User, related_name='executors', null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	stage_of_execution = models.ForeignKey(StageOfExecution, on_delete=models.PROTECT, null=True, blank=True)
	discussion = models.ForeignKey(Discussion, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title