from rest_framework import serializers
from .models import Task, ChangeStatus, Reminder

#Serializers and the fields that should be shown
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'name', 'description', 'executor', 'observer', 'status', 'start_time', 'complete_time', 'planned_complete_time', 'changes_count')

class ChangeStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChangeStatus
		fields = ('id', 'prev_status', 'next_status', 'task', 'changed_by')

class ReminderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reminder
		fields = ('id', 'task', 'text', 'users_list')