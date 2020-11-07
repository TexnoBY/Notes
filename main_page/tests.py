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
        self.user = models.User.objects.create_user(username='testuser',
                                                    password='yuhjnmgk')
        self.client = Client()
        login = self.client.login(username='testuser', password='yuhjnmgk')


    def test_note_created_return_302(self):
        response = self.client.post(
            '/add/',
            {'title': 'note          ' + punctuation + '  asdas dasdas  ',
             'body': 'testbody' + punctuation + 'bbasdfdas sadfdasfa   '},
        )
        self.assertEqual(response.status_code, 302)

    def test_add_one_note(self):
        self.client.post(
            '/add/',
            {'title': 'note          ' + punctuation + '  asdas dasdas  ',
             'body': 'testbody' + punctuation + 'bbasdfdas sadfdasfa   '},
        )
        models.Note.objects.get()

    @ddt.data(
        ('sl ug1', 'sl_ug1testbody'),
        ('s lug 1', 's_lug_1testbody'),
        ('s   lug1', 's___lug1testbody'),
    )
    @ddt.unpack
    def test_slug_created_correctly(self, title, expected_slug):
        """Test slug created correctly. Title: "{}". Expected slug: "{}"."""
        self.client.post(
            '/add/',
            {'title': title,
             'body': 'testbody',},
        )
        note = models.Note.objects.get()
        self.assertEqual(note.slug, expected_slug)
