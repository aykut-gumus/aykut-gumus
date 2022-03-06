from rest_framework import viewsets
from django.core import serializers
from api.models import Job as dbmodel
from api.serializers import JobSerializer as serializer


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Jobs to be viewed or edited.
    """
    queryset = dbmodel.objects.all().order_by()
    serializer_class = serializer
