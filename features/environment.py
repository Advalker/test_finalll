from selenium import webdriver

def before_all(context):
    # Configurar as opções do Chrome
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--disable-site-isolation-trials')
    options_chrome.add_argument('--ignore-certificate-errors')
    options_chrome.add_argument('--start-maximized')

    # Iniciar o navegador com as opções configuradas
    context.browser = webdriver.Chrome(options=options_chrome)

def after_all(context):
    # Fechar o navegador
    context.browser.quit()
