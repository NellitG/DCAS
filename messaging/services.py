from .models import Message
from farmers.models import Farmer

def generate_messages(campaign, filters, text):
    farmers = Farmer.objects.filter(**filters)

    messages = [
        Message(
            farmer=farmer,
            campaign=campaign,
            content=text,
        ) for farmer in farmers 
    ]

    Message.objects.bulk_create(messages)