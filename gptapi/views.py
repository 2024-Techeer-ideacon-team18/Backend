from django.shortcuts import render
from prompt import resultGpt
from rest_framework.response import Response
from rest_framework.views import APIView

class ResultGpt(APIView):
    def get(self, request, *args, **kwargs) :

        combined_data = {
            'resultGpt': resultGpt()
        }

        return Response(combined_data)
