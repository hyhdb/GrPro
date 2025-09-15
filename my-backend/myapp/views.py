from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

@method_decorator(never_cache, name='dispatch')
class ExampleView(APIView):
    def get(self, request):
        return Response({"medasdassdasdasdasdasage": "Hellooo, World!"}, status=status.HTTP_200_OK)
