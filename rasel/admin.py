from django.contrib import admin
from .models import AppointmentsList, Contact, Appointment, MessageTemplate, AssignedMessage
# Register your models here.
admin.site.register(AppointmentsList)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(MessageTemplate)
admin.site.register(AssignedMessage)