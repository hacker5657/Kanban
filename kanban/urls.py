from django.urls import path
from .views import *

app_name = 'kanban'

urlpatterns = [
	path('', index, name='index'),
	path('create/task', create_task, name='create_task'),
	path('create/project', create_project, name='create_project'),
	path('project/<int:project_id>', view_project, name='view_project'),
	path('task/<int:task_id>', change_status, name='change_status'),
	path('project/<int:project_id>/task/user/<int:user_id>', user_tasks, name='user_tasks'),
	path('project/<int:project_id>/task/executor/<int:user_id>', task_executor, name='task_executor'),
	path('task/<int:task_id>/executor/add', add_executor, name='add_executor'),
	path('/project/<int:project_id>/task/<int:task_id>/stage-of-execution/set', set_stage_of_execution, name='set_stage_of_execution'),
	path('project/<int:project_id>/task/<int:task_id>/add-discussion', add_discussion, name='add_discussion')
]