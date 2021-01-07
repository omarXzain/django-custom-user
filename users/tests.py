from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import CustomUser
from django.urls import reverse, reverse_lazy
# Create your tests here.

class TestLoginView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='omar',
                email='omar@gmail.com',
                password='11223344'
        )
    def test__status(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                username='omar',
                email='omar@gmail.com',
                password='11223344'
                    )
        except:
            self.user2 = None
        self.assertEqual(self.user2,None)
    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code , 200)

    def test_signup(self):
        response = self.client.post('/customer/signup/', data={
            
            'email address': 'omar@gmail.com',
            'password': '11223344',
        })
        self.assertEqual(response.status_code, 404)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
        

