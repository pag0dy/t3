# Generated by Django 2.2.4 on 2021-04-10 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ST', 'Started'), ('CM', 'Completed'), ('IP', 'In Progress'), ('BL', 'Backlog'), ('OH', 'On Hold'), ('BL', 'Blocked'), ('DM', 'Dismissed')], default='BL', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=254)),
                ('client', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('hours_assigned', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_assigned', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=254)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('hours_assigned', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ManyToManyField(through='tasks.Assignments', to='users.User')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.Project')),
            ],
        ),
        migrations.AddField(
            model_name='assignments',
            name='tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
