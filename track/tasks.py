from celery import shared_task

from .to_send_email import send_email_changed

#passing celery
@shared_task
def send_email(instance):
	send_email_changed(instance)