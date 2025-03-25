# Sistema de Carrinho de Compras com bugs intencionais para exercícios

class Carrinho:
    def __init__(self):
        self.items = []
        self.descontos = {
            'PROMO10': 0.1,
            'PROMO20': 0.2
        }

    # Bug 1: Não verifica se o produto existe
    def adicionar_produto(self, produto, quantidade):
        self.items.append({
            'produto': produto,
            'quantidade': quantidade
        })

    # Bug 2: Cálculo incorreto do total (não multiplica pela quantidade)
    def calcular_total(self):
        return sum(item['produto']['preco'] for item in self.items)

    # Bug 3: Não valida código de desconto
    def aplicar_desconto(self, codigo):
        total = self.calcular_total()
        return total - (total * self.descontos.get(codigo, 0))

    # Bug 4: Não limpa o carrinho após finalizar
    def finalizar_compra(self):
        total = self.calcular_total()
        return {
            'sucesso': True,
            'total': total,
            'items': self.items
        } 