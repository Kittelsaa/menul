from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MenuItem 
from rest_framework import generics
from .serializers import MenuItemSerializer
from django.http import JsonResponse




class MenuItemListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MenuItemDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        menu_item = self.get_object(pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        menu_item = self.get_object(pk)
        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        menu_item = self.get_object(pk)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def custom_404(request, exception):
    response_data = {
        "error": "Not Found",
        "status_code": 404,
        "message": "The requested resource was not found."
    }
    return JsonResponse(response_data, status=404)

def custom_401(request, exception):
    response_data = {
        "error": "Unauthorized",
        "status_code": 401,
        "message": "Authentication credentials were not provided or are invalid."
    }
    return JsonResponse(response_data, status=401)
