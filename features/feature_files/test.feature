Feature: Login na página da Linkedin
  Como um usuário
  Eu quero fazer login na página da Udemy
  Para que eu possa acessar minha conta
  @TestLogin
  Scenario: Login com sucesso
    Given que estou na página de login
    When eu insiro o email e senha corretos
    And clico no botão de login
    Then eu devo ser redirecionado para a página inicial
  
  @TestErroLogin 
  Scenario: Login com email invalido
    Given que o usuário está na página de login
    When Quando ele insere um email inválido 
    And clica no botão login
    Then Então uma mensagem de erro informando que o email é inválido é exibida