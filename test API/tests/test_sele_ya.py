import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestCase
from HW_Collections.ya_selenium import YaAuthTest
from data_ya import email, password



class Test(TestCase):
    def test_push(self):
        driver = webdriver.Firefox()
        driver.get('https://passport.yandex.ru/auth')
        ya = YaAuthTest(email, password, driver)

        ya.put_email()
        ya.put_button()
        ya.put_password()
        ya.put_button()
        time.sleep(1)
        self.assertTrue(driver.find_element(By.ID, 'passp-field-phoneCode'))
        driver.close()

