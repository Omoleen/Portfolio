# Generated by Django 4.0.5 on 2022-06-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0008_education_end_date_education_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='about',
            field=models.CharField(max_length=1000),
        ),
    ]