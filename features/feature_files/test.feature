Feature: Login na página da Udemy
  Como um usuário
  Eu quero fazer login na página da Udemy
  Para que eu possa acessar minha conta

  Scenario: Login com sucesso
    Given que estou na página de login
    When eu insiro o nome de usuário e senha corretos
    And clico no botão de login
    Then eu devo ser redirecionado para a página inicial
    And eu devo ver meu nome de usuário na página
