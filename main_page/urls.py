from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main_page'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='all_notes'),
    path('add/', views.add_note, name='add_note'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

