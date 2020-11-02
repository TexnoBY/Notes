from django.urls import path
from django.shortcuts import redirect
from django.urls import include

from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.redirect_to_main_or_login, name='to_main_or_login'),
    # path('user/<str:username>/', views.NoteListView.as_view(), name='all_notes'),
    path('user/<str:username>/', views.all_notes, name='all_notes'),
    path('<int:note_id>/', views.delete_note, name='delete_note'),
    path('add/', views.add_note, name='add_note'),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]

