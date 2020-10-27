from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.all_notes, name='all_notes'),
    path('add/', views.add_note, name='add_note')
]
