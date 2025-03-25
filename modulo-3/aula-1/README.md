# Aula 1: Plano de Teste Robusto

## 🎯 Objetivos
- Compreender a importância de um plano de teste bem estruturado
- Aprender a criar planos de teste profissionais
- Desenvolver critérios de aceitação claros
- Criar matriz de rastreabilidade

## 📚 Conteúdo

### 1. Plano de Teste
- Estrutura básica
- Elementos essenciais
- Boas práticas
- Exemplos práticos

### 2. Critérios de Aceitação
- Definição clara
- Formato SMART
- Exemplos práticos
- Validação

### 3. Matriz de Rastreabilidade
- Conceitos básicos
- Como criar
- Ferramentas
- Prática

## 🎮 Projeto Prático: Sistema de Pedidos

### Estrutura do Projeto
- `sistema_pedidos/`: Sistema com bugs intencionais
  - `order.py`: Processador de pedidos
  - `test_order.py`: Testes automatizados
- `templates/`: Templates de documentação
  - `plano_teste_template.md`
  - `matriz_rastreabilidade.md`

### Atividades

#### 1. Análise do Sistema
- Identificar funcionalidades
- Mapear requisitos
- Documentar bugs
- Criar casos de teste

#### 2. Documentação
- Criar plano de teste
- Definir critérios de aceitação
- Desenvolver matriz de rastreabilidade
- Documentar resultados

## 📝 Exercícios

### Exercício 1: Plano de Teste
1. Analise o sistema de pedidos
2. Crie um plano de teste completo
3. Defina critérios de aceitação
4. Documente no formato markdown

### Exercício 2: Matriz de Rastreabilidade
1. Identifique requisitos
2. Mapeie casos de teste
3. Crie matriz de rastreabilidade
4. Valide cobertura

### Exercício 3: Documentação
1. Crie relatório de análise
2. Documente bugs encontrados
3. Proponha melhorias
4. Prepare apresentação

## 🛠️ Como Executar

1. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Execute os testes:
```bash
pytest sistema_pedidos/test_order.py -v
```

3. Gere relatório:
```bash
pytest sistema_pedidos/test_order.py --html=report.html
```

## 📚 Recursos

### Templates
- [Template de Plano de Teste](templates/plano_teste_template.md)
- [Template de Matriz de Rastreabilidade](templates/matriz_rastreabilidade.md)

### Exemplos
- [Exemplo de Plano de Teste](exemplos/plano_teste_exemplo.md)
- [Exemplo de Matriz de Rastreabilidade](exemplos/matriz_exemplo.md)

## 🎓 Avaliação

- Qualidade do plano de teste
- Completude da matriz de rastreabilidade
- Documentação dos bugs
- Proposta de melhorias 