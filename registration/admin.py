from django.contrib import admin
from .models import Participant
from django.http import HttpResponse
import csv
from django.utils.encoding import smart_str

# Register your models here.


def export_to_csv_action(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="model_data.csv"'

    writer = csv.writer(response)
    model_fields = [field.name for field in modeladmin.model._meta.fields]

    # Write header row
    writer.writerow(model_fields)

    # Write data rows
    for obj in queryset:
        writer.writerow([smart_str(getattr(obj, field)) for field in model_fields])

    return response
export_to_csv_action.short_description = "Export selected records to CSV"

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["full_name","email"]
    actions = [export_to_csv_action]  # Add export action

admin.site.register(Participant,ParticipantAdmin)