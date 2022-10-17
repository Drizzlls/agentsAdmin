from django.shortcuts import render
from django.http import HttpResponse
from .models import Agent
from bitrix.views import DataAPIBitrix24
import pprint
from Managers.views import ManagerProcessing


def agentRegistration(request):
    try:
        manager = ManagerProcessing(id=request.POST['Manager']).getManager()
        agent = AgentProcessing(id = request.POST['Agent'], manager=manager,idDeal=request.POST['idDeal']).getAgent()
        return HttpResponse(agent)
    except Exception as e:
        return HttpResponse(e)


def wasTrained(request):
    get = AgentProcessing.trained(request.GET['ID'])
    if get == 'True':
        return HttpResponse('True')
    else:
        return HttpResponse(get)


class AgentProcessing:
    def __init__(self, id, manager, idDeal):
        self.id = id
        self.bitrix = DataAPIBitrix24()
        self.manager = manager
        self.idDeal = idDeal


    def getAgent(self):
        if self.checkInBitrix():
            try:
                get = self.bitrix._B.callMethod('crm.contact.get', ID=self.id)
                self.saveAgent(get)
            except Exception as e:
                raise NameError (e)
        else:
            return 'Такой агент уже есть в базе'


    def saveAgent(self,data):
        agent = Agent(
            name = data['NAME'],
            lastName = data['LAST_NAME'],
            patronymic = data['SECOND_NAME'],
            idFromBitrix = data['ID'],
            personalManager_id = self.manager.id,
            idDeal = self.idDeal
        )
        agent.save()
        return data


    def checkInBitrix(self):
        try:
            get = Agent.objects.get(idFromBitrix=self.id)
            return False
        except:
            return True


    @staticmethod
    def trained(idDeal):
        try:
            get = Agent.objects.get(idDeal = idDeal)
            get.education = True
            get.save()
            updateDeal = DataAPIBitrix24._B.callMethod('crm.deal.update', ID=idDeal, fields={
                "TITLE": 'Он прошел обучение'
            })
            return 'True'
        except Agent.DoesNotExist:
            return 'Такой сделки нет в базе данных'




