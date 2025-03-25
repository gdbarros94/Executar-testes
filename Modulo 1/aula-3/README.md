# Aula 3: Níveis de Teste - Parte 1

## 🎯 Objetivos da Aula
- Compreender os diferentes níveis de teste
- Identificar quando usar cada nível
- Praticar testes unitários
- Praticar testes de integração

## 📚 Conteúdo

### 1. Pirâmide de Testes

#### Níveis (de baixo para cima)
1. **Testes Unitários**
   - Testam componentes isolados
   - Mais rápidos e baratos
   - Maior cobertura

2. **Testes de Integração**
   - Testam interação entre componentes
   - Mais lentos que unitários
   - Menor cobertura

3. **Testes de Sistema**
   - Testam o sistema completo
   - Mais lentos e caros
   - Menor cobertura ainda

4. **Testes de Aceitação**
   - Testam requisitos do usuário
   - Mais lentos e caros
   - Menor cobertura

### 2. Testes Unitários

#### Características
- Isolados
- Rápidos
- Determinísticos
- Independentes

#### Exemplo Prático
```python
# calculadora.py
def somar(a, b):
    return a + b

# test_calculadora.py
def test_somar():
    assert somar(2, 3) == 5
```

### 3. Testes de Integração

#### Características
- Testam múltiplos componentes
- Mais complexos
- Podem depender de ambiente
- Mais lentos

#### Exemplo Prático
```python
# sistema_login.py
class SistemaLogin:
    def __init__(self, banco_dados):
        self.banco_dados = banco_dados

    def login(self, email, senha):
        usuario = self.banco_dados.buscar_usuario(email)
        return usuario and usuario['senha'] == senha

# test_sistema_login.py
def test_login_com_banco_dados():
    mock_db = {
        'buscar_usuario': lambda email: {
            'email': email,
            'senha': '123'
        }
    }
    sistema = SistemaLogin(mock_db)
    assert sistema.login('teste@email.com', '123') is True
```

## 🎮 Atividade Prática

### Exercício 1: Testes Unitários
1. Acesse o arquivo `exercicios/calculadora.py`
2. Crie testes unitários para todas as funções
3. Execute os testes
4. Documente os resultados

### Exercício 2: Testes de Integração
1. Acesse o arquivo `exercicios/sistema_pagamento.py`
2. Crie testes de integração
3. Use mocks para simular dependências
4. Documente os resultados

## 📝 Material Complementar

### Exemplos
- [Exemplo de Teste Unitário](exemplos/teste_unitario.md)
- [Exemplo de Teste de Integração](exemplos/teste_integracao.md)
- [Exemplo de Mock](exemplos/mock_exemplo.md)

### Próxima Aula
- Testes de sistema
- Testes de aceitação
- Prática final 