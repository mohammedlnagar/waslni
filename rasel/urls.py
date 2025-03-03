
# from django.urls import path
# from .views import viewLists


# urlpatterns = [
#     path('Arkam/', viewLists, name='contact_lists'),
# ]

from django.urls import path
from .views import (manage_appointments_and_messages, appointment_list_detail,
                    edit_assigned_message, update_assigned_message_status, 
                    filter_assigned_messages, export_assigned_messages_to_csv, update_contact_details)
urlpatterns = [
    path('AppointmentsManage/', manage_appointments_and_messages, name='manage_appointments'),
    path('list/<int:list_id>/', appointment_list_detail, name='appointment_list_detail'),
    path('EditMessage/', edit_assigned_message, name='EditMessage'),
    path('update-message-status/', update_assigned_message_status, name='update_assigned_message_status'),
    path('list/<int:list_id>/filter-messages/', filter_assigned_messages, name='filter_assigned_messages'),
    path('list/<int:list_id>/export-csv/', export_assigned_messages_to_csv, name='export_assigned_messages_to_csv'),
    path('update-contact/', update_contact_details, name='update_contact_details'),

]


