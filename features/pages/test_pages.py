import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.elementos import *

class LoginPage:
    URL = URL_LINKDIN
    
    def __init__(self, browser: webdriver):
        self.browser = browser

    def open(self):
        # Abre a página de login
        self.browser.get(self.URL)

    def enter_login(self):        
        username_field = self.browser.find_element(By.ID, 'username')
        username_field.send_keys(EMAIL_LOGIN) # recebe o email do arquivo em elementos
        time.sleep(2)
        password_field = self.browser.find_element(By.ID, 'password')
        password_field.send_keys(SENHA_LOGIN) # recebe senha do arquivo em elementos
        time.sleep(2)

    def get_text_from_element(self, by, value):
        message_text = self.browser.find_element(By.ID, 'error-for-username')
        return message_text
        
    def email_incorreto(self):        
        username_field = self.browser.find_element(By.ID, 'username')
        username_field.send_keys(EMAIL_ERRADO) # recebe o email do arquivo em elementos
        time.sleep(2)
        

    def click_login_button(self):
        # Localiza o botão de login pelo ID usando By e clica nele
        login_button = self.browser.find_element(By.XPATH, BTN_LOGIN)
        login_button.click()
        time.sleep(10)

   
