// Sistema de Gerenciamento de Produtos com bugs intencionais para exercícios

class GerenciadorProdutos {
    constructor() {
        this.produtos = new Map();
    }

    // Bug 1: Não valida preço negativo
    cadastrarProduto(id, nome, preco, estoque) {
        this.produtos.set(id, {
            nome: nome,
            preco: preco,
            estoque: estoque
        });
        return true;
    }

    // Bug 2: Não verifica se produto existe
    buscarProduto(id) {
        return this.produtos.get(id);
    }

    // Bug 3: Não atualiza estoque corretamente
    atualizarEstoque(id, quantidade) {
        const produto = this.produtos.get(id);
        produto.estoque = quantidade;
        return true;
    }

    // Bug 4: Lista produtos sem estoque
    listarProdutos() {
        return Array.from(this.produtos.values());
    }

    // Bug 5: Não valida dados de entrada
    atualizarProduto(id, dados) {
        const produto = this.produtos.get(id);
        Object.assign(produto, dados);
        return true;
    }
}

module.exports = GerenciadorProdutos; 