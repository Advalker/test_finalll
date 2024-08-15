from behave import given, when, then
from pages.test_pages import LoginPage

@given('que estou na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()

@when('eu insiro o nome de usuário e senha corretos')
def step_impl(context):
    context.page.enter_username('advalker@hotmail.com')
    context.page.enter_password('@Evolucao#2024')

@when('clico no botão de login')
def step_impl(context):
    context.page.click_login_button()

@then('eu devo ser redirecionado para a página inicial')
def step_impl(context):
    assert context.page.is_redirected_to_home()

@then('eu devo ver meu nome de usuário na página')
def step_impl(context):
    assert context.page.is_username_displayed('meu_usuario')
