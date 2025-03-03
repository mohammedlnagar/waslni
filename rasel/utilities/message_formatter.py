def format_message(template, appointment):
    """
    Replaces placeholders in the template with actual appointment details.

    Available placeholders:
    - #appointment_date
    - #appointment_time
    - #doctor
    - #patient_name
    - #appointment_status
    """
    placeholders = {
        "#appointment_date": appointment.appointment_date.strftime("%d-%m-%Y") if appointment.appointment_date else "N/A",
        "#appointment_time": appointment.appointment_time.strftime("%I:%M %p") if appointment.appointment_time else "N/A",
        "#doctor": appointment.doctor_name or "N/A",
        "#patient_name": appointment.contact.name or "N/A",
        "#appointment_status": appointment.appointment_status.capitalize(),
    }

    message = template
    for placeholder, value in placeholders.items():
        message = message.replace(placeholder, value)

    return message
