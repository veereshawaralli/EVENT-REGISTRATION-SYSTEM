from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/register/', views.register_event, name='register_event'),
    path('dashboard/organizer/', views.organizer_dashboard, name='organizer_dashboard'),
    path('dashboard/participant/', views.participant_dashboard, name='participant_dashboard'),
    path('organizer/event/create/', views.event_create, name='event_create'),
    path('organizer/event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('organizer/event/<int:pk>/export_csv/', views.export_participants_csv, name='export_participants_csv'),
]
