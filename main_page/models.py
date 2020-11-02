from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Note(models.Model):

    title = models.CharField(max_length=250, blank=True, default='Note')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    publish = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_note')

    access = models.ManyToManyField(User,
                                    related_name='access',
                                    default=author)
    def __str__(self):
        return self.slug

class MyUser(User):
    def get_absolute_url(self):
        return reverse('main_page:all_notes',
                       args=[self.username])