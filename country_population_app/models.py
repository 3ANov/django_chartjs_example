from django.db import models
from colorfield.fields import ColorField


class Country(models.Model):
    """Модель для сохранения названия страны популяции и цвета(для вывода на диаграмму) """
    country_name = models.CharField(max_length=100)
    color = ColorField()
    population = models.PositiveBigIntegerField()