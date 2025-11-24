from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, EventForm
from django.contrib.auth import login
from django.http import HttpResponse
import csv

def index(request):
    events = Event.objects.filter(is_active=True, reg_end_date__gte=timezone.now()).order_by('date_time')
    return render(request, 'events/index.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_active=True)
    registered = False
    if request.user.is_authenticated:
        registered = Registration.objects.filter(event=event, participant=request.user, status='registered').exists()
    return render(request, 'events/event_detail.html', {'event': event, 'registered': registered})

@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk, is_active=True)
    now = timezone.now()
    if not (event.reg_start_date <= now <= event.reg_end_date):
        messages.error(request, 'Registration for this event is not open.')
        return redirect('events:event_detail', pk=pk)

    # check duplicate
    if Registration.objects.filter(event=event, participant=request.user, status='registered').exists():
        messages.info(request, 'You are already registered for this event.')
        return redirect('events:event_detail', pk=pk)

    # check capacity
    if event.max_participants and event.registration_count >= event.max_participants:
        messages.error(request, 'Event capacity is full.')
        return redirect('events:event_detail', pk=pk)

    Registration.objects.create(event=event, participant=request.user)
    messages.success(request, 'Registration successful.')
    return redirect('events:participant_dashboard')

@login_required
def organizer_dashboard(request):
    events = Event.objects.filter(created_by=request.user).order_by('-date_time')
    return render(request, 'events/organizer_dashboard.html', {'events': events})

@login_required
def participant_dashboard(request):
    regs = request.user.registrations.select_related('event').order_by('-registration_date')
    return render(request, 'events/participant_dashboard.html', {'registrations': regs})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            # save profile extras
            role = form.cleaned_data.get('role')
            phone = form.cleaned_data.get('phone')
            user.profile.role = role
            user.profile.phone = phone
            user.profile.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            # redirect based on role
            if user.profile.role == 'organizer':
                return redirect('events:organizer_dashboard')
            return redirect('events:participant_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'events/signup.html', {'form': form})

@login_required
def event_create(request):
    # only organizer allowed to create events
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'organizer':
        messages.error(request, 'Only organizers can create events.')
        return redirect('events:index')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            ev = form.save(commit=False)
            ev.created_by = request.user
            ev.save()
            messages.success(request, 'Event created.')
            return redirect('events:organizer_dashboard')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'create': True})

@login_required
def event_edit(request, pk):
    ev = get_object_or_404(Event, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=ev)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated.')
            return redirect('events:organizer_dashboard')
    else:
        form = EventForm(instance=ev)
    return render(request, 'events/event_form.html', {'form': form, 'create': False, 'event': ev})

@login_required
def export_participants_csv(request, pk):
    ev = get_object_or_404(Event, pk=pk, created_by=request.user)
    participants = ev.registrations.select_related('participant').filter(status='registered')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{ev.title}_participants.csv"'

    writer = csv.writer(response)
    writer.writerow(['username','email','phone','registration_date'])
    for r in participants:
        profile = getattr(r.participant, 'profile', None)
        phone = profile.phone if profile else ''
        writer.writerow([r.participant.username, r.participant.email, phone, r.registration_date])

    return response
