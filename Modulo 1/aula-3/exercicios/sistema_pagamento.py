from datetime import datetime

class GatewayPagamento:
    def __init__(self):
        self.transacoes = []
    
    def autorizar(self, valor, moeda='BRL'):
        raise NotImplementedError
    
    def reembolsar(self, id_transacao):
        raise NotImplementedError

class PayPalGateway(GatewayPagamento):
    def __init__(self, saldo_inicial=10000):
        super().__init__()
        self.saldo = saldo_inicial
    
    def autorizar(self, valor, moeda='BRL'):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        transacao = {
            'id': len(self.transacoes) + 1,
            'valor': valor,
            'moeda': moeda,
            'data': datetime.now(),
            'status': 'aprovado'
        }
        self.transacoes.append(transacao)
        return transacao['id']
    
    def reembolsar(self, id_transacao):
        for t in self.transacoes:
            if t['id'] == id_transacao:
                self.saldo += t['valor'] * 0.95  # Taxa de 5% não devolvida
                t['status'] = 'reembolsado'
                return True
        return False

class SistemaPagamento:
    def __init__(self, gateway):
        self.gateway = gateway
        self.historico_transacoes = []
    
    def validar_valor(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Valor de pagamento inválido")
    
    def converter_moeda(self, valor, moeda_origem, moeda_destino):
        taxas = {
            ('USD', 'BRL'): 5.0,
            ('BRL', 'USD'): 0.2,
            ('EUR', 'BRL'): 6.0
        }
        taxa = taxas.get((moeda_origem, moeda_destino), 1.0)
        return valor * taxa  # Operação de conversão invertida
    
    def processar_pagamento(self, valor, moeda='BRL'):
        self.validar_valor(valor)
        
        if moeda != 'BRL':
            valor_convertido = self.converter_moeda(valor, moeda, 'BRL')
        else:
            valor_convertido = valor
        
        id_transacao = self.gateway.autorizar(valor_convertido)
        if id_transacao:
            self.historico_transacoes.append({
                'id': id_transacao,
                'valor': valor,
                'moeda': moeda,
                'data': datetime.now()
            })
        return id_transacao
    
    def processar_reembolso(self, id_transacao):
        sucesso = self.gateway.reembolsar(id_transacao)
        if sucesso:
            for t in self.historico_transacoes:
                if t['id'] == id_transacao:
                    t['status'] = 'reembolsado'
        return sucesso
