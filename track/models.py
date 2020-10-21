from django.db import models




#status options
planned = 'Планируется'
activated = 'Активная'
controle = 'Контроль'
complete = 'Завершена'

status_choice = [
				(planned, 'Планируется'),
				(activated, 'Активная'),
				(controle, 'Контроль'),
				(complete, 'Завершена')]



class Task(models.Model):
	name = models.CharField("Название", max_length=50) #Title
	description = models.TextField("Описание", blank=True, null=True) #Description
	executor = models.CharField("Исполнитель", max_length=50) #Executor
	observer = models.CharField("Наблюдатель", max_length=50) #Observer
	
	status = models.CharField("Статус", choices=status_choice, max_length=50) #Status
	start_time = models.DateTimeField("Дата начала", blank=True, null=True) #Start time
	complete_time = models.DateTimeField("Дата завершения", blank=True, null=True) #Complete time
	planned_complete_time = models.DateTimeField("Планируемая время завершения", blank=True, null=True) #Planned_complete_time
	changes_count = models.IntegerField("Сколько раз было изменено статус", default=0) #changes_count

	def __str__(self):
		return self.name




class ChangeStatus(models.Model):

	prev_status = models.CharField("Пред. статус", choices=status_choice, max_length=50)#prev status
	next_status = models.CharField("След. статус", choices=status_choice, max_length=50)#next status
	task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True) #connect the field to the Task model
	changed_by = models.CharField("Кто изменил", max_length=50, default='nikto') #who was changed

	def __str__(self):
		return str(self.task)

#Reminder
class Reminder(models.Model):
	task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True) #connect the field to the Task model
	text = models.TextField("Текст напоминания", blank=True, null=True) #Message
	users_list = models.CharField("Список пользователей", max_length=50) #to whom to send

	def __str__(self):
		return str(self.task)
