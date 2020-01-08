import json
from datetime    import datetime

from .models     import Users
from django.test import TestCase
from django.test import Client

class UserTest(TestCase):
    def setUp(self):
        Users.objects.create(
                name = 'yerin',
                password ='12345'
                )

    def teardown(self):
        Users.objects.get(name='yerin').delete()



