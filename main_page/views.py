from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import redirect
from . import models
from . import forms
from django.contrib.auth.models import User
# Create your views here.


def all_notes(request):
    notes_lst = models.Note.objects.all()
    return render(request,
                  'main.html',
                  {'notes': notes_lst})


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




