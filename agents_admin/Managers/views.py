from django.shortcuts import render
from bitrix.views import DataAPIBitrix24
from .models import Manager

class ManagerProcessing:
    def __init__(self, id):
        self.id = id
        self.bitrix = DataAPIBitrix24()


    def checkInBitrix(self):
        get = self.bitrix._B.callMethod("user.get", ID=self.id)
        if not get:
            raise NameError('Менеджера с таким ID в Битрикс24 отсутствует')
        else:
            return self.setManager(get)


    def setManager(self,get):
        set = Manager(name=get[0]['NAME'],lastName=get[0]['LAST_NAME'],patronymic=get[0]['SECOND_NAME'],idFromBitrix=get[0]['ID'])
        set.save()
        return set


    def getManager(self):
        try:
            get = Manager.objects.get(idFromBitrix=self.id)
            return get
        except:
            return self.checkInBitrix()