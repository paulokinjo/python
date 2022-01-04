from lists.models import Item
from django.urls import resolve
from django.test import TestCase, Client
from django.http import HttpRequest, request, response
from django.template.loader import render_to_string
from django.template import RequestContext

from lists.views import home_page


homePageUrl = '/'


class HomePageTest(TestCase):

    def setUp(self):
        self.client_stub = Client()

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve(homePageUrl)
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get(homePageUrl)
        print(response.content)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        message = 'A new list item'
        
        self.client_stub.post(homePageUrl,
                                         {'item_text': message})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, message)

    def test_home_page_redirects_after_POST(self):
        message = 'A new list item'
        response = self.client_stub.post(homePageUrl,
                                         {'item_text': message})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.get('location', ''), '/')

    def test_home_page_only_saves_items_when_necessary(self):
        self.client_stub.get(homePageUrl)
        self.assertEqual(Item.objects.count(), 0)
        
    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response = self.client_stub.get(homePageUrl)
        
        responseContentDecoded = response.content.decode()
        
        self.assertIn('itemey 1', responseContentDecoded)
        self.assertIn('itemey 2', responseContentDecoded)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
