# Generated by Django 4.0.5 on 2022-06-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0009_alter_project_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree_type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
