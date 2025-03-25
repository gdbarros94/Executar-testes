// API de Produtos com bugs intencionais

class ProductAPI {
    constructor() {
        this.products = new Map();
    }

    // Bug 1: Não valida dados obrigatórios
    createProduct(data) {
        const id = this.generateId();
        this.products.set(id, {
            ...data,
            id,
            createdAt: new Date()
        });
        return id;
    }

    // Bug 2: Não implementa paginação corretamente
    listProducts(page = 1, limit = 10) {
        const allProducts = Array.from(this.products.values());
        const start = (page - 1) * limit;
        return allProducts.slice(start, start + limit);
    }

    // Bug 3: Não valida existência do produto
    updateProduct(id, data) {
        const product = this.products.get(id);
        Object.assign(product, data);
        return true;
    }

    // Bug 4: Permite preço negativo
    validatePrice(price) {
        return typeof price === 'number';
    }

    // Bug 5: Busca case sensitive
    searchProducts(term) {
        return Array.from(this.products.values())
            .filter(product => product.name.includes(term));
    }

    // Bug 6: IDs podem colidir
    generateId() {
        return Math.floor(Math.random() * 1000);
    }

    // Bug 7: Não valida estoque
    checkStock(productId, quantity) {
        const product = this.products.get(productId);
        return product.stock >= quantity;
    }

    // Bug 8: Não atualiza data de modificação
    updateStock(productId, quantity) {
        const product = this.products.get(productId);
        product.stock = quantity;
        return true;
    }
}

module.exports = ProductAPI; 