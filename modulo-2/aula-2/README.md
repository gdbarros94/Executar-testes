# Aula 2 - Técnicas de Caixa Preta vs Branca

## Objetivos
- Compreender as diferenças entre testes de caixa preta e branca
- Aplicar técnicas de particionamento de equivalência
- Praticar análise de valores limite
- Realizar análise de fluxo de dados

## Conteúdo

### 1. Testes de Caixa Preta
- Testes baseados em especificação
- Particionamento de equivalência
- Análise de valores limite
- Testes de casos de uso

### 2. Testes de Caixa Branca
- Testes baseados em código
- Cobertura de código
- Análise de fluxo de dados
- Testes de caminhos

## Projeto Prático: Sistema de Criptografia

### Estrutura do Projeto
- `criptografia.py`: Implementação do sistema
- `test_criptografia.py`: Testes automatizados
- `requisitos-api.md`: Especificação do sistema

### Atividades

#### 1. Testes de Caixa Preta
- Analisar requisitos da API
- Identificar classes de equivalência
- Definir casos de teste
- Documentar resultados esperados

#### 2. Testes de Caixa Branca
- Analisar código fonte
- Identificar caminhos de execução
- Criar testes unitários
- Medir cobertura de código

## Exercícios

### Exercício 1: Particionamento de Equivalência
- Identificar classes válidas e inválidas
- Criar casos de teste para cada classe
- Documentar critérios de particionamento

### Exercício 2: Análise de Valores Limite
- Identificar limites das funções
- Testar valores nas fronteiras
- Validar comportamento nos limites

### Exercício 3: Análise de Fluxo
- Mapear fluxo de dados
- Identificar dependências
- Criar testes de integração

## Como Executar os Testes

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute os testes com cobertura:
```bash
pytest --cov=criptografia test_criptografia.py
```

## Entrega
- Documentação dos testes realizados
- Casos de teste implementados
- Relatório de cobertura
- Bugs encontrados documentados

## Critérios de Avaliação
- Qualidade dos casos de teste
- Cobertura de código alcançada
- Documentação produzida
- Bugs identificados 