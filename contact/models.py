from django.db import models
from datetime import datetime
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
