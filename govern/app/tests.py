# from django.test import TestCase,SimpleTestCase, Client
# from django.urls import reverse

# Create your tests here.

# class TestViews(SimpleTestCase):
#     def test_home(self):
#         client = Client()
#         response = client.get(reverse('home'))
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response, 'about.html')


from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# options = Options()
# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get('http://127.0.0.1:8000/login/')

class TestHome(LiveServerTestCase):
    def testhomepage(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/login/')
        driver.find_element(By.NAME,"username").send_keys('suman')
        driver.find_element(By.NAME,"password").send_keys('gautam')
        driver.find_element(By.XPATH,"//butto").click()
        time.sleep(5)


