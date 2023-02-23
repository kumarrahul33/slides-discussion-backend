from rest_framework import serializers
from base.models import SlideQue
class SlideQueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideQue
        fields = '__all__'