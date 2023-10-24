from django.db import models
import datetime

# Create your models here.

class Address(models.Model):
    address = models.TextField()
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    class Meta:
        verbose_name_plural = "Addresses"

class TrafficReport(models.Model):
    start_location = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='traffic_start', null=True)
    end_location = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='traffic_end', null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    travel_time = datetime.timedelta(minutes=14, seconds=30)
    duration = models.DurationField(editable=False, default=travel_time, auto_created=True)

    
    def save(self, *args, **kwargs):
        # Could call api here and prevent editing in the future
        # self.duration = datetime.timedelta(minutes=14, seconds=30)
        super().save(*args, **kwargs)
        