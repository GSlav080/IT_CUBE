from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class INFORMATION(models.Model):
    NAME = models.CharField('НАЗВАНИЕ КУРСА: ', max_length=22)
    YEAR = models.CharField('ВОЗРАСТ: ', max_length=50)
    NAME_TEACHER = models.CharField('ФИО ПРЕПОДВАТЕЛЕЙ: ', max_length=100)
    INFO = models.TextField('О КУРСЕ', max_length=500)
    N = models.CharField('Номер кабинета', max_length=2)
    def __str__(self):
        return self.NAME
class USER_REG(models.Model):
    NAME = models.CharField('ФИО: ', max_length=100)
    YEAR = models.PositiveSmallIntegerField('ВОЗРАСТ: ',validators=[MinValueValidator(1),
                                       MaxValueValidator(100)])
    NUMBER = models.CharField('Контактный телефон: ', max_length=30)
    KURS = models.TextField('Название курса', max_length=500)
    USER = models.CharField('USER: ', max_length=100)
    def __str__(self):
        return self.USER