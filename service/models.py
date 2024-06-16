from django.db import models
class Service(models.Model):

    username = None
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []




# Create your models here.
