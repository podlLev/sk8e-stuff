# Generated by Django 4.0.6 on 2022-10-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_product_user'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('sort', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активировано')),
                ('products', models.ManyToManyField(to='catalog.product', verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'Карусель товаров',
                'verbose_name_plural': 'Карусели товаров',
                'ordering': ['sort'],
            },
        ),
    ]
