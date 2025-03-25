# Aula 4 - Ferramentas Profissionais

## Objetivos
- Conhecer ferramentas profissionais de teste
- Configurar ambiente de testes automatizados
- Implementar testes E2E com Playwright
- Criar pipeline de CI/CD

## Conteúdo

### 1. Playwright
- Instalação e configuração
- Seletores e comandos básicos
- Page Objects
- Relatórios e screenshots

### 2. Integração Contínua
- GitHub Actions
- Configuração de workflow
- Execução automática de testes
- Geração de relatórios

### 3. Relatórios e Métricas
- Relatórios de execução
- Métricas de desempenho
- Análise de resultados
- Tomada de decisão

## Projeto Prático: Testes E2E

### Estrutura do Projeto
- `tests/`: Testes E2E
  - `test_checkout.py`: Testes do fluxo de checkout
  - `test_login.py`: Testes do fluxo de login
- `pages/`: Page Objects
  - `checkout_page.py`: Objetos da página de checkout
  - `login_page.py`: Objetos da página de login
- `relatorio-desempenho.md`: Análise de performance

### Atividades

#### 1. Configuração do Playwright
- Instalar e configurar Playwright
- Criar primeiro teste E2E
- Configurar relatórios
- Executar testes

#### 2. Pipeline CI/CD
- Configurar GitHub Actions
- Integrar testes automatizados
- Gerar relatórios
- Notificar resultados

## Exercícios

### Exercício 1: Testes E2E
- Criar testes para fluxo de compra
- Implementar Page Objects
- Adicionar screenshots
- Gerar relatórios

### Exercício 2: CI/CD
- Configurar pipeline
- Automatizar execução
- Validar resultados
- Corrigir falhas

### Exercício 3: Análise de Desempenho
- Coletar métricas
- Analisar resultados
- Identificar gargalos
- Propor melhorias

## Como Executar os Testes

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instale as dependências do Playwright:
```bash
playwright install
```

3. Execute os testes:
```bash
pytest tests/ --headed
```

4. Gere relatório HTML:
```bash
pytest tests/ --html=report.html
```

## Entrega
- Testes E2E implementados
- Pipeline configurado
- Relatórios gerados
- Análise de desempenho

## Critérios de Avaliação
- Qualidade dos testes E2E
- Configuração do pipeline
- Clareza dos relatórios
- Análise de resultados

## Recursos Adicionais
- [Documentação do Playwright](https://playwright.dev/python/docs/intro)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Pytest HTML Report](https://pytest-html.readthedocs.io/)
- [Locust para Testes de Carga](https://locust.io/) 