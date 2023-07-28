from django.contrib import admin
from .models import RegisteredVehicle
# Register your models here.
class RVAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'plate_number']


admin.site.register(RegisteredVehicle, RVAdmin)
