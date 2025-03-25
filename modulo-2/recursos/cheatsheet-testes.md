# Cheatsheet - Testes de Software

## Tipos de Teste

### Testes Funcionais
```javascript
// Exemplo de teste funcional
test('deve calcular o total corretamente', () => {
    const carrinho = new Carrinho();
    carrinho.adicionarProduto({id: 1, preco: 100}, 2);
    expect(carrinho.calcularTotal()).toBe(200);
});
```

### Testes de Regressão
- Executar após mudanças
- Verificar funcionalidades existentes
- Documentar resultados

### Testes de Desempenho
```javascript
// Exemplo de teste de performance
console.time('operacao');
// ... código a ser testado
console.timeEnd('operacao');
```

## Termos Importantes

### Português -> English
- Teste de Unidade -> Unit Test
- Teste de Integração -> Integration Test
- Teste de Sistema -> System Test
- Teste de Aceitação -> Acceptance Test
- Caso de Teste -> Test Case
- Plano de Teste -> Test Plan
- Relatório de Teste -> Test Report

## Comandos Úteis

### NPM
```bash
npm test           # Executar testes
npm run test:watch # Modo watch
npm run coverage   # Relatório de cobertura
```

### Jest
```javascript
describe('suite', () => {});    // Agrupar testes
test('caso', () => {});        // Definir teste
expect(valor).toBe(esperado);  // Asserção
```

## Boas Práticas

### Estrutura de Teste
1. Arrange (Preparar)
2. Act (Agir)
3. Assert (Verificar)

### Nomenclatura
- Descritiva e clara
- Indicar cenário testado
- Usar padrão consistente

### Documentação
- Descrever objetivo
- Listar pré-requisitos
- Documentar passos
- Registrar resultados

## Dicas de Debug

### Console
```javascript
console.log()    // Informação geral
console.error()  // Erros
console.table()  // Dados tabulares
console.time()   // Performance
```

### Breakpoints
- Debugger statement
- Chrome DevTools
- VS Code debugger

## Relatórios

### Elementos Essenciais
1. Sumário executivo
2. Casos executados
3. Resultados obtidos
4. Bugs encontrados
5. Recomendações

### Métricas
- Total de testes
- Taxa de sucesso
- Cobertura de código
- Tempo de execução 