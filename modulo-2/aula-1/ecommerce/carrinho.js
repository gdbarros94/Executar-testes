// Sistema de Carrinho de Compras com bugs intencionais para exercícios

class Carrinho {
    constructor() {
        this.items = [];
        this.descontos = {
            'PROMO10': 0.1,
            'PROMO20': 0.2
        };
    }

    // Bug 1: Não verifica se o produto existe
    adicionarProduto(produto, quantidade) {
        this.items.push({
            produto: produto,
            quantidade: quantidade
        });
    }

    // Bug 2: Cálculo incorreto do total (não multiplica pela quantidade)
    calcularTotal() {
        return this.items.reduce((total, item) => {
            return total + item.produto.preco;
        }, 0);
    }

    // Bug 3: Não valida código de desconto
    aplicarDesconto(codigo) {
        const total = this.calcularTotal();
        return total - (total * this.descontos[codigo]);
    }

    // Bug 4: Não limpa o carrinho após finalizar
    finalizarCompra() {
        const total = this.calcularTotal();
        return {
            sucesso: true,
            total: total,
            items: this.items
        };
    }
}

module.exports = Carrinho; 