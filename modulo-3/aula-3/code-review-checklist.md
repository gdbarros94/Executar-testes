# Checklist de Code Review

## 1. Qualidade do Código

### 1.1 Legibilidade
- [ ] Nomes de variáveis claros e significativos
- [ ] Funções com responsabilidade única
- [ ] Comentários explicativos quando necessário
- [ ] Formatação consistente
- [ ] Complexidade ciclomática aceitável

### 1.2 Manutenibilidade
- [ ] Código duplicado eliminado
- [ ] Funções com tamanho adequado
- [ ] Dependências claramente definidas
- [ ] Arquitetura consistente
- [ ] Padrões de projeto apropriados

### 1.3 Performance
- [ ] Algoritmos eficientes
- [ ] Uso adequado de memória
- [ ] Queries otimizadas
- [ ] Cache quando apropriado
- [ ] Operações em lote quando possível

## 2. Testes

### 2.1 Cobertura
- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Testes de borda
- [ ] Casos de erro testados
- [ ] Mocks apropriados

### 2.2 Qualidade dos Testes
- [ ] Testes independentes
- [ ] Assertions claros
- [ ] Setup/Teardown adequados
- [ ] Dados de teste realistas
- [ ] Testes legíveis

## 3. Segurança

### 3.1 Validações
- [ ] Input sanitizado
- [ ] Autenticação adequada
- [ ] Autorização verificada
- [ ] Dados sensíveis protegidos
- [ ] SQL Injection prevenido

### 3.2 Tratamento de Erros
- [ ] Erros logados apropriadamente
- [ ] Mensagens de erro seguras
- [ ] Try/catch em operações críticas
- [ ] Rollback em falhas
- [ ] Timeout configurado

## 4. Documentação

### 4.1 Código
- [ ] Funções documentadas
- [ ] Parâmetros descritos
- [ ] Retornos explicados
- [ ] Exemplos de uso
- [ ] Avisos importantes

### 4.2 API
- [ ] Endpoints documentados
- [ ] Payloads descritos
- [ ] Respostas exemplificadas
- [ ] Erros documentados
- [ ] Autenticação explicada

## 5. Boas Práticas

### 5.1 Versionamento
- [ ] Commits atômicos
- [ ] Mensagens claras
- [ ] Branch correta
- [ ] Conflitos resolvidos
- [ ] Histórico preservado

### 5.2 Processo
- [ ] Code review solicitado
- [ ] Testes passando
- [ ] Lint sem erros
- [ ] Build funcionando
- [ ] Documentação atualizada

## 6. Critérios de Aceitação

### 6.1 Funcionalidade
- [ ] Requisitos atendidos
- [ ] Casos de uso cobertos
- [ ] Integrações testadas
- [ ] UI/UX adequada
- [ ] Performance aceitável

### 6.2 Qualidade
- [ ] Sem bugs conhecidos
- [ ] Cobertura de testes adequada
- [ ] Métricas de qualidade
- [ ] Revisão de segurança
- [ ] Documentação completa 