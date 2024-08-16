from behave import given, when, then
from pages.test_pages import LoginPage

@given(u'que estou na página de login')
def step_impl(context):
    context.page = LoginPage(context.browser)
    context.page.open()

@when('eu insiro o email e senha corretos')
def step_impl(context):
    context.page.enter_username()
    

@when(u'clico no botão de login')
def step_impl(context):
    context.page.click_login_button()

@then(u'eu devo ser redirecionado para a página inicial')
def step_impl(context):
    ...#assert context.page.is_redirected_to_home()


# Revion 

@given(u'que o usuário está na página de login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que o usuário está na página de login')


@when(u'Quando ele insere um email inválido')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Quando ele insere um email inválido')


@when(u'clica no botão login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clica no botão login')


@then(u'Então uma mensagem de erro informando que o email é inválido é exibida')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Então uma mensagem de erro informando que o email é inválido é exibida')