from django.urls import path
from django.shortcuts import redirect
from django.urls import include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main_page'


# class MyHack(auth_views.PasswordResetView):
#     success_url = reverse_lazy('main_page:password_reset_done')

urlpatterns = [
    path('', views.redirect_to_main_or_login, name='to_main_or_login'),
    # path('user/<str:username>/', views.NoteListView.as_view(), name='all_notes'),
    path('user/<str:username>/', views.all_notes, name='all_notes'),
    path('<int:note_id>/', views.delete_note, name='delete_note'),
    path('add/', views.add_note, name='add_note'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('create_user/', views.create_user, name='create_user'),
    path('profile/', views.view_profile, name='profile'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
          views.edit_note,
          name='edit_note'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
