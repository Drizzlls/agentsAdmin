from bitrix24 import *
from django.http import HttpResponse

class DataAPIBitrix24:
    _WEBHOOK = "https://novoedelo.bitrix24.ru/rest/24/d4k293pu21gr1f39/"
    _B = Bitrix24(_WEBHOOK)


class FormData:
    def __init__(self, idDeal, data):
        self.idDeal = idDeal
        self.data = data
        self.bitrix = DataAPIBitrix24


    def addLeadFromBitrix(self):
            try:
                add = self.bitrix._B.callMethod(
                    "crm.lead.add",
                    fields={
                        "TITLE": "Лид от агента",
                        "NAME": self.data['NAME'],
                        "LAST_NAME": self.data['LAST_NAME'],
                        "STATUS_ID": "NEW",
                        "OPENED": "Y",
                        "PHONE": [{"VALUE": self.data['PHONE'], "VALUE_TYPE": "WORK"}],
                        "ASSIGNED_BY_ID": self.assignedPerson(),
                        "UF_CRM_1674717865": self.idDeal
                    }
                )
                return HttpResponse('True')
            except Exception as e:
                print(e)
                return e

    def assignedPerson(self):
        add = self.bitrix._B.callMethod(
            "crm.deal.get",ID=self.idDeal)
        return add['ASSIGNED_BY_ID']