from django.shortcuts import render
from . import models
# Create your views here.


def all_notes(request):
    notes_lst = models.Note.objects.all()
    return render(request,
                  'main.html',
                  {'notes': notes_lst})
