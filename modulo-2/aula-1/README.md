# Aula 1 - Tipos de Teste na Prática

## Objetivos
- Compreender diferentes tipos de teste
- Praticar testes em um sistema de e-commerce
- Documentar e reportar bugs encontrados

## Conteúdo

### 1. Testes Funcionais
- Verificação de funcionalidades básicas
- Fluxos principais de negócio
- Casos de teste positivos e negativos

### 2. Testes de Regressão
- Garantia de funcionalidades existentes
- Impacto de novas alterações
- Automação de testes recorrentes

### 3. Testes de Desempenho
- Análise de tempo de resposta
- Comportamento sob carga
- Limites do sistema

## Projeto Prático: E-commerce

### Estrutura do Projeto
- `carrinho.py`: Sistema de carrinho de compras
- `produtos.py`: Gerenciamento de produtos

### Atividades
1. Identificar bugs no sistema de carrinho
2. Criar casos de teste documentados
3. Executar testes manuais e registrar resultados

## Exercícios

### Exercício 1: Testes Funcionais
- Testar cadastro de produtos
- Validar cálculo do carrinho
- Verificar aplicação de descontos

### Exercício 2: Testes de Regressão
- Documentar cenários principais
- Criar lista de verificação
- Executar suite de testes

### Exercício 3: Testes de Desempenho
- Testar com grande volume de produtos
- Analisar tempo de resposta
- Documentar resultados

## Como Executar os Testes

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute os testes:
```bash
pytest exercicios/test_carrinho.py
pytest exercicios/test_produtos.py
```

## Entrega
- Documentação dos testes realizados
- Registro de bugs encontrados
- Relatório de execução dos testes 