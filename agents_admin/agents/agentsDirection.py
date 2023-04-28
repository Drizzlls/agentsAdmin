from django.http import HttpResponse
from .models import Agent
from Managers.views import ManagerProcessing
from bitrix.views import DataAPIBitrix24



def agentEndEducation(idDeal):
    try:
        get = Agent.objects.get(idDeal=idDeal)
        get.education = True
        get.save()
        updateDeal = DataAPIBitrix24._B.callMethod('crm.deal.update', ID=idDeal, fields={
            "STAGE_ID": 'C18:UC_76WFPI'
        })
        print('Агент завершил обучение')
        return 'Агент завершил обучение'
    except Agent.DoesNotExist:
        print('Такой сделки нет в базе данных')
        return 'Такой сделки нет в базе данных'

def agentStartEducation(idDeal):
    updateDeal = DataAPIBitrix24._B.callMethod('crm.deal.update', ID=idDeal, fields={
        "STAGE_ID": 'C18:PREPAYMENT_INVOIC'
    })
    print('Агент приступил к обучению')
    return 'Обновлено'