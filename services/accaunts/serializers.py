from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class User_InformationSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'date_joined')
