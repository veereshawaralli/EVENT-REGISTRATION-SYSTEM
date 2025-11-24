from django import forms
from .models import Event, Registration, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','description','category','date_time','venue','reg_start_date','reg_end_date','max_participants','is_active']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username','email','password1','password2','phone','role')
