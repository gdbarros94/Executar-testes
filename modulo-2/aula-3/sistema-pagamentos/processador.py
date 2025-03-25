# Sistema de Processamento de Pagamentos com bugs intencionais

class ProcessadorPagamentos:
    def __init__(self):
        self.taxas = {
            'credito': 0.05,  # Bug 1: Taxa incorreta (deveria ser 0.015)
            'debito': 0.02,
            'pix': 0
        }
        self.transacoes = []

    # Bug 2: Não valida valor negativo
    def processar_pagamento(self, valor, metodo):
        taxa = self.calcular_taxa(valor, metodo)
        total = valor + taxa
        
        transacao = {
            'id': self.gerar_id(),
            'valor': valor,
            'metodo': metodo,
            'taxa': taxa,
            'total': total,
            'status': 'aprovado'
        }
        
        self.transacoes.append(transacao)
        return transacao

    # Bug 3: Não verifica método de pagamento válido
    def calcular_taxa(self, valor, metodo):
        return valor * self.taxas.get(metodo, 0)

    # Bug 4: IDs podem se repetir
    def gerar_id(self):
        import random
        return random.randint(0, 999)

    # Bug 5: Não valida ID existente
    def buscar_transacao(self, id):
        return next((t for t in self.transacoes if t['id'] == id), None)

    # Bug 6: Não verifica status atual
    def cancelar_transacao(self, id):
        transacao = self.buscar_transacao(id)
        if transacao:
            transacao['status'] = 'cancelado'
            return True
        return False

    # Bug 7: Lista transações canceladas
    def listar_transacoes_ativas(self):
        return self.transacoes 