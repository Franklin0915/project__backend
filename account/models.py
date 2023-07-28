from django.db import models

# Create your models here.
class RegisteredVehicle(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="White")
    plate_number = models.CharField(max_length=255)
    owner_fullname = models.CharField(max_length=255)
    registered_at = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    