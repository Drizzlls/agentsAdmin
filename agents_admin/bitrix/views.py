from django.shortcuts import render
from bitrix24 import *


class DataAPIBitrix24:
    _WEBHOOK = "https://novoedelo.bitrix24.ru/rest/24/d4k293pu21gr1f39/"
    _B = Bitrix24(_WEBHOOK)
