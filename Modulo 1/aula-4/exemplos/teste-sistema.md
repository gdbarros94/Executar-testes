# Exemplo de Teste de Sistema: E-commerce

## 1. Fluxo de Compra Completo

### 1.1 Cadastro de Produtos
```javascript
describe('Cadastro de Produtos', () => {
    test('deve cadastrar produto com dados válidos', () => {
        const ecommerce = new Ecommerce();
        const resultado = ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        expect(resultado).toBe(true);
        
        const produto = ecommerce.produtos.get(1);
        expect(produto).toEqual({
            id: 1,
            nome: 'Notebook',
            preco: 3500,
            quantidade: 10
        });
    });

    test('deve falhar ao cadastrar produto com preço negativo', () => {
        const ecommerce = new Ecommerce();
        expect(() => {
            ecommerce.cadastrarProduto(1, 'Notebook', -3500, 10);
        }).toThrow();
    });
});
```

### 1.2 Adição ao Carrinho
```javascript
describe('Carrinho de Compras', () => {
    test('deve adicionar produto ao carrinho', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        
        const resultado = ecommerce.adicionarAoCarrinho(1, 2);
        expect(resultado).toBe(true);
        
        const qtdCarrinho = ecommerce.carrinho.get(1);
        expect(qtdCarrinho).toBe(2);
    });

    test('deve falhar ao adicionar produto sem estoque', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 5);
        
        expect(() => {
            ecommerce.adicionarAoCarrinho(1, 10);
        }).toThrow();
    });
});
```

### 1.3 Cálculo de Total
```javascript
describe('Cálculo de Total', () => {
    test('deve calcular total corretamente', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.cadastrarProduto(2, 'Mouse', 50, 20);
        
        ecommerce.adicionarAoCarrinho(1, 1);
        ecommerce.adicionarAoCarrinho(2, 2);
        
        const total = ecommerce.calcularTotal();
        expect(total).toBe(3600); // 3500 + (50 * 2)
    });

    test('deve aplicar desconto corretamente', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.adicionarAoCarrinho(1, 1);
        
        const desconto = ecommerce.aplicarDesconto('DESCONTO10');
        const total = ecommerce.calcularTotal();
        const totalComDesconto = total * (1 - desconto.percentual / 100);
        
        expect(totalComDesconto).toBe(3150); // 3500 - 10%
    });
});
```

### 1.4 Finalização de Compra
```javascript
describe('Finalização de Compra', () => {
    test('deve finalizar compra com sucesso', async () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.adicionarAoCarrinho(1, 1);
        
        const pedido = ecommerce.finalizarCompra('4111111111111111');
        
        expect(pedido).toMatchObject({
            status: 'aprovado',
            total: 3500
        });
        
        // Verifica se o estoque foi atualizado
        const estoqueAtual = ecommerce.estoque.get(1);
        expect(estoqueAtual).toBe(9);
    });

    test('deve falhar ao finalizar compra com cartão inválido', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.adicionarAoCarrinho(1, 1);
        
        expect(() => {
            ecommerce.finalizarCompra('123');
        }).toThrow();
    });
});
```

## 2. Fluxos de Negócio

### 2.1 Gestão de Estoque
```javascript
describe('Gestão de Estoque', () => {
    test('deve atualizar estoque corretamente', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        
        const resultado = ecommerce.atualizarEstoque(1, 5);
        expect(resultado).toBe(true);
        
        const estoqueAtual = ecommerce.estoque.get(1);
        expect(estoqueAtual).toBe(15);
    });

    test('deve listar apenas produtos com estoque', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 0);
        ecommerce.cadastrarProduto(2, 'Mouse', 50, 5);
        
        const produtos = ecommerce.obterProdutosDisponiveis();
        expect(produtos).toHaveLength(1);
        expect(produtos[0].id).toBe(2);
    });
});
```

### 2.2 Consulta de Pedidos
```javascript
describe('Consulta de Pedidos', () => {
    test('deve buscar pedido existente', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.adicionarAoCarrinho(1, 1);
        const pedido = ecommerce.finalizarCompra('4111111111111111');
        
        const pedidoEncontrado = ecommerce.buscarPedido(pedido.id);
        expect(pedidoEncontrado).toEqual(pedido);
    });

    test('deve retornar null para pedido inexistente', () => {
        const ecommerce = new Ecommerce();
        const pedido = ecommerce.buscarPedido(999);
        expect(pedido).toBeNull();
    });
});
```

## 3. Cenários de Erro

### 3.1 Validações
```javascript
describe('Validações do Sistema', () => {
    test('deve validar dados do produto', () => {
        const ecommerce = new Ecommerce();
        
        expect(() => {
            ecommerce.cadastrarProduto(null, 'Notebook', 3500, 10);
        }).toThrow();
        
        expect(() => {
            ecommerce.cadastrarProduto(1, '', 3500, 10);
        }).toThrow();
    });

    test('deve validar operações do carrinho', () => {
        const ecommerce = new Ecommerce();
        
        expect(() => {
            ecommerce.adicionarAoCarrinho(999, 1);
        }).toThrow('Produto não encontrado');
        
        expect(() => {
            ecommerce.adicionarAoCarrinho(1, -1);
        }).toThrow();
    });
});
```

### 3.2 Tratamento de Erros
```javascript
describe('Tratamento de Erros', () => {
    test('deve tratar falha na finalização', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.adicionarAoCarrinho(1, 1);
        
        try {
            ecommerce.finalizarCompra('123');
            fail('Deveria ter lançado erro');
        } catch (error) {
            expect(error.message).toBe('Cartão inválido');
        }
    });

    test('deve manter consistência em caso de erro', () => {
        const ecommerce = new Ecommerce();
        ecommerce.cadastrarProduto(1, 'Notebook', 3500, 10);
        ecommerce.adicionarAoCarrinho(1, 1);
        
        try {
            ecommerce.finalizarCompra('123');
        } catch (error) {
            // Verifica se o carrinho não foi limpo
            expect(ecommerce.carrinho.size).toBe(1);
            // Verifica se o estoque não foi alterado
            expect(ecommerce.estoque.get(1)).toBe(10);
        }
    });
});
``` 