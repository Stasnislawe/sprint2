from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .choices import LEVELS_CHOICES, STATUS_CHOICES

# Create your models here.

class User(models.Model):
    """"Пользователи"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    otc = models.CharField(max_length=100, verbose_name='Отчество')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=12, verbose_name='Телефон')

    def __str__(self):
        return f'{self.pk}: {self.name} {self.surname}'

class Coords(models.Model):
    """"Координаты перевала"""
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], default=34.3,
                                 verbose_name="Широта", help_text="Широта в градусах")
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], default=61.8,
                                  verbose_name="Долгота", help_text="Долгота в градусах")
    height = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(8848)], default=0,
                                 verbose_name="Высота", help_text="Высота в метрах над уровнем моря")


class DifficultyLevel(models.Model):
    winter = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Зима')
    summer = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Лето')
    autumn = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Осень')
    spring = models.CharField(choices=LEVELS_CHOICES, max_length=6, null=True, blank=True, verbose_name='Весна')

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"

class AddMount(models.Model):
    beauty_title = models.CharField(default='пер.', max_length=255, verbose_name='Красивое название')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_titles = models.CharField(max_length=255, verbose_name='Другое название')
    connect = models.CharField(max_length=1, default="", blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    user = models.ForeignKey(User, related_name='mount_user', on_delete=models.CASCADE, verbose_name='Автор')
    coord = models.OneToOneField(Coords, related_name='mount_coord', on_delete=models.CASCADE, verbose_name='Координаты')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NW', verbose_name='Статус')
    level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE, verbose_name='Уровень сложности')

    def __str__(self):
        return f"{self.pk} - {self.beauty_title}"

class Images(models.Model):
    mount = models.ForeignKey(AddMount, on_delete=models.CASCADE, related_name='images', null=True, blank=True, verbose_name='Фото перевала')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Название")
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, verbose_name="Фото")

    def __str__(self):
        return f"Фото: {self.mount}"