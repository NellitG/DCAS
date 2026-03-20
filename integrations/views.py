from rest_framework.decorators import api_view
from rest_framework.response import Response
from messaging.models import Message
from django.utils import timezone

@api_view(["POST"])
def delivery_callback(request):
    external_id = request.data.get("message_id")
    status = request.data.get("status")

    message = Message.objects.get(external_id=external_id)
    message.status = status

    if status == "delivered":
        message.delivered_at = timezone.now()

    message.save()

    return Response({"status": "ok"})