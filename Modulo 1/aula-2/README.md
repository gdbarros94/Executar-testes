# Aula 2: Terminologia e Artefatos de Teste

## 🎯 Objetivos da Aula
- Compreender a terminologia específica de testes
- Identificar os principais artefatos de teste
- Criar documentação de teste básica
- Praticar a escrita de casos de teste

## 📚 Conteúdo

### 1. Terminologia de Testes

#### Termos Básicos
- **Test Case (Caso de Teste)**: Conjunto de condições e passos para verificar uma funcionalidade
- **Test Suite (Conjunto de Testes)**: Grupo de casos de teste relacionados
- **Test Plan (Plano de Teste)**: Documento que descreve a estratégia de teste
- **Test Report (Relatório de Teste)**: Documento com resultados dos testes

#### Comparação PT/EN
| Português | Inglês | Descrição |
|-----------|---------|-----------|
| Caso de Teste | Test Case | Cenário específico a ser testado |
| Plano de Teste | Test Plan | Estratégia e abordagem de testes |
| Relatório de Teste | Test Report | Resultados e análises dos testes |
| Bug | Bug | Erro no código |
| Defeito | Defect | Problema que pode causar falha |
| Falha | Failure | Manifestação visível de um defeito |

### 2. Artefatos de Teste

#### Documentação Essencial
1. **Plano de Teste**
   - Objetivos
   - Escopo
   - Estratégia
   - Cronograma

2. **Casos de Teste**
   - Pré-condições
   - Passos
   - Resultados esperados
   - Resultados reais

3. **Relatórios**
   - Métricas
   - Análises
   - Recomendações

### 3. Exemplo Prático

#### Template de Caso de Teste
```markdown
# Caso de Teste: Login de Usuário

## ID: CT-001
## Descrição: Verificar login com credenciais válidas

### Pré-condições
- Sistema acessível
- Usuário cadastrado

### Passos
1. Acessar página de login
2. Inserir email válido
3. Inserir senha válida
4. Clicar em "Entrar"

### Resultado Esperado
- Usuário é redirecionado para dashboard
- Mensagem de boas-vindas exibida

### Resultado Real
[Preencher após execução]
```

## 🎮 Atividade Prática

### Exercício 1: Criando Casos de Teste
1. Acesse o arquivo `exercicios/sistema_login.py`
2. Crie 3 casos de teste usando o template
3. Documente os casos no formato markdown
4. Compartilhe com a turma

### Exercício 2: Análise de Documentação
1. Leia o arquivo `exemplos/plano_teste_exemplo.md`
2. Identifique os elementos principais
3. Sugira melhorias
4. Crie um novo plano baseado no exemplo

## 📝 Material Complementar

### Templates
- [Template de Plano de Teste](templates/plano_teste.md)
- [Template de Caso de Teste](templates/caso_teste.md)
- [Template de Relatório](templates/relatorio.md)

### Próxima Aula
- Níveis de teste
- Testes unitários
- Testes de integração 