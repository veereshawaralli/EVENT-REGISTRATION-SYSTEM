from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('participant','Participant'),
        ('organizer','Organizer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='participant')
    phone = models.CharField(max_length=20, blank=True)
    organization = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('technical','Technical'),
        ('cultural','Cultural'),
        ('sports','Sports'),
        ('other','Other'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=255)
    reg_start_date = models.DateTimeField()
    reg_end_date = models.DateTimeField()
    max_participants = models.PositiveIntegerField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def registration_count(self):
        return self.registrations.filter(status='registered').count()

class Registration(models.Model):
    STATUS_CHOICES = [
        ('registered','Registered'),
        ('cancelled','Cancelled'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')

    class Meta:
        unique_together = ('event','participant')

    def __str__(self):
        return f"{self.participant.username} -> {self.event.title}"
