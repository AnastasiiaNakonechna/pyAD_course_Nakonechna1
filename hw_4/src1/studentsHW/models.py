from django.db import models

import random

# Create your models here.
# ORM - Object relation mapping

class Student(models.Model):
    first_name = models.CharField(max_length=64) #создаем столбец с данными, все символы 64 шт должны быть заполнены, если строка короче, то остаток заполняем пробелами
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField() # можно было просто выбрать models.IntegerField, но тогда можно было бы ввести и отрицательные значения, что для возраста не подходит +, -, -127 ... +127

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

    def inc_age(self) -> None:
        self.age +=1 #вносим изменения в базу и
        self.save() #и сохраняем эти изменения


class Group(models.Model):
    first_name = models.CharField(max_length=64) #создаем столбец с данными, все символы 64 шт должны быть заполнены, если строка короче, то остаток заполняем пробелами
    last_name = models.CharField(max_length=64)
    scores_in_group = models.PositiveSmallIntegerField() # можно было просто выбрать models.IntegerField, но тогда можно было бы ввести и отрицательные значения, что для возраста не подходит +, -, -127 ... +127

class Teachers(models.Model):
    first_name = models.CharField(max_length=64) #создаем столбец с данными, все символы 64 шт должны быть заполнены, если строка короче, то остаток заполняем пробелами
    last_name = models.CharField(max_length=64)

