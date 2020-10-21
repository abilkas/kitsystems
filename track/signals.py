from django.db.models import signals
from django.dispatch import receiver
from .tasks import send_email
from .models import Task

#catches a signal if the model fields have been changed
@receiver(signals.post_save, sender=Task)
def create_customer(sender, instance, **kwargs):
	send_email(instance).delay()
