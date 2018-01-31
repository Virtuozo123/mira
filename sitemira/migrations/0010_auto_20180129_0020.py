# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitemira', '0009_auto_20180129_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='third_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='create',
            name='chosen_category',
            field=models.CharField(choices=[(None, 'Выберите категорию'), ('Пенсионеры и Инвалиды', 'Пенсионеры и Инвалиды'), ('Малоимущие семьи', 'Малоимущие семьи'), ('Больные дети и сироты', 'Больные дети и сироты'), ('Храмы и монастыри', 'Храмы и монастыри'), ('Заключеные', 'Заключенные'), ('Дома милосердия', 'Дома милосердия')], default=None, max_length=100, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='create',
            name='chosen_category_2',
            field=models.CharField(choices=[(None, 'Выберите вид'), ('Материальная', 'Материальная'), ('Нематериальная', 'Нематериальная')], default=None, max_length=100, null=True, verbose_name='Вид помощи'),
        ),
        migrations.AlterField(
            model_name='create',
            name='coordinates',
            field=models.TextField(max_length=300, null=True, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='create',
            name='description',
            field=models.TextField(max_length=2000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='create',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='@Почта'),
        ),
        migrations.AlterField(
            model_name='create',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='create',
            name='logo_pic',
            field=models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Логотип проекта/Фотография'),
        ),
        migrations.AlterField(
            model_name='create',
            name='low_description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='create',
            name='organizathion_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название организации'),
        ),
        migrations.AlterField(
            model_name='create',
            name='phone',
            field=models.CharField(max_length=12, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='create',
            name='second_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия'),
        ),
    ]
