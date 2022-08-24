import re
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class snacksTests(SimpleTestCase):

  def test_homepage_status(self):
    #Navigate to the home page an return the status code
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_aboutpage_status(self):
    #Navigate to the home page an return the status code
    url = reverse('about')
    response = self.client.get(url)
    print(response)
    self.assertEqual(response.status_code, 200)
  
  #Test url templpare use
  def test_homeUrl_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')

  def test_aboutUrl_template(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')

