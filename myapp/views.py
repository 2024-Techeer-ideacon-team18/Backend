from rest_framework import generics
from .models import mathlib, langlib, netlib, utillib
from .serializers import MathlibSerializer, LanglibSerializer, NetlibSerializer, UtillibSerializer

# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import mathlib, langlib, netlib, utillib
from .serializers import MathlibSerializer, LanglibSerializer, NetlibSerializer, UtillibSerializer


class MathlibList(APIView):
    def get(self, request, *args, **kwargs):
        math_data = mathlib.objects.all()[:15]
        lang_data = langlib.objects.all()[:5]
        net_data = netlib.objects.all()[:5]
        #util_data = utillib.objects.all()[:5]

        math_serializer = MathlibSerializer(math_data, many=True)
        lang_serializer = LanglibSerializer(lang_data, many=True)
        net_serializer = NetlibSerializer(net_data, many=True)
        #util_serializer = UtillibSerializer(util_data, many=True)

        combined_data = {
            'mathlib': math_serializer.data,
            'langlib': lang_serializer.data,
            'netlib': net_serializer.data
            #'utillib': util_serializer.data
        }

        return Response(combined_data)
