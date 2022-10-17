from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    idFromBitrix = models.IntegerField(unique=True, null=False)

