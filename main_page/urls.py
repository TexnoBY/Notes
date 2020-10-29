from django.urls import path

from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='all_notes'),
    path('<int:note_id>/', views.delete_note, name='delete_note'),
    path('add/', views.add_note, name='add_note'),
]

