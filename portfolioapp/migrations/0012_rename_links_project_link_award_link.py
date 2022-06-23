# Generated by Django 4.0.5 on 2022-06-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0011_project_links'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='links',
            new_name='link',
        ),
        migrations.AddField(
            model_name='award',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]