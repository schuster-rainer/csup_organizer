from django.contrib import admin

# Register your models here.
from .models import Track,Car

admin.site.register(Track)
admin.site.register(Car)