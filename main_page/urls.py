from django.urls import path
from django.shortcuts import redirect
from django.urls import include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'main_page'


# class MyHack(auth_views.PasswordResetView):
#     success_url = reverse_lazy('main_page:password_reset_done')

urlpatterns = [
    path('', views.redirect_to_main_or_login, name='to_main_or_login'),
    # path('user/<str:username>/', views.NoteListView.as_view(), name='all_notes'),
    path('user/<str:username>/', views.all_notes, name='all_notes'),
    path('<int:note_id>/', views.delete_note, name='delete_note'),
    path('add/', views.add_note, name='add_note'),

    # path('password_reset/', MyHack.as_view(), name='password_reset'),
]

