from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    profile_picture = models.CharField(null=True, max_length=100)
    auth0_user_id = models.CharField(max_length=100, unique=True)


class Preferences(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="preferences")
    max_distance = models.FloatField(help_text="Maximum distance the user is willing to travel (in km).")
    budget = models.DecimalField(max_digits=10, decimal_places=2, help_text="Maximum budget for the trip.")
    duration = models.IntegerField(help_text="Number of days the user wants to travel.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Preferences"

class Trip(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="trips")
    destination = models.CharField(max_length=100, help_text="Name of the destination.")
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2, help_text="Budget allocated for this trip.")
    distance = models.FloatField(help_text="Distance to the destination (in km).")
    packing_checklist = models.TextField(help_text="Dynamic packing checklist for the trip.", blank=True, null=True)
    real_time_alerts = models.TextField(help_text="Real-time alerts related to the trip.", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Trip to {self.destination}"
