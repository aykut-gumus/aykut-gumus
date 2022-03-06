from rest_framework import viewsets
from django.core import serializers
from api.models import Social as dbmodel
from api.serializers import SocialSerializer as serializer


class SocialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Socials to be viewed or edited.
    """
    queryset = dbmodel.objects.all().order_by()
    serializer_class = serializer
