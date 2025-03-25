# Aula 4: Níveis de Teste - Parte 2

## 🎯 Objetivos da Aula
- Compreender testes de sistema
- Compreender testes de aceitação
- Praticar escrita de casos de teste de aceitação
- Realizar prática final do módulo

## 📚 Conteúdo

### 1. Testes de Sistema

#### Características
- Testam o sistema completo
- Ambiente real ou similar
- Foco em fluxos de negócio
- Testam interfaces externas

#### Exemplo Prático
```javascript
// sistema-pagamento.test.js
describe('Sistema de Pagamento', () => {
    test('processar pagamento deve atualizar saldo', async () => {
        const sistema = new SistemaPagamento();
        const resultado = await sistema.processarPagamento({
            valor: 100,
            cartao: '4111111111111111'
        });
        expect(resultado.status).toBe('aprovado');
        expect(resultado.saldo).toBe(900);
    });
});
```

### 2. Testes de Aceitação

#### Características
- Baseados em requisitos do usuário
- Escritos em linguagem natural
- Foco em comportamento esperado
- Usam BDD (Behavior Driven Development)

#### Exemplo Prático
```gherkin
Feature: Login de Usuário
  Como um usuário cadastrado
  Eu quero fazer login no sistema
  Para acessar minha conta

  Scenario: Login com credenciais válidas
    Given que estou na página de login
    When eu insiro meu email "teste@email.com"
    And eu insiro minha senha "123456"
    And eu clico no botão "Entrar"
    Then eu devo ser redirecionado para o dashboard
    And eu devo ver a mensagem "Bem-vindo!"
```

### 3. Prática Final

#### Objetivo
Criar um conjunto completo de testes para um sistema de e-commerce simples, incluindo:
- Testes unitários
- Testes de integração
- Testes de sistema
- Testes de aceitação

## 🎮 Atividade Prática

### Exercício 1: Testes de Sistema
1. Acesse o arquivo `exercicios/ecommerce.js`
2. Crie testes de sistema para:
   - Fluxo de compra
   - Processamento de pagamento
   - Atualização de estoque
3. Documente os resultados

### Exercício 2: Testes de Aceitação
1. Crie cenários de teste usando Gherkin
2. Implemente os testes usando Cucumber
3. Execute os testes
4. Documente os resultados

## 📝 Material Complementar

### Exemplos
- [Exemplo de Teste de Sistema](exemplos/teste-sistema.md)
- [Exemplo de Teste de Aceitação](exemplos/teste-aceitacao.md)
- [Exemplo de BDD](exemplos/bdd-exemplo.md)

### Próxima Aula
- Revisão do módulo
- Avaliação prática
- Introdução ao próximo módulo 