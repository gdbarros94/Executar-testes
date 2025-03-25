// Sistema de Processamento de Pagamentos com bugs intencionais

class ProcessadorPagamentos {
    constructor() {
        this.taxas = {
            credito: 0.05,  // Bug 1: Taxa incorreta (deveria ser 0.015)
            debito: 0.02,
            pix: 0
        };
        this.transacoes = [];
    }

    // Bug 2: Não valida valor negativo
    processarPagamento(valor, metodo) {
        const taxa = this.calcularTaxa(valor, metodo);
        const total = valor + taxa;
        
        const transacao = {
            id: this.gerarId(),
            valor,
            metodo,
            taxa,
            total,
            status: 'aprovado'
        };
        
        this.transacoes.push(transacao);
        return transacao;
    }

    // Bug 3: Não verifica método de pagamento válido
    calcularTaxa(valor, metodo) {
        return valor * this.taxas[metodo];
    }

    // Bug 4: IDs podem se repetir
    gerarId() {
        return Math.floor(Math.random() * 1000);
    }

    // Bug 5: Não valida ID existente
    buscarTransacao(id) {
        return this.transacoes.find(t => t.id === id);
    }

    // Bug 6: Não verifica status atual
    cancelarTransacao(id) {
        const transacao = this.buscarTransacao(id);
        if (transacao) {
            transacao.status = 'cancelado';
            return true;
        }
        return false;
    }

    // Bug 7: Lista transações canceladas
    listarTransacoesAtivas() {
        return this.transacoes;
    }
}

module.exports = ProcessadorPagamentos; 