# API de Produtos com bugs intencionais

class ProductAPI:
    def __init__(self):
        self.products = {}

    # Bug 1: Não valida dados obrigatórios
    def create_product(self, data):
        id = self.generate_id()
        self.products[id] = {
            **data,
            'id': id,
            'created_at': datetime.now()
        }
        return id

    # Bug 2: Não implementa paginação corretamente
    def list_products(self, page=1, limit=10):
        all_products = list(self.products.values())
        start = (page - 1) * limit
        return all_products[start:start + limit]

    # Bug 3: Não valida existência do produto
    def update_product(self, id, data):
        product = self.products.get(id)
        product.update(data)
        return True

    # Bug 4: Permite preço negativo
    def validate_price(self, price):
        return isinstance(price, (int, float))

    # Bug 5: Busca case sensitive
    def search_products(self, term):
        return [
            product for product in self.products.values()
            if term in product['name']
        ]

    # Bug 6: IDs podem colidir
    def generate_id(self):
        import random
        return random.randint(0, 999)

    # Bug 7: Não valida estoque
    def check_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        return product['stock'] >= quantity

    # Bug 8: Não atualiza data de modificação
    def update_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        product['stock'] = quantity
        return True 