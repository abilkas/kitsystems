from django.contrib import admin

# Register your models here.
from .models import Task, ChangeStatus, Reminder
admin.site.register(Task)
admin.site.register(ChangeStatus)
admin.site.register(Reminder)



