from rest_framework import serializers
from api.models import Interest


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'
