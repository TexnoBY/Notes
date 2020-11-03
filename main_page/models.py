from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


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

    def get_absolute_url(self):
        return reverse('main_page:edit_note',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        return self.slug


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    friends = models.ManyToManyField(User,
                                     related_name='friends')

