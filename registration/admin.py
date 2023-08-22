from django.contrib import admin
from .models import Participant

# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["full_name","email"]


admin.site.register(Participant,ParticipantAdmin)
