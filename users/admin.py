from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Food, Consume

# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)
