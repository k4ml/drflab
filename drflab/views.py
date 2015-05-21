from rest_framework.views import APIView
from rest_framework.response import Response

from drflab.serializers import CustomerSerializer

class CustomerResource(APIView):
    def post(self, request):
        import pdb;pdb.set_trace()
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
