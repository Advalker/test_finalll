import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    URL = 'https://www.udemy.com/join/login-popup/'
    
    def __init__(self, browser: webdriver):
        self.browser = browser

    def open(self):
        # Abre a página de login
        self.browser.get(self.URL)

    def enter_username(self, username):
        # Localiza o campo de email pelo ID usando By e insere o valor fornecido
        username_field = self.browser.find_element(By.ID, 'form-group--1')
        username_field.clear()  # Limpa qualquer valor existente
        username_field.send_keys(username)
        time.sleep(3)

    def enter_password(self, password):
        # Localiza o campo de senha pelo ID usando By e insere o valor fornecido
        password_field = self.browser.find_element(By.ID, 'form-group--3')
        password_field.clear()  # Limpa qualquer valor existente
        password_field.send_keys(password)
        time.sleep(3)
    def click_login_button(self):
        # Localiza o botão de login pelo ID usando By e clica nele
        login_button = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/nav/button/span")
        login_button.click()
        time.sleep(10)

    def is_redirected_to_home(self):
        # Verifica se foi redirecionado para a página inicial
        return 'home' in self.browser.current_url

    def is_username_displayed(self, username):
        # Verifica se o nome de usuário está visível na página após o login
        user_display = self.browser.find_element(By.ID, 'username_display')
        return username in user_display.text
