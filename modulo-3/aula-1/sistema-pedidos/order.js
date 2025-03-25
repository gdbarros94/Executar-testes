// Sistema de Pedidos com bugs intencionais para exercícios

class OrderProcessor {
    constructor() {
        this.orders = [];
        this.taxRate = 0.1; // Bug 1: Taxa fixa, deveria variar por estado
    }

    // Bug 2: Não valida itens vazios
    createOrder(items, customer) {
        const order = {
            id: this.generateOrderId(),
            items: items,
            customer: customer,
            total: this.calculateTotal(items),
            status: 'pending'
        };
        
        this.orders.push(order);
        return order;
    }

    // Bug 3: Cálculo incorreto do total
    calculateTotal(items) {
        const subtotal = items.reduce((sum, item) => sum + item.price, 0);
        // Bug 4: Não aplica desconto para grandes pedidos
        return subtotal + (subtotal * this.taxRate);
    }

    // Bug 5: IDs podem se repetir
    generateOrderId() {
        return Math.floor(Math.random() * 1000);
    }

    // Bug 6: Não valida status atual
    processOrder(orderId) {
        const order = this.findOrder(orderId);
        if (order) {
            order.status = 'processed';
            return true;
        }
        return false;
    }

    // Bug 7: Não trata pedido não encontrado
    findOrder(orderId) {
        return this.orders.find(order => order.id === orderId);
    }

    // Bug 8: Lista inclui pedidos cancelados
    listActiveOrders() {
        return this.orders;
    }
}

module.exports = OrderProcessor; 