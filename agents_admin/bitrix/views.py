from django.shortcuts import render
from bitrix24 import *


class DataAPIBitrix24:
    _WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/4pzfo9y3vbk2e0t5/"
    _B = Bitrix24(_WEBHOOK)
