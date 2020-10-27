from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from . import forms
from . import models


# Create your views here.


class NoteListView(LoginRequiredMixin, ListView):
    queryset = models.Note.objects.all()
    context_object_name = 'notes'
    template_name = 'main.html'


def add_note(request):
    if request.method == 'POST':
        note_form = forms.NoteForm(request.POST)
        if note_form.is_valid():
            new_note = note_form.save(commit=False)
            new_note.author = User.objects.first()
            new_note.slug = new_note.title.replace(" ", "-") + new_note.body.replace(" ", "-")
            new_note.save()
            return redirect('main_page:all_notes')
    else:
        note_form = forms.NoteForm()
    return render(request,
                  'add_new_note.html',
                  {'form': note_form})


def delete_note(request, note_id):
    models.Note.objects.filter(id=note_id).delete()
    return redirect('main_page:all_notes')




