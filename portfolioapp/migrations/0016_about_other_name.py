# Generated by Django 3.2.13 on 2022-07-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0015_about_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='other_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
