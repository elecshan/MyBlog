from django.test import TestCase, Client

# Create your tests here.

class blogTest(TestCase):
    def test(self):
        c = Client()
        response = c.get('/BlogApp')
        print('well')