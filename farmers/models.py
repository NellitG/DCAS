from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)

    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)

    value_chain = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
