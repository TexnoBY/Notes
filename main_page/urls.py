from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main_page'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='all_notes'),
    path('<int:note_id>/', views.delete_note, name='delete_note'),
    path('add/', views.add_note, name='add_note'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

