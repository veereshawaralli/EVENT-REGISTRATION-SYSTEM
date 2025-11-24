from django.contrib import admin
from .models import Profile, Event, Registration

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','role','organization')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','category','date_time','venue','is_active','created_by')
    list_filter = ('category','is_active')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event','participant','registration_date','status')
    list_filter = ('status',)
