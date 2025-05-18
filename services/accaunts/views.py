from .serializers import User_InformationSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class User_Information_viewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_InformationSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username = user)