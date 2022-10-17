from django.db import models
from agents.models import Agent

class Leads(models.Model):
    name = models.CharField(max_length=50,verbose_name = 'Имя')
    lastName = models.CharField(max_length=50,null=True, verbose_name = 'Фамилия')
    agent = models.ForeignKey(Agent,on_delete=models.SET_DEFAULT, default=None,null=True, verbose_name = 'Агент')
    phone = models.IntegerField(unique=True,null=False, verbose_name = 'Номер телефона')
    date = models.DateTimeField (auto_now_add = True, verbose_name = 'Дата заявки')

