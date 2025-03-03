from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Use email instead of username
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    # Fix for the system check error: Set unique related names
    groups = models.ManyToManyField(
        "auth.Group", related_name="custom_user_groups", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="custom_user_permissions", blank=True
    )

    USERNAME_FIELD = "email"  # Authenticate with email instead of username
    REQUIRED_FIELDS = ["username"]  # 'email' is already required

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    passport = models.ImageField(upload_to="documents/", blank=True, null=True)
    emirates_id = models.ImageField(upload_to="documents/", blank=True, null=True)
    university_certificate = models.FileField(
        upload_to="documents/", blank=True, null=True
    )
    cv = models.FileField(upload_to="documents/", blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    work_email = models.EmailField(blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    marital_status = models.CharField(
        max_length=20,
        choices=[("Single", "Single"), ("Married", "Married")],
        blank=True,
        null=True,
    )
    visa_copy = models.FileField(upload_to="documents/", blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

    def get_documents(self):
        return {
            self.passport: "Passport",
            self.emirates_id: "Emirates ID",
            self.university_certificate: "University Certificate",
            self.cv: "CV",
            self.visa_copy: "Visa Copy",
        }

    def __str__(self):
        return f"Profile of {self.user.email}"


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
