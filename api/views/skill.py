from rest_framework import viewsets
from django.core import serializers
from api.models import Skill as dbmodel
from api.serializers import SkillSerializer as serializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Skills to be viewed or edited.
    """
    queryset = dbmodel.objects.all().order_by()
    serializer_class = serializer
