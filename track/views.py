from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Task, ChangeStatus, Reminder
from .serializers import TaskSerializer, ChangeStatusSerializer, ReminderSerializer

#views api
class TaskViewSet(ModelViewSet):
	serializer_class = TaskSerializer
	queryset = Task.objects.all()


class ChangeStatusViewSet(ModelViewSet):
	serializer_class = ChangeStatusSerializer
	queryset = ChangeStatus.objects.all()


class ReminderViewSet(ModelViewSet):
	serializer_class = ReminderSerializer
	queryset = Reminder.objects.all()

		
	

