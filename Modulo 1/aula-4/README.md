# Aula 4: Níveis de Teste - Parte 2

## 🎯 Objetivos da Aula
- Compreender testes de sistema
- Compreender testes de aceitação
- Praticar testes end-to-end
- Praticar testes de regressão

## 📚 Conteúdo

### 1. Testes de Sistema

#### Características
- Testam o sistema completo
- Mais lentos e caros
- Podem depender de ambiente
- Menor cobertura

#### Exemplo Prático
```python
# sistema_ecommerce.py
class SistemaEcommerce:
    def __init__(self, banco_dados, gateway_pagamento):
        self.banco_dados = banco_dados
        self.gateway_pagamento = gateway_pagamento

    def processar_pedido(self, pedido):
        # Verifica estoque
        if not self.banco_dados.verificar_estoque(pedido['produto_id']):
            return {'sucesso': False, 'erro': 'Produto sem estoque'}
        
        # Processa pagamento
        pagamento = self.gateway_pagamento.processar_pagamento(pedido['valor'])
        if not pagamento['sucesso']:
            return {'sucesso': False, 'erro': 'Falha no pagamento'}
        
        # Atualiza estoque
        self.banco_dados.atualizar_estoque(pedido['produto_id'])
        
        return {'sucesso': True, 'pedido_id': pagamento['id']}

# test_sistema_ecommerce.py
def test_processar_pedido_completo():
    mock_db = {
        'verificar_estoque': lambda _: True,
        'atualizar_estoque': lambda _: None
    }
    mock_gateway = {
        'processar_pagamento': lambda valor: {
            'sucesso': True,
            'id': '123'
        }
    }
    
    sistema = SistemaEcommerce(mock_db, mock_gateway)
    resultado = sistema.processar_pedido({
        'produto_id': '1',
        'valor': 100.0
    })
    
    assert resultado['sucesso'] is True
    assert 'pedido_id' in resultado
```

### 2. Testes de Aceitação

#### Características
- Testam requisitos do usuário
- Mais lentos e caros
- Podem depender de ambiente
- Menor cobertura

#### Exemplo Prático
```python
# test_aceitacao.py
from playwright.sync_api import sync_playwright

def test_fluxo_completo_compra():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Acessa a página inicial
        page.goto('http://localhost:3000')
        
        # Adiciona produto ao carrinho
        page.click('#produto-1')
        page.click('#adicionar-carrinho')
        
        # Vai para o carrinho
        page.click('#carrinho')
        
        # Verifica se produto está no carrinho
        assert page.text_content('#produto-1') == 'Produto 1'
        
        # Finaliza compra
        page.click('#finalizar-compra')
        
        # Preenche formulário
        page.fill('#nome', 'Teste')
        page.fill('#email', 'teste@email.com')
        page.fill('#cartao', '4111111111111111')
        
        # Confirma compra
        page.click('#confirmar')
        
        # Verifica sucesso
        assert page.text_content('#mensagem') == 'Compra realizada com sucesso!'
        
        browser.close()
```

## 🎮 Atividade Prática

### Exercício 1: Testes de Sistema
1. Acesse o arquivo `exercicios/sistema_vendas.py`
2. Crie testes de sistema
3. Use mocks para simular dependências
4. Documente os resultados

### Exercício 2: Testes de Aceitação
1. Acesse o arquivo `exercicios/test_aceitacao.py`
2. Crie testes de aceitação
3. Use Playwright para automação
4. Documente os resultados

## 📝 Material Complementar

### Exemplos
- [Exemplo de Teste de Sistema](exemplos/teste_sistema.md)
- [Exemplo de Teste de Aceitação](exemplos/teste_aceitacao.md)
- [Exemplo de Teste de Regressão](exemplos/teste_regressao.md)

### Próxima Aula
- Revisão do módulo
- Projeto final
- Avaliação 