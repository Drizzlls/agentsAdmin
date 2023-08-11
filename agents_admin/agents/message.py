from bitrix.views import DataAPIBitrix24

class DataFromMessageClass:
    def __init__(self, idDeal):
        self.idDeal = idDeal

    def amountOfTrained(self):
        get = DataAPIBitrix24._B.callMethod('crm.deal.list', filter={"STAGE_ID":"C18:UC_76WFPI"})
        return {
            'amount': len(get)
        }

    def IdAssigned(self):
        get = DataAPIBitrix24._B.callMethod('crm.deal.get', ID=self.idDeal)
        return get['ASSIGNED_BY_ID']

    def dataAssigned(self):
        get = DataAPIBitrix24._B.callMethod('user.get', ID=self.IdAssigned())
        return {
            "phone": get[0].get('WORK_PHONE',''),
            "name": get[0]['NAME']
        }

    def getData(self):
        assigned = self.dataAssigned()
        amount = self.amountOfTrained()
        data = assigned.update(amount)
        return assigned
