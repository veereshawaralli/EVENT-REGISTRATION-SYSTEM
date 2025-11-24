from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, Registration
from django.utils import timezone
from datetime import timedelta

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass')
        # profile auto-created by signals
        self.user.profile.role = 'organizer'
        self.user.profile.save()
        now = timezone.now()
        self.event = Event.objects.create(
            title='Test Event',
            description='desc',
            category='technical',
            date_time=now + timedelta(days=5),
            venue='Online',
            reg_start_date=now - timedelta(days=1),
            reg_end_date=now + timedelta(days=3),
            created_by=self.user,
            is_active=True
        )

    def test_registration_create(self):
        participant = User.objects.create_user(username='p1', password='pass')
        reg = Registration.objects.create(event=self.event, participant=participant)
        self.assertEqual(self.event.registration_count, 1)
