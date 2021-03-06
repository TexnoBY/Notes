from string import punctuation

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView

from . import forms
from . import models


# Create your views here.



class NoteListView(LoginRequiredMixin, ListView):
    queryset = models.Note.objects.all()
    context_object_name = 'notes'
    template_name = 'main.html'


def all_notes(request, username):
    if request.user.username == username:
        all_notes = models.Note.objects.filter(author__in=request.user.profile.friends.all())
    else:
        user = get_object_or_404(User, username=username)
        if request.user in request.user.profile.friends.all():
            all_notes = models.Note.objects.filter(author=user)
        else:
            all_notes = None
    return render(request,
                  'main.html',
                  {'notes': all_notes})


def add_note(request):
    if request.method == 'POST':
        note_form = forms.NoteForm(request.POST)
        if note_form.is_valid():
            new_note = note_form.save(commit=False)
            new_note.author = request.user
            slug = new_note.title + new_note.body
            new_note.slug = ''.join('_' if char in ' \n\r' else char for char in slug if char not in punctuation)

            new_note.save()
            return redirect('main_page:to_main_or_login')
    else:

        note_form = forms.NoteForm()
    return render(request,
                  'add_new_note.html',
                  {'form': note_form})


def delete_note(request, note_id):
    models.Note.objects.filter(id=note_id).delete()
    return redirect('main_page:to_main_or_login')


def redirect_to_main_or_login(request):
    if request.user.is_authenticated:
        return redirect('main_page:all_notes',
                        request.user.username)
    else:
        return redirect('login')


def edit_note(request, year, month, day, slug, id):
    note = get_object_or_404(models.Note,
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             id=id)
    if request.method == "POST":
        note_form = forms.NoteForm(data=request.POST,
                                   instance=note)
        if note_form.is_valid():
            edit_note = note_form.save(commit=False)
            slug = edit_note.title + edit_note.body
            edit_note.slug = ''.join('_' if char in ' \n\r' else char for char in slug if char not in punctuation)
            edit_note.save()
            return redirect('main_page:to_main_or_login')
    else:
        note_form = forms.NoteForm(instance=note)
    return render(request,
                  'edit_note.html',
                  {'note_form': note_form})


def create_user(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(data=request.POST,
                                       instance=request.user)
        profile_form = forms.ProfileEditForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_profile_form = profile_form.save(commit=False)
            new_profile_form.user = request.user
            user_form.save()
            # profile_form.save()
            new_profile_form.save()
            return redirect('main_page:to_main_or_login')
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm()
    return render(request,
                  'edit_profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def edit_user(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(data=request.POST,
                                       instance=request.user)
        profile_form = forms.ProfileEditForm(data=request.POST,
                                             instance=request.user.profile,
                                             files=request.FILES)
        user_form.save()
        profile_form.save()
        return render(request,
                      'profile.html',
                      {'user': request.user})
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'edit_profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def view_profile(request, username='', id=0):
    if username and id:
        user = get_object_or_404(User,
                                 username=username,
                                 id=id)
    else:
        user = request.user

    return render(request, 'profile.html', {'user': user})



