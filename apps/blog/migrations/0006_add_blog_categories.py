# Generated by Django 4.0.6 on 2022-07-21 13:44

from django.db import migrations
from apps.blog.models import BlogCategory


def add_blog_categories(apps, schema_editor):
    categories = [
        'Новости',
        'Обзоры',
        'Акции',
        'Партнерам',
        'Специальные предложения',
    ]
    for category in categories:
        BlogCategory.objects.create(name=category)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_tag'),
    ]

    operations = [
        migrations.RunPython(add_blog_categories)
    ]
