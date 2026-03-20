# campaigns/tasks.py

from celery import shared_task
from django.utils.timezone import now
from .models import Campaign

@shared_task
def process_scheduled_campaigns():
    campaigns = Campaign.objects.filter(
        scheduled_at__lte=now(),
        status="pending"
    )

    for campaign in campaigns:
        print(f"Processing campaign: {campaign.name}")

        campaign.status = "processed"
        campaign.save()