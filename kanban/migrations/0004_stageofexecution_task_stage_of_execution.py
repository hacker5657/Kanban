# Generated by Django 4.2.11 on 2024-04-15 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0003_alter_task_executors'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageOfExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='stage_of_execution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kanban.stageofexecution'),
        ),
    ]
