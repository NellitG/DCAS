from django.db import models

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    advisory_type = models.CharField(max_length=50)

    scheduled_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name