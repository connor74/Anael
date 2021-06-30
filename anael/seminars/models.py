from django.db import models
from django.utils import timezone


class Region(models.Model):
    region_name = models.CharField(max_length=250, verbose_name='Регион')

    class Meta:
        ordering = ('region_name',)
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=250, verbose_name='Город')
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               related_name='cities')

    class Meta:
        ordering = ('city_name',)
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city_name + ', ' + str(self.region)


class Seminar(models.Model):
    PUBLISHED = (
        ('draft', 'Скрыть'),
        ('published', 'Опубликовать'),
    )
    COSMOENERGY = (
        ('yes', 'Да'),
        ('no', 'Нет'),
    )
    title = models.CharField(max_length=250, verbose_name='Наименование')
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE,
                             related_name='seminars')
    slug = models.SlugField(max_length=250, unique_for_date='date_begin', verbose_name='Слаг')
    adress = models.CharField(max_length=300, verbose_name='Адрес')
    organizer = models.CharField(max_length=200, default='Центр космоэенргетики "Анаэль"', verbose_name='Организатор')
    phone_num1 = models.CharField(max_length=25, default='+7 961 595-02-20', verbose_name='Телефон 1')
    phone_num2 = models.CharField(max_length=25, verbose_name='Телефон 2')
    seo_keywords = models.CharField(max_length=250, verbose_name='Ключевые слова')
    date_begin = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    body = models.TextField(verbose_name='Текст')
    status = models.CharField(max_length=10,
                              choices=PUBLISHED,
                              default='draft')
    cosmoenergy = models.CharField(max_length=5,
                              choices=COSMOENERGY,
                              default='yes')

    class Meta:
        ordering = ('-date_begin',)
        verbose_name = 'Семинар'
        verbose_name_plural = 'Семинары'

    def __str__(self):
        return str(self.date_begin) + ' | ' + str(self.city) + ' | ' +self.title






# Create your models here.
