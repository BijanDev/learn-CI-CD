from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheck(APIView):
    def get(self, request):
        return Response({'message': 'Hello from server'}, status=status.HTTP_200_OK)
