from behave import given, when, then
from pages.test_pages import LoginPage
from features.elementos import *

@given(u'que estou na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()

@when('eu insiro o email e senha corretos')
def step_impl(context):
    context.page.enter_login()
    

@when(u'clico no botão de login')
def step_impl(context):
    context.page.click_login_button()

@then(u'eu devo ser redirecionado para a página inicial')
def step_impl(context):
    ...#assert context.page.is_redirected_to_home()


# Revion 
#TestErroLogin
@given(u'que o usuário está na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()


@when(u'Quando ele insere um email inválido')
def step_impl(context):
    context.page.email_incorreto()


@when(u'clica no botão login')
def step_impl(context):
    context.page.click_login_button()


@then(u'Então uma mensagem de erro informando que o email é inválido é exibida')
def step_impl(context):
    ...



# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from features.pages.login_page import LoginPage

# @given(u'que o usuário está na página de login')
# def step_impl(context):
#     context.browser = webdriver.Chrome()
#     context.login_page = LoginPage(context.browser)
#     context.login_page.open()

# @when(u'Quando ele insere um email inválido')
# def step_impl(context):
#     context.login_page.enter_login()  # Certifique-se de que EMAIL_LOGIN é um email inválido

# @when(u'clica no botão login')
# def step_impl(context):
#     context.login_page.click_login_button()

# @then(u'Então uma mensagem de erro informando que o email é inválido é exibida')
# def step_impl(context):
#     error_message = context.login_page.get_text_from_element(By.ID, 'error_message')  # Use o ID correto para o elemento de mensagem de erro
#     assert "email é inválido" in error_message, f"Esperava 'email é inválido', mas recebeu: {error_message}"
#     context.browser.quit()
   