from django.http import HttpResponse
from .models import Agent
from Managers.views import ManagerProcessing
from bitrix.views import DataAPIBitrix24


class AgentFromClient:
    def __init__(self, idDeal, idManager, idContact):
        self.idDeal = idDeal
        self.idManager = idManager
        self.idContact = idContact


    def agentRegistration(self):
        try:
            manager = ManagerProcessing(id=self.idManager).getManager()
            agent = AgentProcessing(idContact = self.idContact, idManager=manager, idDeal=self.idDeal).getAgent()
            return agent
        except Exception as e:
            print(e)
            return 'Ошибка'


    def wasTrained(self):
        get = AgentProcessing.trained('id')
        if get == 'True':
            return HttpResponse('True')
        else:
            return HttpResponse(get)


class AgentProcessing:
    def __init__(self, idContact, idManager, idDeal):
        self.idContact = idContact
        self.bitrix = DataAPIBitrix24()
        self.idManager = idManager
        self.idDeal = idDeal


    def getAgent(self):
        if self.checkInBitrix():
            try:
                get = self.bitrix._B.callMethod('crm.contact.get', ID=self.idContact)
                self.saveAgent(data = get)
                return 'Агент добавлен'
            except Exception as e:
                raise NameError (e)
        else:
            return 'Такой агент уже есть в базе'


    def saveAgent(self, data):
        agent = Agent(
            name = data['NAME'],
            lastName = data['LAST_NAME'],
            patronymic = data['SECOND_NAME'],
            idFromBitrix = data['ID'],
            personalManager_id = self.idManager.id,
            idDeal = self.idDeal
        )
        agent.save()
        return True


    def checkInBitrix(self):
        try:
            get = Agent.objects.get(idFromBitrix=self.idContact)
            return False
        except Exception as e:
            return True


def clientEndEducation(idDeal):
    try:
        get = Agent.objects.get(idDeal=idDeal)
        get.education = True
        get.save()
        updateDeal = DataAPIBitrix24._B.callMethod('crm.deal.update', ID=idDeal, fields={
            "UF_CRM_1676967434": 26068
        })
        return 'Обновлено'
    except Agent.DoesNotExist:
        return 'Такой сделки нет в базе данных'

def clientStartEducation(idDeal):
    updateDeal = DataAPIBitrix24._B.callMethod('crm.deal.update', ID=idDeal, fields={
        "UF_CRM_1676967409": 26064
    })
    return 'Обновлено'