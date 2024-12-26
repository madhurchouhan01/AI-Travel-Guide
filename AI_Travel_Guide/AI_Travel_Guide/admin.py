from django.contrib import admin
from .models import MyUser, Preferences, Trip

@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email","email_verified", "phone_number", "profile_picture", "is_active", "date_joined")

@admin.register(Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ("user", "max_distance", "budget", "duration")

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("user", "destination", "start_date", "end_date", "budget", "distance")
