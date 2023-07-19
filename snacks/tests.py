from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse
# Create your tests here.
    

class SnackTest(TestCase):

    def test_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_list.html')
    
    def test_detail_view(self):
        url = reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_detail.html')

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random',email='random@random.com',
            password='random@12345'
        )
        self.snack = Snack.objects.create(
            name='test',
            purchaser=self.user,
            description ='ddddd'
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')
    
    def test_name_field(self):
        self.assertEqual(str(self.snack.name),'test')
    
    def test_purchaser_field(self):
        self.assertEqual(str(self.snack.purchaser),'random')
    
    def test_description_field(self):
        self.assertEqual(str(self.snack.description),'ddddd')

    def test_create_view(self):
        url = reverse('snack_create')
        data={
            "name":"test",
            "purchaser":self.user.id,
            "description":"test"
        }
        response = self.client.post(url,data=data,follow=True)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response,reverse('snack_detail',args=[2]))
    
    def test_update_view(self):
        url = reverse('snack_update',args=[1])
        data={
            "name":"test",
            "purchaser":self.user.id,
            "description":"test"
        }
        response = self.client.post(url,data=data,follow=True)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()),1)
        self.assertRedirects(response,reverse('snack_detail',args=[1]))
    
    def test_delete_view(self):
        url = reverse('snack_delete',args=[1])
        response = self.client.post(url,follow=True)
        self.assertTemplateUsed(response,'snack_list.html')
        self.assertEqual(len(Snack.objects.all()),0)
        self.assertRedirects(response,reverse('snack_list'))
    

