# Generated by Django 2.2.4 on 2021-04-10 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_project_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='company_projects', to='users.Company'),
        ),
    ]
