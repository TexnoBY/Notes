from django import forms
from django.contrib.auth.models import User

from . import models


class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ('title', 'body')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('friends',)
