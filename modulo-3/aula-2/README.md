# Aula 2: Relato de Defeitos

## 🎯 Objetivos
- Aprender a documentar defeitos de forma profissional
- Desenvolver habilidades de comunicação técnica
- Compreender a importância de evidências
- Praticar priorização de bugs

## 📚 Conteúdo

### 1. Documentação de Defeitos
- Estrutura de um relatório de bug
- Elementos essenciais
- Boas práticas
- Exemplos práticos

### 2. Comunicação Efetiva
- Linguagem técnica
- Clareza e objetividade
- Evidências e provas
- Contexto e impacto

### 3. Priorização
- Critérios de severidade
- Critérios de urgência
- Matriz de priorização
- Decisões de negócio

## 🎮 Projeto Prático: API com Bugs

### Estrutura do Projeto
- `api_bugada/`: API com defeitos intencionais
  - `products.py`: API de produtos
  - `test_products.py`: Testes automatizados
- `templates/`: Templates de documentação
  - `relatorio_bug_template.md`
  - `matriz_priorizacao.md`

### Atividades

#### 1. Análise da API
- Identificar endpoints
- Testar funcionalidades
- Documentar defeitos
- Coletar evidências

#### 2. Documentação
- Criar relatórios de bug
- Priorizar defeitos
- Propor soluções
- Documentar resultados

## 📝 Exercícios

### Exercício 1: Relatório de Bug
1. Analise a API de produtos
2. Identifique defeitos
3. Crie relatórios detalhados
4. Inclua evidências

### Exercício 2: Priorização
1. Liste todos os defeitos
2. Aplique critérios de severidade
3. Aplique critérios de urgência
4. Crie matriz de priorização

### Exercício 3: Comunicação
1. Documente impactos
2. Proponha soluções
3. Estime esforço
4. Prepare apresentação

## 🛠️ Como Executar

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute os testes:
```bash
pytest api_bugada/test_products.py -v
```

3. Gere relatório:
```bash
pytest api_bugada/test_products.py --html=report.html
```

## 📚 Recursos

### Templates
- [Template de Relatório de Bug](templates/relatorio_bug_template.md)
- [Template de Matriz de Priorização](templates/matriz_priorizacao.md)

### Exemplos
- [Exemplo de Relatório de Bug](exemplos/relatorio_bug_exemplo.md)
- [Exemplo de Matriz de Priorização](exemplos/matriz_priorizacao_exemplo.md)

## 🎓 Avaliação

- Qualidade dos relatórios de bug
- Completude das evidências
- Clareza da comunicação
- Justificativa da priorização 