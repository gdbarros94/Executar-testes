# Sistema de E-commerce com bugs intencionais para exercício de testes
class Ecommerce:
    def __init__(self):
        self.produtos = {}
        self.carrinho = {}
        self.estoque = {}
        self.pedidos = []

    def cadastrar_produto(self, id, nome, preco, quantidade):
        # Bug: não valida se o preço é positivo
        self.produtos[id] = {
            'id': id,
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        self.estoque[id] = quantidade
        return True

    def adicionar_ao_carrinho(self, id, quantidade):
        # Bug: não verifica se o produto existe
        produto = self.produtos.get(id)
        if not produto:
            raise ValueError('Produto não encontrado')

        # Bug: não verifica estoque
        qtd_atual = self.carrinho.get(id, 0)
        self.carrinho[id] = qtd_atual + quantidade
        return True

    def calcular_total(self):
        # Bug: não considera desconto
        total = 0
        for id, quantidade in self.carrinho.items():
            produto = self.produtos[id]
            total += produto['preco'] * quantidade
        return total

    def finalizar_compra(self, cartao):
        # Bug: não valida cartão
        total = self.calcular_total()
        
        # Bug: não atualiza estoque
        pedido = {
            'id': int(time.time()),
            'itens': list(self.carrinho.items()),
            'total': total,
            'status': 'aprovado',
            'data': datetime.now()
        }

        self.pedidos.append(pedido)
        self.carrinho.clear()
        return pedido

    def buscar_pedido(self, id):
        # Bug: não valida ID
        return next((p for p in self.pedidos if p['id'] == id), None)

    def atualizar_estoque(self, id, quantidade):
        # Bug: não verifica se quantidade é positiva
        qtd_atual = self.estoque.get(id, 0)
        self.estoque[id] = qtd_atual + quantidade
        return True

    def obter_produtos_disponiveis(self):
        # Bug: retorna produtos sem estoque
        return list(self.produtos.values())

    def aplicar_desconto(self, codigo):
        # Bug: não valida código de desconto
        return {
            'percentual': 10,
            'mensagem': 'Desconto aplicado com sucesso!'
        } 