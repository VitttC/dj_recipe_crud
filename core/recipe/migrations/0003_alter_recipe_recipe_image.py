# Generated by Django 5.1.4 on 2025-01-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='home/vi/Documents/DJANGO_PROJECTS/dj_recipe_crud/core/media'),
        ),
    ]