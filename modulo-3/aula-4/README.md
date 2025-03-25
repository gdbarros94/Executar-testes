# Aula 4: Qualidade Contínua

## 🎯 Objetivos
- Implementar CI/CD na prática
- Realizar testes de carga
- Configurar monitoramento
- Gerar relatórios automatizados

## 📚 Conteúdo

### 1. CI/CD
- GitHub Actions
- Workflows de teste
- Automação de processos
- Integração contínua

### 2. Testes de Carga
- Configuração do ambiente
- Scripts de teste
- Métricas e KPIs
- Análise de resultados

### 3. Monitoramento
- Configuração do Grafana
- Dashboards
- Alertas
- Métricas de performance

## 🎮 Projeto Prático: E-commerce

### Estrutura do Projeto
- `load-test/`: Testes de carga
  - `checkout_test.py`: Teste de carga do checkout
  - `api_test.py`: Teste de carga da API
- `monitoring/`: Configuração de monitoramento
  - `grafana/`: Dashboards e configurações
  - `prometheus/`: Métricas e alertas
- `ci/`: Configuração de CI/CD
  - `workflows/`: GitHub Actions
  - `config/`: Configurações gerais

### Atividades

#### 1. Configuração de CI/CD
- Criar workflows
- Configurar jobs
- Automatizar testes
- Gerar relatórios

#### 2. Testes de Carga
- Desenvolver scripts
- Configurar cenários
- Executar testes
- Analisar resultados

## 📝 Exercícios

### Exercício 1: CI/CD
1. Configure GitHub Actions
2. Crie workflow de testes
3. Automatize relatórios
4. Valide pipeline

### Exercício 2: Testes de Carga
1. Desenvolva scripts
2. Configure cenários
3. Execute testes
4. Analise resultados

### Exercício 3: Monitoramento
1. Configure Grafana
2. Crie dashboards
3. Configure alertas
4. Documente métricas

## 🛠️ Como Executar

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute os testes de carga:
```bash
# Usando k6
k6 run load-test/checkout_test.py

# Usando Locust
locust -f load-test/api_test.py
```

3. Acesse o Grafana:
```bash
# Inicie o Grafana
docker-compose up -d grafana

# Acesse http://localhost:3000
```

## 📚 Recursos

### Templates
- [Template de Workflow CI/CD](ci/workflows/template.yml)
- [Template de Dashboard](monitoring/grafana/dashboard_template.json)
- [Template de Relatório de Performance](templates/relatorio_performance.md)

### Exemplos
- [Exemplo de Workflow](ci/workflows/exemplo.yml)
- [Exemplo de Dashboard](monitoring/grafana/exemplo.json)
- [Exemplo de Relatório](exemplos/relatorio_performance_exemplo.md)

## 🎓 Avaliação

- Configuração do CI/CD
- Qualidade dos testes de carga
- Configuração do monitoramento
- Documentação dos resultados 