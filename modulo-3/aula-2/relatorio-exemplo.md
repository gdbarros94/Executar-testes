# Relatório de Defeitos - API de Produtos

## Defeito #1: Validação de Dados Ausente

### Descrição
A API não valida campos obrigatórios ao criar um produto novo.

### Impacto
- **Severidade:** Alta
- **Prioridade:** Alta
- **Módulos Afetados:** Cadastro de Produtos, Estoque

### Passos para Reproduzir
1. Fazer POST para `/products`
2. Enviar objeto vazio `{}`
3. Produto é criado sem dados necessários

### Comportamento Esperado
- API deve validar campos obrigatórios
- Retornar erro 400 se faltarem dados

### Comportamento Atual
- Cria produto com dados vazios
- Não retorna erro

### Evidências
```javascript
// Requisição
POST /products
{}

// Resposta
200 OK
{
  "id": 123,
  "createdAt": "2024-02-20T10:00:00Z"
}
```

### Sugestão de Correção
```javascript
createProduct(data) {
    if (!data.name || !data.price) {
        throw new Error('Dados obrigatórios ausentes');
    }
    // ... resto do código
}
```

## Defeito #2: Paginação Incorreta

### Descrição
Paginação não considera filtros aplicados.

### Impacto
- **Severidade:** Média
- **Prioridade:** Média
- **Módulos Afetados:** Listagem de Produtos

### Passos para Reproduzir
1. GET `/products?category=eletronicos&page=2`
2. Paginação considera todos os produtos

### Comportamento Esperado
- Aplicar filtros antes da paginação
- Retornar página correta do resultado filtrado

### Comportamento Atual
- Ignora filtros na paginação
- Retorna dados incorretos

### Evidências
```javascript
// Atual
listProducts(page = 1, limit = 10) {
    const start = (page - 1) * limit;
    return allProducts.slice(start, start + limit);
}
```

### Sugestão de Correção
```javascript
listProducts(page = 1, limit = 10, filters = {}) {
    const filtered = this.applyFilters(allProducts, filters);
    const start = (page - 1) * limit;
    return filtered.slice(start, start + limit);
}
```

## Defeito #3: Geração de IDs Insegura

### Descrição
IDs de produtos podem colidir devido ao uso de números aleatórios simples.

### Impacto
- **Severidade:** Alta
- **Prioridade:** Média
- **Módulos Afetados:** Todo o Sistema

### Passos para Reproduzir
1. Criar múltiplos produtos rapidamente
2. Observar IDs gerados

### Comportamento Esperado
- IDs únicos garantidos
- Sem possibilidade de colisão

### Comportamento Atual
- Usa Math.random()
- Possível colisão de IDs

### Evidências
```javascript
generateId() {
    return Math.floor(Math.random() * 1000);
}
```

### Sugestão de Correção
```javascript
generateId() {
    return Date.now() + '-' + Math.random().toString(36).substr(2, 9);
}
```

## Recomendações Gerais

### Priorização
1. Validação de Dados (#1)
2. Geração de IDs (#3)
3. Paginação (#2)

### Próximos Passos
1. Implementar validações
2. Adicionar testes automatizados
3. Revisar logs de erro
4. Atualizar documentação

### Métricas
- Total de Defeitos: 3
- Críticos: 2
- Médios: 1
- Baixos: 0 