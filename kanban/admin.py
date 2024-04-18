from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(TaskStatus)
admin.site.register(StageOfExecution)
admin.site.register(Discussion)