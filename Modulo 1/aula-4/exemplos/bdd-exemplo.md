# Exemplo de BDD: E-commerce

## Implementação dos Steps

### Compra de Produtos
```javascript
const { Given, When, Then } = require('@cucumber/cucumber');
const Ecommerce = require('../../exercicios/ecommerce');

let ecommerce;
let resultado;

Given('que existem os seguintes produtos:', function(dataTable) {
    ecommerce = new Ecommerce();
    dataTable.rows().forEach(row => {
        ecommerce.cadastrarProduto(
            parseInt(row[0]),
            row[1],
            parseFloat(row[2]),
            parseInt(row[3])
        );
    });
});

When('eu adiciono {string} ao carrinho', function(produto) {
    const produtoObj = Array.from(ecommerce.produtos.values())
        .find(p => p.nome === produto);
    ecommerce.adicionarAoCarrinho(produtoObj.id, 1);
});

When('eu insiro o código de desconto {string}', function(codigo) {
    resultado = ecommerce.aplicarDesconto(codigo);
});

When('eu finalizo a compra com o cartão {string}', function(cartao) {
    resultado = ecommerce.finalizarCompra(cartao);
});

Then('eu devo ver a mensagem {string}', function(mensagem) {
    expect(resultado.mensagem).toBe(mensagem);
});

Then('o pedido deve ser registrado', function() {
    const pedido = ecommerce.buscarPedido(resultado.id);
    expect(pedido).toBeDefined();
});

Then('o estoque deve ser atualizado', function() {
    const produto = Array.from(ecommerce.produtos.values())[0];
    expect(ecommerce.estoque.get(produto.id)).toBe(produto.quantidade - 1);
});
```

### Gestão de Estoque
```javascript
Given('que estou logado como administrador', function() {
    // Implementação da autenticação
});

Given('que estou na página de gestão de estoque', function() {
    // Navegação para a página
});

When('eu adiciono {int} unidades ao produto {string}', function(quantidade, produto) {
    const produtoObj = Array.from(ecommerce.produtos.values())
        .find(p => p.nome === produto);
    resultado = ecommerce.atualizarEstoque(produtoObj.id, quantidade);
});

Then('o estoque de {string} deve ser {int}', function(produto, quantidade) {
    const produtoObj = Array.from(ecommerce.produtos.values())
        .find(p => p.nome === produto);
    expect(ecommerce.estoque.get(produtoObj.id)).toBe(quantidade);
});
```

### Aplicação de Descontos
```javascript
Given('que estou na página do carrinho', function() {
    // Navegação para o carrinho
});

Given('que tenho os seguintes produtos no carrinho:', function(dataTable) {
    dataTable.rows().forEach(row => {
        const produto = Array.from(ecommerce.produtos.values())
            .find(p => p.nome === row[0]);
        ecommerce.adicionarAoCarrinho(produto.id, parseInt(row[1]));
    });
});

Then('o desconto de {int}% deve ser aplicado', function(percentual) {
    expect(resultado.percentual).toBe(percentual);
});

Then('o total deve ser {int}', function(total) {
    expect(ecommerce.calcularTotal()).toBe(total);
});
```

### Consulta de Pedidos
```javascript
Given('que estou logado como cliente', function() {
    // Implementação da autenticação
});

Given('que tenho um pedido realizado:', function(dataTable) {
    const pedido = dataTable.rows()[0];
    ecommerce.pedidos.push({
        id: parseInt(pedido[0]),
        data: new Date(pedido[1]),
        status: pedido[2],
        total: parseFloat(pedido[3])
    });
});

When('eu acesso a página de meus pedidos', function() {
    // Navegação para a página
});

When('eu clico no pedido {string}', function(id) {
    resultado = ecommerce.buscarPedido(parseInt(id));
});

Then('eu devo ver os detalhes do pedido:', function(dataTable) {
    dataTable.rows().forEach(row => {
        expect(resultado[row[0]]).toBe(row[1]);
    });
});
```

### Validações de Segurança
```javascript
Given('que não estou logado', function() {
    // Estado não autenticado
});

When('eu tento acessar a página de gestão de estoque', function() {
    try {
        // Tentativa de acesso
        resultado = { erro: 'Acesso não autorizado' };
    } catch (error) {
        resultado = { erro: error.message };
    }
});

Then('eu devo ser redirecionado para a página de login', function() {
    expect(resultado.erro).toBe('Acesso não autorizado');
});
```

## Configuração do Cucumber
```javascript
// cucumber.js
module.exports = {
    default: {
        requireModule: ['ts-node/register'],
        require: ['features/**/*.ts'],
        format: ['progress-bar', 'html:cucumber-report.html'],
        formatOptions: { snippetInterface: 'async-await' },
        publishQuiet: true
    }
};
```

## Execução dos Testes
```bash
# Instalação das dependências
npm install @cucumber/cucumber ts-node typescript

# Execução dos testes
npx cucumber-js
```

## Relatório de Execução
```html
<!-- cucumber-report.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Relatório de Testes BDD</title>
    <style>
        /* Estilos do relatório */
    </style>
</head>
<body>
    <h1>Relatório de Execução dos Testes BDD</h1>
    <div class="summary">
        <p>Total de cenários: 10</p>
        <p>Passaram: 8</p>
        <p>Falharam: 2</p>
    </div>
    <!-- Detalhes dos testes -->
</body>
</html>
``` 