from rest_framework import serializers
from .models import mathlib, langlib, netlib, utillib

class MathlibSerializer(serializers.ModelSerializer):
    class Meta:
        model = mathlib
        fields = ['math_id', 'math_name']

class LanglibSerializer(serializers.ModelSerializer):
    class Meta:
        model = langlib
        fields = ['lang_id', 'lang_name']

class NetlibSerializer(serializers.ModelSerializer):
    class Meta:
        model = netlib
        fields = ['net_id', 'net_name']

class UtillibSerializer(serializers.ModelSerializer):
    class Meta:
        model = utillib
        fields = ['util_id', 'util_name']
