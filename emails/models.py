from django.db import models

# Create your models here.

class EmailEntry(models.Model):
    email = models.EmailField()
    updated_at = models.DateTimeField(auto_now=True) # Date time updated
    timestamp = models.DateTimeField(auto_now_add=True) # Date time added
