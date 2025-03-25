# Sistema de Gerenciamento de Produtos com bugs intencionais para exercícios

class GerenciadorProdutos:
    def __init__(self):
        self.produtos = {}

    # Bug 1: Não valida preço negativo
    def cadastrar_produto(self, id, nome, preco, estoque):
        self.produtos[id] = {
            'nome': nome,
            'preco': preco,
            'estoque': estoque
        }
        return True

    # Bug 2: Não verifica se produto existe
    def buscar_produto(self, id):
        return self.produtos.get(id)

    # Bug 3: Não atualiza estoque corretamente
    def atualizar_estoque(self, id, quantidade):
        produto = self.produtos.get(id)
        produto['estoque'] = quantidade
        return True

    # Bug 4: Lista produtos sem estoque
    def listar_produtos(self):
        return list(self.produtos.values())

    # Bug 5: Não valida dados de entrada
    def atualizar_produto(self, id, dados):
        produto = self.produtos.get(id)
        produto.update(dados)
        return True 