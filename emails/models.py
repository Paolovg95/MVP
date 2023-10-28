from django.db import models

# Create your models here.

class EmailEntry(models.Model):
    email = models.EmailField()
<<<<<<< HEAD
    name = models.CharField(max_length=100)
=======
>>>>>>> 29ea5ac9f08d046164cf2fbf5731d5a5aee3406d
    updated_at = models.DateTimeField(auto_now=True) # Date time updated
    timestamp = models.DateTimeField(auto_now_add=True) # Date time added
