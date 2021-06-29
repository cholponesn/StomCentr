from rest_framework import serializers
from .models import *

class DaySerializer(serializers.Serializer):

    class Meta:
        model = Day
        fields = "__all__"