from celery import shared_task
from .models import Message
from integrations.sms import send_sms

@shared_task
def send_sms_task(message_id):
    message = Message.objects.get(id=message_id)

    try:
        response = send_sms(
            phone=message.farmer.phone_number,
            text=message.content
        )

        message.status = "sent"
        message.external_id = response.get("message_id")

    except Exception as e:
        message.status = "failed"
        message.error_message = str(e)

    message.save()