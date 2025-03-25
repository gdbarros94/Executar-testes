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
```javascript
// calculadora.js
function somar(a, b) {
    return a + b;
}

// calculadora.test.js
test('somar deve retornar a soma dos números', () => {
    expect(somar(2, 3)).toBe(5);
});
```

### 3. Testes de Integração

#### Características
- Testam múltiplos componentes
- Mais complexos
- Podem depender de ambiente
- Mais lentos

#### Exemplo Prático
```javascript
// sistema-login.js
class SistemaLogin {
    constructor(bancoDados) {
        this.bancoDados = bancoDados;
    }

    login(email, senha) {
        const usuario = this.bancoDados.buscarUsuario(email);
        return usuario && usuario.senha === senha;
    }
}

// sistema-login.test.js
test('login deve funcionar com banco de dados', () => {
    const mockDB = {
        buscarUsuario: (email) => ({
            email,
            senha: '123'
        })
    };
    const sistema = new SistemaLogin(mockDB);
    expect(sistema.login('teste@email.com', '123')).toBe(true);
});
```

## 🎮 Atividade Prática

### Exercício 1: Testes Unitários
1. Acesse o arquivo `exercicios/calculadora.js`
2. Crie testes unitários para todas as funções
3. Execute os testes
4. Documente os resultados

### Exercício 2: Testes de Integração
1. Acesse o arquivo `exercicios/sistema-pagamento.js`
2. Crie testes de integração
3. Use mocks para simular dependências
4. Documente os resultados

## 📝 Material Complementar

### Exemplos
- [Exemplo de Teste Unitário](exemplos/teste-unitario.md)
- [Exemplo de Teste de Integração](exemplos/teste-integracao.md)
- [Exemplo de Mock](exemplos/mock-exemplo.md)

### Próxima Aula
- Testes de sistema
- Testes de aceitação
- Prática final 