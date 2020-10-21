from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .serializers import UserSerializer
from .models import User

class UserViewSet(ModelViewSet):
	model = UserSerializer
	queryset = User.objects.all()