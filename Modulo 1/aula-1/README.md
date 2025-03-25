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
```python
# Exemplo de código sem testes
def calcular_desconto(valor, desconto):
    return valor - desconto
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
```python
# calculadora.py
def somar(a, b):
    return a + b

# test_calculadora.py
def test_somar():
    assert somar(2, 3) == 5
```

## 🎮 Atividade Prática

### Exercício 1: Identificando Bugs
1. Abra o arquivo `exercicios/calculadora_bugada.py`
2. Identifique os bugs
3. Crie um caso de teste que falha
4. Abra uma issue no GitHub descrevendo o problema

### Exercício 2: Primeiro Teste
1. Crie um arquivo de teste para a função `calcular_desconto`
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