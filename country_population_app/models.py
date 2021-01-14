from django.db import models
from colorfield.fields import ColorField


class Country(models.Model):
    """Модель для сохранения названия страны популяции и цвета(для вывода на диаграмму) """
    name = models.CharField(max_length=100, verbose_name='Название страны')
    color = ColorField(verbose_name='Цвет колонки')
    population = models.PositiveBigIntegerField(verbose_name='Численность населения')

    def __str__(self):
        return self.name
