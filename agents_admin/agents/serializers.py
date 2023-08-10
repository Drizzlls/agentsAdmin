from rest_framework import serializers

class ClietnAgentSerializer(serializers.Serializer):
    idDeal = serializers.IntegerField()
    idManager = serializers.IntegerField()
    idContact = serializers.IntegerField()

class EducationClietnAgentSerializer(serializers.Serializer):
    idDeal = serializers.IntegerField()

class DataFromMessageSerializer(serializers.Serializer):
    idDeal = serializers.IntegerField()