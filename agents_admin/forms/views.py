from django.shortcuts import render
from django.http import HttpResponse
from agents.models import Agent
from Managers.models import Manager
from bitrix.views import DataAPIBitrix24


def pageForm(request, idAgent):
    return render(request, 'forms/personalForm.html',{'AGENT' : idAgent})


def checkForm(request):
    agent = FormProcessing(id=request.POST['AGENT'], data=request.POST).addLeadFromBitrix()
    if agent == True:
        return HttpResponse('True')
    else:
        return HttpResponse(agent)


def index(request):
    return render(request,'forms/personalForm.html')


class FormProcessing:
    def __init__(self,id,data):
        self.id = id
        self.bitrix = DataAPIBitrix24()
        self.data = data


    def checkInBase(self):
        try:
            getAgent = Agent.objects.get(idFromBitrix=self.id)
            return True
        except Agent.DoesNotExist:
            return 'Такого агента нет в базе'


    def addLeadFromBitrix(self):
        if self.checkInBase() == True:
            try:
                getAgent = Agent.objects.get(idFromBitrix=self.id)
                add = self.bitrix._B.callMethod(
                    "crm.lead.add",
                    fields={
                        "TITLE": "Лид от агента",
                        "NAME": self.data['NAME'],
                        "LAST_NAME": self.data['LAST_NAME'],
                        "STATUS_ID": "NEW",
                        "OPENED": "Y",
                        "PHONE": [{"VALUE": self.data['PHONE'], "VALUE_TYPE": "WORK"}],
                        "ASSIGNED_BY_ID" : getAgent.personalManager.idFromBitrix,
                        "UF_CRM_1674717838" : getAgent.idFromBitrix,
                        "UF_CRM_1674717865" : getAgent.idDeal
                    }
                )
                return True
            except Exception as e:
                return e
        else:
            return self.checkInBase()