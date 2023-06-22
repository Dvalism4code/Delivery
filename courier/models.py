from django.db import models
import uuid
from django.utils import timezone


class TrackingNumber(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'Active'
        INACTIVE = 'Inactive'
        INTRANSIT = 'In transit'
        PICKED = 'Picked Up'
        ARRIVED = 'Arrived'
        DELIVERED = 'Delivered'
        ONHOLD = 'On Hold'
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='TRACKER ID')
    sender_name = models.CharField(max_length=50)
    sender_phone = models.IntegerField()
    sender_email = models.EmailField()
    sender_address = models.CharField(max_length=80)
    receiver_name = models.CharField(max_length=50)
    receiver_phone = models.IntegerField()
    receiver_email = models.EmailField()
    receiver_address = models.CharField(max_length=80)
    parcel_description = models.CharField(max_length=200)
    dispatch_location = models.CharField(max_length=200)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.INTRANSIT)
    dispatch_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateField()
    current_location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.unique_id)


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    subject = models.CharField(max_length=50, default=True)

    def __str__(self):
        return self.name
