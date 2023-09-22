from django.db import models

# Create your models here.
class RegisteredVehicle(models.Model):
    GENDER_LIST = [
        ('male', 'male'),
        ('female', 'female')
    ]
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="White")
    plate_number = models.CharField(max_length=255)
    owner_fullname = models.CharField(max_length=255)
    registered_at = models.CharField(max_length=255)
    drivers_image = models.ImageField(blank=True, null=True)
    cars_image = models.ImageField(blank=True, null=True)
    owner_gender = models.CharField(max_length=100, choices = GENDER_LIST, blank=True, null=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    Registered = models.BooleanField(default=False)
    owners_nationality = models.CharField(max_length=255)
    owners_age = models.CharField(max_length=255)
    registration_expiry = models.CharField(max_length=255)
    vehicle_category = models.CharField(max_length=255)
    chasis_number = models.CharField(max_length=255)
    national_identification = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    