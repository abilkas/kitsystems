from django.core.mail import send_mail

#function that sends the letter
def send_email_changed(instance):
	send_mail('Статус был изменен', f'Здравствуйте, статус был изменен на {instance.status}', 
		'tvoiemail', 
		['komu@email.com'], 
		fail_silently=False)