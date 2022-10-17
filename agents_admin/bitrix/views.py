from django.shortcuts import render
from bitrix24 import *


class DataAPIBitrix24:
    _WEBHOOK = "https://novoedelo.bitrix24.ru/rest/16/fpxyso83jr4wfxpl/"
    _B = Bitrix24(_WEBHOOK)
