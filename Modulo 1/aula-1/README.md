 # Aula 1: Introdução aos Testes de Software

## 🎯 Objetivos da Aula
- Compreender a importância dos testes de software
- Identificar os principais conceitos e terminologias
- Analisar o impacto da falta de testes
- Introduzir o primeiro caso de teste

## 📚 Conteúdo

### 1. Por que Testar Software?

#### Impacto da Falta de Testes
- **Custo de Falhas**: 
  - Correção tardia é mais cara
  - Impacto no negócio
  - Perda de confiança do cliente

#### Exemplo Prático
```javascript
// Exemplo de código sem testes
function calcularDesconto(valor, desconto) {
    return valor - desconto;
}
```

### 2. Conceitos Básicos

#### Terminologia
- **Bug**: Erro no código
- **Defeito**: Problema que pode causar falha
- **Falha**: Manifestação visível de um defeito

#### Tipos de Testes
1. Testes Manuais
2. Testes Automatizados
3. Testes de Regressão

### 3. Primeiro Caso de Teste

#### Exemplo Prático
```javascript
// calculadora.js
function somar(a, b) {
    return a + b;
}

// calculadora.test.js
test('somar 2 + 3 deve retornar 5', () => {
    expect(somar(2, 3)).toBe(5);
});
```

## 🎮 Atividade Prática

### Exercício 1: Identificando Bugs
1. Abra o arquivo `exercicios/calculadora-bugada.js`
2. Identifique os bugs
3. Crie um caso de teste que falha
4. Abra uma issue no GitHub descrevendo o problema

### Exercício 2: Primeiro Teste
1. Crie um arquivo de teste para a função `calcularDesconto`
2. Implemente casos de teste básicos
3. Execute os testes
4. Documente os resultados

## 📝 Material Complementar

### Links Úteis
- [Glossário de Testes](glossario.md)
- [Exemplos de Casos Reais](casos-reais.md)
- [Boas Práticas](boas-praticas.md)

### Próxima Aula
- Terminologia avançada
- Artefatos de teste
- Documentação de testes