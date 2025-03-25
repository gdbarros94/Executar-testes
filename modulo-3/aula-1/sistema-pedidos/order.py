# Sistema de Pedidos com bugs intencionais para exercícios

class OrderProcessor:
    def __init__(self):
        self.orders = []
        self.tax_rate = 0.1  # Bug 1: Taxa fixa, deveria variar por estado

    # Bug 2: Não valida itens vazios
    def create_order(self, items, customer):
        order = {
            'id': self.generate_order_id(),
            'items': items,
            'customer': customer,
            'total': self.calculate_total(items),
            'status': 'pending'
        }
        
        self.orders.append(order)
        return order

    # Bug 3: Cálculo incorreto do total
    def calculate_total(self, items):
        subtotal = sum(item['price'] for item in items)
        # Bug 4: Não aplica desconto para grandes pedidos
        return subtotal + (subtotal * self.tax_rate)

    # Bug 5: IDs podem se repetir
    def generate_order_id(self):
        import random
        return random.randint(0, 999)

    # Bug 6: Não valida status atual
    def process_order(self, order_id):
        order = self.find_order(order_id)
        if order:
            order['status'] = 'processed'
            return True
        return False

    # Bug 7: Não trata pedido não encontrado
    def find_order(self, order_id):
        return next((order for order in self.orders if order['id'] == order_id), None)

    # Bug 8: Lista inclui pedidos cancelados
    def list_active_orders(self):
        return self.orders 