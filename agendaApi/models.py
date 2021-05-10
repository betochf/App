from django.db import models

# Create your models here.

class Contact(models.Model):
    
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name