# Generated by Django 3.2.14 on 2022-07-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220719_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Тег'),
        ),
    ]
