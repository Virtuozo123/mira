from django.db import models
from django.utils import timezone
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class create(models.Model): 
    author = models.ForeignKey('auth.User',blank=True, null=True)
    name_project = models.CharField('Название проекта', max_length=100, null=True)
    first_name = models.CharField('Имя', max_length=20, blank=True, null=True)
    second_name = models.CharField('Фамилия', max_length=20, blank=True, null=True)
    third_name =models.CharField('Отчество', max_length=20, blank=True, null=True)
    organizathion_name = models.CharField('Название организации', max_length=50, blank=True, null=True)
    pensioner = 'Пенсионеры и Инвалиды'
    poor ='Малоимущие семьи'
    child = 'Больные дети и сироты'
    churches = 'Храмы и монастыри'
    prisoners = 'Заключеные'
    mercy = 'Дома милосердия'
    category =  reason_choises = (
                              (None,'Выберите категорию'),
                         (pensioner,'Пенсионеры и Инвалиды'),
                              (poor,'Малоимущие семьи'),
                             (child,'Больные дети и сироты'),
                          (churches,'Храмы и монастыри'),
                         (prisoners,'Заключенные'),
                             (mercy,'Дома милосердия'),
    )
    chosen_category = models.CharField('Категория', max_length=100, choices=category, default=None, null=True)
    material = 'Материальная'
    non_material = 'Нематериальная'
    category_2 = type_of_help = (
                                  (None,'Выберите вид'),
                              (material,'Материальная'),
                          (non_material,'Нематериальная'),
    )
    chosen_category_2 = models.CharField('Вид помощи', max_length=100, choices=category_2, default=None, null=True)
    low_description =  models.TextField('Краткое описание', max_length=300, blank=True, null=True)
    description =  models.TextField('Описание', max_length=2000, null=True)
    coordinates = models.TextField('Координаты', max_length=300, null=True)
    phone =  models.CharField('Телефон', max_length=12, null=True)
    email =  models.EmailField('@Почта', max_length=254, null=True)
    logo_pic = models.ImageField('Логотип проекта/Фотография', upload_to='media/%Y/%m/%d', max_length=100, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
     
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name_project
    

    
class Comment(models.Model):
    post = models.ForeignKey('sitemira.create', related_name='comments')
    author = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text    
    