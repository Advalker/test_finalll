from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()  # Ou use o driver do seu navegador

def after_all(context):
    context.browser.quit()
