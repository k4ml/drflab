from rest_framework.views import APIView
from rest_framework.response import Response

from drflab.serializers import (
    CustomerSerializer,
    CustomerSerializerOverride
)

class CustomerResource(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CustomerResourceOverride(APIView):
    def post(self, request):
        assert 'extra' in request.data
        serializer = CustomerSerializerOverride(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
