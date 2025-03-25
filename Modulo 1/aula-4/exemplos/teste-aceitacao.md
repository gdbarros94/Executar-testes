# Exemplo de Teste de Aceitação: E-commerce

## Feature: Compra de Produtos

### Scenario: Compra bem-sucedida
```gherkin
Feature: Compra de Produtos
  Como um cliente
  Eu quero comprar produtos no e-commerce
  Para receber os itens em casa

  Background:
    Given que existem os seguintes produtos:
      | id | nome     | preco | quantidade |
      | 1  | Notebook | 3500  | 10         |
      | 2  | Mouse    | 50    | 20         |

  Scenario: Compra bem-sucedida
    Given que estou na página inicial
    When eu adiciono "Notebook" ao carrinho
    And eu adiciono "Mouse" ao carrinho
    And eu insiro o código de desconto "DESCONTO10"
    And eu finalizo a compra com o cartão "4111111111111111"
    Then eu devo ver a mensagem "Compra realizada com sucesso!"
    And o pedido deve ser registrado
    And o estoque deve ser atualizado
    And eu devo receber um email de confirmação
```

### Scenario: Falha na compra por estoque insuficiente
```gherkin
  Scenario: Falha na compra por estoque insuficiente
    Given que estou na página inicial
    When eu adiciono "Notebook" ao carrinho
    And eu adiciono "Notebook" ao carrinho
    And eu adiciono "Notebook" ao carrinho
    And eu adiciono "Notebook" ao carrinho
    And eu adiciono "Notebook" ao carrinho
    And eu adiciono "Notebook" ao carrinho
    And eu finalizo a compra com o cartão "4111111111111111"
    Then eu devo ver a mensagem "Estoque insuficiente"
    And o pedido não deve ser registrado
    And o estoque não deve ser alterado
```

## Feature: Gestão de Estoque

### Scenario: Atualização de estoque
```gherkin
Feature: Gestão de Estoque
  Como um administrador
  Eu quero gerenciar o estoque de produtos
  Para manter o controle do inventário

  Background:
    Given que estou logado como administrador
    And que existem os seguintes produtos:
      | id | nome     | preco | quantidade |
      | 1  | Notebook | 3500  | 10         |

  Scenario: Adicionar produtos ao estoque
    Given que estou na página de gestão de estoque
    When eu adiciono 5 unidades ao produto "Notebook"
    Then o estoque de "Notebook" deve ser 15
    And o sistema deve registrar a operação
    And eu devo ver a mensagem "Estoque atualizado com sucesso"

  Scenario: Remover produtos do estoque
    Given que estou na página de gestão de estoque
    When eu removo 3 unidades do produto "Notebook"
    Then o estoque de "Notebook" deve ser 7
    And o sistema deve registrar a operação
    And eu devo ver a mensagem "Estoque atualizado com sucesso"
```

## Feature: Aplicação de Descontos

### Scenario: Aplicar desconto válido
```gherkin
Feature: Aplicação de Descontos
  Como um cliente
  Eu quero aplicar descontos nas compras
  Para economizar dinheiro

  Background:
    Given que estou na página do carrinho
    And que tenho os seguintes produtos no carrinho:
      | produto  | quantidade | preco |
      | Notebook | 1          | 3500  |
      | Mouse    | 2          | 50    |

  Scenario: Aplicar desconto válido
    When eu insiro o código de desconto "DESCONTO10"
    Then o desconto de 10% deve ser aplicado
    And o total deve ser 3240
    And eu devo ver a mensagem "Desconto aplicado com sucesso!"

  Scenario: Tentar aplicar desconto inválido
    When eu insiro o código de desconto "INVALIDO"
    Then o desconto não deve ser aplicado
    And o total deve permanecer 3600
    And eu devo ver a mensagem "Código de desconto inválido"
```

## Feature: Consulta de Pedidos

### Scenario: Consultar pedido existente
```gherkin
Feature: Consulta de Pedidos
  Como um cliente
  Eu quero consultar meus pedidos
  Para acompanhar minhas compras

  Background:
    Given que estou logado como cliente
    And que tenho um pedido realizado:
      | id | data       | status   | total |
      | 1  | 2024-03-20 | aprovado | 3500  |

  Scenario: Consultar pedido existente
    When eu acesso a página de meus pedidos
    And eu clico no pedido "1"
    Then eu devo ver os detalhes do pedido:
      | campo  | valor  |
      | status | aprovado |
      | total  | 3500    |
      | data   | 2024-03-20 |
    And eu devo ver os produtos do pedido:
      | produto  | quantidade | preco |
      | Notebook | 1          | 3500  |

  Scenario: Consultar pedido inexistente
    When eu acesso a página de meus pedidos
    And eu tento acessar o pedido "999"
    Then eu devo ver a mensagem "Pedido não encontrado"
```

## Feature: Validações de Segurança

### Scenario: Tentativa de acesso não autorizado
```gherkin
Feature: Validações de Segurança
  Como um sistema
  Eu quero garantir a segurança das operações
  Para proteger dados sensíveis

  Background:
    Given que não estou logado

  Scenario: Tentativa de acesso não autorizado
    When eu tento acessar a página de gestão de estoque
    Then eu devo ser redirecionado para a página de login
    And eu devo ver a mensagem "Acesso não autorizado"

  Scenario: Tentativa de manipulação de preço
    Given que estou logado como cliente
    When eu tento modificar o preço de um produto
    Then a modificação não deve ser permitida
    And eu devo ver a mensagem "Operação não permitida"
``` 