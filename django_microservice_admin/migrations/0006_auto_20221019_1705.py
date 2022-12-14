# Generated by Django 3.2.7 on 2022-10-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_microservice_admin', '0005_auto_20221019_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminapps',
            name='app_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='adminapps',
            name='project_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='adminapps',
            name='tab_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='adminapps',
            unique_together={('project_name', 'tab_name')},
        ),
    ]
