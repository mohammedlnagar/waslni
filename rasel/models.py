
from django.db import models
from django.conf import settings

# -------------------------------
# 1. Appointment List (Each CSV Upload)
# -------------------------------
class AppointmentsList(models.Model):
    title = models.CharField(max_length=230)  # Example: "Appointments - March 2025"
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    message_selected = models.ManyToManyField('MessageTemplate', blank=True)  # Messages assigned to the list
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user who uploaded the CSV

    def __str__(self):
        return self.title


# -------------------------------
# 2. Contact (Unique Patients)
# -------------------------------
class Contact(models.Model):
    name = models.CharField(max_length=230)
    phone_number = models.CharField(max_length=20, unique=True)  # Ensures no duplicate contacts
    file_number = models.CharField(max_length=230, unique=True, blank=True, null=True)  # Optional unique patient ID

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


# -------------------------------
# 3. Appointment (Links Contacts to Appointment Lists)
# -------------------------------
class Appointment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)  # Links appointment to a unique contact
    appointments_list = models.ForeignKey(AppointmentsList, on_delete=models.CASCADE)  # Links to uploaded CSV batch
    doctor_name = models.CharField(max_length=230, default=" ")
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)
    appointment_remarks = models.CharField(max_length=230, blank=True, null=True)
    appointment_status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"Appointment for {self.contact.name} on {self.appointment_date}"


# -------------------------------
# 4. Message Template (Predefined Messages)
# -------------------------------
class MessageTemplate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user who created this template
    category = models.CharField(max_length=255)  # Message type (e.g., "Reminder", "Follow-up")
    content = models.TextField()  # The actual message text

    def __str__(self):
        return f"{self.category} - {self.content[:50]}"


# -------------------------------
# 5. Assigned Message (Customizable Messages Per Appointment)
# -------------------------------
# class AssignedMessage(models.Model):
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)  # Links to a specific appointment
#     message_template = models.ForeignKey(MessageTemplate, on_delete=models.SET_NULL, null=True, blank=True)  # Optional predefined template
#     custom_message = models.TextField(blank=True, null=True)  # Allows user customization before sending

#     status = models.CharField(
#         max_length=10,
#         choices=[('sent', 'Sent'), ('pending', 'Pending'), ('ignored', 'Ignored')],
#         default='pending'
#     )
#     sent_at = models.DateTimeField(null=True, blank=True)  # Timestamp of when the message was sent

#     def __str__(self):
#         return f"Message for {self.appointment.contact.name} - Status: {self.status}"

class AssignedMessage(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    message_template = models.ForeignKey(MessageTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    custom_message = models.TextField(blank=True, null=True)
    
    status = models.CharField(
        max_length=10,
        choices=[('sent', 'Sent'), ('pending', 'Pending'), ('ignored', 'Ignored')],
        default='pending'
    )
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Message for {self.appointment.contact.name} - Status: {self.status}"
