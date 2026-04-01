from pydoc import text
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

def generate_messages_for_campaign(campaign, text=text):
    filters = {
        "county": campaign.county,
        "value_chain": campaign.value_chain,
        "gender": campaign.gender,
    }
    
    farmer=Farmer.objects.filter(**filters)
    
    messages = []
    for farmer in farmer:
        message = Message(
            farmer=farmer,
            campaign=campaign,
            content=text,
        )
        messages.append(message)

    Message.objects.bulk_create(messages)

    return messages