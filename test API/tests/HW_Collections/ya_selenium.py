import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from AD.AD_HW6.tests.data_ya import email, password
class YaAuthTest():
    def __init__(self, login, password, driver):
        self.login = login
        self.password = password
        self.driver = driver

    def put_email(self):
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'AuthLoginInputToggle-type').click()
        time.sleep(1)
        self.driver.find_element(By.ID, 'passp-field-login').send_keys(self.login)
    def put_button(self):
        time.sleep(1)
        self.driver.find_element(By.ID, 'passp:sign-in').click()
    def put_password(self):
        time.sleep(1)
        self.driver.find_element(By.ID, 'passp-field-passwd').send_keys(self.password)



if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.get('https://passport.yandex.ru/auth')
    ya = YaAuthTest(email, password, driver)

    ya.put_email()
    ya.put_button()
    ya.put_password()
    ya.put_button()


    time.sleep(10)
    driver.close()