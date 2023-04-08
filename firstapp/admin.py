from django.contrib import admin
from .models import Cyber

# Register your models here.
@admin.register(Cyber)
class CyberAdmin(admin.ModelAdmin):
    list_display = "name","surname"