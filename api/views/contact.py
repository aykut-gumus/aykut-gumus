from rest_framework import viewsets
from django.core import serializers
from api.models import Contact as dbmodel
from api.serializers import ContactSerializer as serializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contacts to be viewed or edited.
    """
    queryset = dbmodel.objects.all().order_by()
    serializer_class = serializer
