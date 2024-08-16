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

    def enter_username(self):        
        username_field = self.browser.find_element(By.ID, 'username')
        username_field.send_keys(EMAIL_LOGIN) # recebe o email do arquivo em elementos
        time.sleep(2)
        password_field = self.browser.find_element(By.ID, 'password')
        password_field.send_keys(SENHA_LOGIN) # recebe senha do arquivo em elementos
        time.sleep(2)

    
    def click_login_button(self):
        # Localiza o botão de login pelo ID usando By e clica nele
        login_button = self.browser.find_element(By.XPATH, BTN_LOGIN)
        login_button.click()
        time.sleep(10)

    def is_redirected_to_home(self):
        # Verifica se foi redirecionado para a página inicial
        return 'home' in self.browser.current_url

    def is_username_displayed(self, username):
        # Verifica se o nome de usuário está visível na página após o login
        user_display = self.browser.find_element(By.ID, 'username_display')
        return username in user_display.text
