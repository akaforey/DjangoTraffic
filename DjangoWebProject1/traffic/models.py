from django.db import models
import datetime
import json
from ..DjangoWebProject1.secret import API_KEY
import requests

# Create your models here.

class Address(models.Model):
    address = models.TextField()
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    class Meta:
        verbose_name_plural = "Addresses"


def get_traffic(start, end):
    baseURL = "api.tomtom.com"
    versionNumber = "2"
    key = API_KEY
    
    postURL = f'https://{baseURL}/routemonitoring/{versionNumber}/routes?key={key}'

    body = {
        "name": "test",
        "pathPoints": [
            {"longitude": start.longitude, "latitude": start.latitude},
            {"longitude": end.longitude, "latitude": end.latitude}
        ]
    }
    json_body = json.dumps(body)
    
    try:
        post_response = requests.post(url=postURL, data=body)
        print(post_response.text)
        print(post_response.json())
        routeID = json.loads(post_response.json())["routeID"]
        getURL = f'https://{baseURL}/routemonitoring/{versionNumber}/routes/{routeID}?key={API_KEY}'
        get_response = requests.get(url=getURL)
        print(get_response.json())
    except requests.exceptions.JSONDecodeError as e:
        print(e)
        return None
        
    return json.loads(get_response.json())["travelTime"]
    

    
    
    
    
    
    


class TrafficReport(models.Model):
    start_location = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='traffic_start', null=True)
    end_location = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='traffic_end', null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    travel_time = datetime.timedelta(minutes=14, seconds=30)
    # travel_time = datetime.timedelta(seconds=get_traffic(start_location, end_location)
    duration = models.DurationField(editable=False, default=travel_time, auto_created=True)

    
    def save(self, *args, **kwargs):
        # Could call api here and prevent editing in the future
        # self.duration = datetime.timedelta(minutes=14, seconds=30)
        super().save(*args, **kwargs)
        