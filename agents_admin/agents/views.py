from django.shortcuts import render
from django.http import HttpResponse
from .models import Agent
from bitrix.views import DataAPIBitrix24
import pprint
from Managers.views import ManagerProcessing
from .serializers import ClietnAgentSerializer, EducationClietnAgentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .clients import AgentFromClient, clientEndEducation, clientStartEducation
from .agentsDirection import agentEndEducation, agentStartEducation


class AddAgentForClient(APIView):
    def post(self, request):
        serializer = ClietnAgentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = AgentFromClient(idDeal=request.data['idDeal'],idManager=request.data['idManager'],
                               idContact=request.data['idContact']).agentRegistration()
        clientStartEducation(idDeal=request.data['idDeal'])
        return Response(data)

class EducationAgentForClient(APIView):
    def post(self, request):
        serializer = EducationClietnAgentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = clientEndEducation(idDeal=request.data['idDeal'])
        return Response(data)


class AddAgentForDirection(APIView):
    def post(self, request):
        serializer = ClietnAgentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = AgentFromClient(idDeal=request.data['idDeal'],idManager=request.data['idManager'],
                               idContact=request.data['idContact']).agentRegistration()
        agentStartEducation(idDeal=request.data['idDeal'])
        return Response(data)


class EducationAgentForDirection(APIView):
    def post(self, request):
        serializer = EducationClietnAgentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = agentEndEducation(idDeal=request.data['idDeal'])
        return Response(data)




