from django.contrib import admin

# Register your models here.
from .models import FoodGood, FoodExperience

admin.site.register(FoodGood)
admin.site.register(FoodExperience)
