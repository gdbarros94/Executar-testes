// Sistema de E-commerce com bugs intencionais para exercício de testes
class Ecommerce {
    constructor() {
        this.produtos = new Map();
        this.carrinho = new Map();
        this.estoque = new Map();
        this.pedidos = [];
    }

    cadastrarProduto(id, nome, preco, quantidade) {
        // Bug: não valida se o preço é positivo
        this.produtos.set(id, {
            id,
            nome,
            preco,
            quantidade
        });
        this.estoque.set(id, quantidade);
        return true;
    }

    adicionarAoCarrinho(id, quantidade) {
        // Bug: não verifica se o produto existe
        const produto = this.produtos.get(id);
        if (!produto) {
            throw new Error('Produto não encontrado');
        }

        // Bug: não verifica estoque
        const qtdAtual = this.carrinho.get(id) || 0;
        this.carrinho.set(id, qtdAtual + quantidade);
        return true;
    }

    calcularTotal() {
        // Bug: não considera desconto
        let total = 0;
        for (const [id, quantidade] of this.carrinho) {
            const produto = this.produtos.get(id);
            total += produto.preco * quantidade;
        }
        return total;
    }

    finalizarCompra(cartao) {
        // Bug: não valida cartão
        const total = this.calcularTotal();
        
        // Bug: não atualiza estoque
        const pedido = {
            id: Date.now(),
            itens: Array.from(this.carrinho.entries()),
            total,
            status: 'aprovado',
            data: new Date()
        };

        this.pedidos.push(pedido);
        this.carrinho.clear();
        return pedido;
    }

    buscarPedido(id) {
        // Bug: não valida ID
        return this.pedidos.find(p => p.id === id);
    }

    atualizarEstoque(id, quantidade) {
        // Bug: não verifica se quantidade é positiva
        const qtdAtual = this.estoque.get(id) || 0;
        this.estoque.set(id, qtdAtual + quantidade);
        return true;
    }

    obterProdutosDisponiveis() {
        // Bug: retorna produtos sem estoque
        return Array.from(this.produtos.values());
    }

    aplicarDesconto(codigo) {
        // Bug: não valida código de desconto
        return {
            percentual: 10,
            mensagem: 'Desconto aplicado com sucesso!'
        };
    }
}

module.exports = Ecommerce; 