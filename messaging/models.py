from django.db import models
from farmers.models import Farmer
from campaigns.models import Campaign

class Message(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    content = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    external_id = models.CharField(max_length=255, null=True, blank=True)

    sent_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)

    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.farmer} - {self.status}"