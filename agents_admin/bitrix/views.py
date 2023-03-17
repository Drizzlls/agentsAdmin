from django.shortcuts import render
from bitrix24 import *


class DataAPIBitrix24:
    _WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/l4963lnfla2m21ww/"
    _B = Bitrix24(_WEBHOOK)
