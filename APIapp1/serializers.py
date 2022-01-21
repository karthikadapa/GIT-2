
from rest_framework import serializers

from .models import KarthikModel


class KarthikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KarthikModel
        fields = ('name','id1','salary')
