from rest_framework import serializers
from api.models import Social


class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
