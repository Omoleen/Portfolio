# Generated by Django 4.0.5 on 2022-06-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0012_rename_links_project_link_award_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
