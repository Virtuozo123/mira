# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('second_name', models.CharField(blank=True, max_length=20, null=True)),
                ('chosen_category', models.CharField(blank=True, choices=[(None, 'Выберите категорию'), ('pensioner', 'Пенсионеры и Инвалиды'), ('poor', 'Малоимущие семьи'), ('child', 'Больные дети и сироты'), ('churches', 'Храмы и монастыри'), ('prisoners', 'Заключенные'), ('mercy', 'Дома милосердия')], default=None, max_length=100, null=True)),
                ('chosen_category_2', models.CharField(blank=True, choices=[(None, 'Выберите категорию'), ('material', 'Материальная'), ('non_material', 'Нематериальная')], default=None, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
