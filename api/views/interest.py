from rest_framework import viewsets
from django.core import serializers
from api.models import Interest as dbmodel
from api.serializers import InterestSerializer as serializer


class InterestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interests to be viewed or edited.
    """
    queryset = dbmodel.objects.all().order_by()
    serializer_class = serializer
