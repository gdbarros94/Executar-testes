// Serviço de Pagamentos com dívida técnica intencional

class PaymentProcessor {
    constructor() {
        this.transactions = [];
        this.fees = {
            credit: 0.05,  // Bug 1: Taxa muito alta
            debit: 0.02,
            pix: 0
        };
    }

    // Bug 2: Não valida dados do cartão
    async processPayment(amount, method, cardData) {
        const fee = this.calculateFee(amount, method);
        const total = amount + fee;

        const transaction = {
            id: this.generateId(),
            amount,
            fee,
            total,
            method,
            status: 'pending'
        };

        // Bug 3: Não trata erros assíncronos
        await this.validatePayment(transaction);
        
        transaction.status = 'completed';
        this.transactions.push(transaction);
        
        return transaction;
    }

    // Bug 4: Não considera taxas diferentes por valor
    calculateFee(amount, method) {
        return amount * this.fees[method];
    }

    // Bug 5: Validação simulada sem verificações reais
    async validatePayment(transaction) {
        return new Promise(resolve => {
            setTimeout(resolve, 100);
        });
    }

    // Bug 6: Não implementa retry em caso de falha
    async retryPayment(transactionId) {
        const transaction = this.findTransaction(transactionId);
        if (transaction) {
            transaction.status = 'completed';
            return true;
        }
        return false;
    }

    // Bug 7: Não valida status atual
    async refundPayment(transactionId) {
        const transaction = this.findTransaction(transactionId);
        if (transaction) {
            transaction.status = 'refunded';
            return true;
        }
        return false;
    }

    // Bug 8: Busca ineficiente
    findTransaction(id) {
        return this.transactions.find(t => t.id === id);
    }

    // Bug 9: IDs podem colidir
    generateId() {
        return Math.floor(Math.random() * 1000);
    }
}

module.exports = PaymentProcessor; 