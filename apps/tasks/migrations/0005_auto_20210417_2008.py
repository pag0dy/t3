# Generated by Django 2.2.4 on 2021-04-18 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210412_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='status',
            field=models.CharField(choices=[('ST', 'Started'), ('CM', 'Completed'), ('IP', 'In Progress'), ('BL', 'Backlog'), ('OH', 'On Hold'), ('BD', 'Blocked'), ('DM', 'Dismissed')], default='BL', max_length=100),
        ),
    ]
