# Aula 3 - Estratégias Preventivas e Reativas

## Objetivos
- Compreender diferentes estratégias de teste
- Praticar TDD (Test-Driven Development)
- Implementar testes de integração
- Criar documentação efetiva de testes

## Conteúdo

### 1. Test-Driven Development (TDD)
- Ciclo Red-Green-Refactor
- Escrita de testes antes do código
- Refatoração contínua
- Benefícios e desafios

### 2. Testes de Integração
- Integração entre componentes
- Testes de API
- Testes de banco de dados
- Mocks e stubs

### 3. Documentação de Testes
- Planos de teste
- Casos de teste
- Relatórios de execução
- Rastreamento de bugs

## Projeto Prático: Sistema de Pagamentos

### Estrutura do Projeto
- `processador.py`: Sistema de processamento de pagamentos
- `test_processador.py`: Testes automatizados
- `relatorio-teste.md`: Template de relatório

### Atividades

#### 1. Prática de TDD
- Implementar novas funcionalidades usando TDD
- Documentar ciclo de desenvolvimento
- Refatorar código existente
- Manter suite de testes

#### 2. Testes de Integração
- Testar fluxo completo de pagamento
- Validar integração entre módulos
- Testar cenários de erro
- Documentar resultados

## Exercícios

### Exercício 1: TDD na Prática
- Implementar nova funcionalidade de reembolso
- Seguir ciclo Red-Green-Refactor
- Documentar processo
- Apresentar resultados

### Exercício 2: Testes de Integração
- Criar testes para API de pagamentos
- Validar fluxos completos
- Testar cenários de erro
- Documentar casos de teste

### Exercício 3: Documentação
- Criar relatório de testes
- Documentar bugs encontrados
- Propor melhorias
- Apresentar métricas

## Como Executar os Testes

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute os testes:
```bash
pytest test_processador.py -v
```

3. Gere relatório de cobertura:
```bash
pytest --cov=processador test_processador.py --cov-report=html
```

## Entrega
- Código implementado com TDD
- Testes de integração
- Documentação completa
- Relatório de bugs

## Critérios de Avaliação
- Aplicação correta do TDD
- Qualidade dos testes de integração
- Clareza da documentação
- Identificação de problemas 