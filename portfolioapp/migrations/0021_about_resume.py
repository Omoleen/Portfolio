# Generated by Django 4.0.4 on 2023-07-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0020_alter_education_coursework_alter_experience_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]