from django.db import models
from Managers.models import Manager


class Agent(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50,null=True)
    patronymic = models.CharField(max_length=50,null=True)
    idFromBitrix = models.IntegerField(unique=True,null=False)
    education = models.BooleanField(default=False, blank=True)
    education_n = models.BooleanField(default=False, blank=True)
    personalManager = models.ForeignKey(Manager,on_delete=models.SET_DEFAULT, default=None,null=True)
    idDeal = models.IntegerField(null=False)

