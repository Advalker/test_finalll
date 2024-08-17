# Projeto de Testes Automatizados com Behave e Selenium

Este projeto implementa testes automatizados para o processo de login, verificação de mensagens de erro e logout no LinkedIn. Os testes são escritos em Python utilizando a biblioteca Behave para BDD (Behavior-Driven Development) e Selenium para automação de navegação na web.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em seu ambiente:

- **Python 3.x**: Linguagem de programação usada para escrever os testes.
- **pip**: Gerenciador de pacotes do Python.
- **Google Chrome**: Navegador usado nos testes.
- **ChromeDriver**: Ferramenta que permite ao Selenium controlar o navegador Chrome.

## Configuração do Ambiente

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências do Python:**

   Execute o comando abaixo para instalar as bibliotecas necessárias listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Caso o arquivo `requirements.txt` não exista, instale as bibliotecas manualmente:

   ```bash
   pip install behave selenium
   ```

3. **Baixe o ChromeDriver:**

   - Baixe a versão compatível com o seu navegador Chrome a partir do [site oficial do ChromeDriver](https://sites.google.com/chromium.org/driver/).
   - Extraia o arquivo e adicione o caminho do executável `chromedriver` ao `PATH` do sistema.

4. **Crie o arquivo `elementos.py`:**

   O arquivo `elementos.py` deve conter os seletores dos elementos HTML usados nos testes. Exemplo:

   ```python
   URL_LINKDIN = "https://www.linkedin.com/login"
   CAMPO_EMAIL = "username"
   CAMPO_SENHA = "password"
   BTN_LOGIN = "//button[@type='submit']"
   IMG_MENU = "//img[@class='profile-rail-card__profile-photo']"
   TXT_CAPTURADO = "//div[@id='error-for-password']"
   ```

5. **Configure suas credenciais:**

   Insira suas credenciais de login e outros dados necessários no arquivo `elementos.py`:

   ```python
   EMAIL = "seu_email@exemplo.com"
   SENHA = "sua_senha"
   EMAIL_ERRADO = "email_errado@exemplo.com"
   ```

## Estrutura do Projeto

- **features/**: Diretório que contém os arquivos `.feature` onde os cenários de teste são descritos.
- **pages/**: Diretório que contém as classes de página (`LoginPage`) com os métodos que realizam ações específicas nos elementos HTML.
- **features/steps/**: Diretório que contém os arquivos `.py` que implementam os passos definidos nos arquivos `.feature`.
- **features/elementos.py**: Arquivo que contém todos os seletores de elementos HTML e variáveis de configuração usadas nos testes.

## Executando os Testes

Para executar os testes, utilize o comando:

```bash
behave --tags="@TestLogin"
```
