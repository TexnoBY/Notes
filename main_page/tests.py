from django.test import TestCase, Client
from main_page import models
from string import punctuation

import ddt
from unittest import mock


# Create your tests here.

@ddt.ddt
class NoteTestCase(TestCase):

    def setUp(self):
        super(NoteTestCase, self).setUp()
        self.user = models.User(username='Test',
                                first_name='te',
                                last_name='st',
                                email='gg@ggg.com',)
        self.user.save()
        self.client = Client()

    def test_note_created_return_200(self):
        response = self.client.post(
            '/add/',
            {'title': 'note          ' + punctuation + '  asdas dasdas  ',
             'body': 'testbody' + punctuation + 'bbasdfdas sadfdasfa   ',
             'author': self.user,},
        )
        self.assertEqual(response.status_code, 200)

    def test_add_one_note(self):
        self.client.post(
            '/add/',
            {'title': 'note          ' + punctuation + '  asdas dasdas  ',
             'body': 'testbody' + punctuation + 'bbasdfdas sadfdasfa   ',
             'author': self.user},
        )
        models.Note.objects.get()

    @ddt.data(('    note   ' + punctuation, punctuation + '   body    '),
              ('note   badsaf' + punctuation, punctuation + 'bbbb   body'))
    @ddt.unpack
    def test_slug_created(self, title, body):
        self.client.post(
            '/add/',
            {'title': title,
             'body': body,
             'author': self.user,},
        )
        note = models.Note.objects.get()
        self.assertEqual(note.slug, title)

    @ddt.data(
        ('sl ug1', 'sl-ug1testbody'),
        ('s lug 1', 's-lug-1testbody'),
        ('s   lug1', 's---lug1testbody'),
    )
    @ddt.unpack
    def test_slug_created_correctly(self, title, expected_slug):
        """Test slug created correctly. Title: "{}". Expected slug: "{}"."""
        self.client.post(
            '/add/',
            {'title': title,
             'body': 'testbody',
             'author': self.user,},
        )
        note = models.Note.objects.get()
        self.assertEqual(note.slug, expected_slug)
