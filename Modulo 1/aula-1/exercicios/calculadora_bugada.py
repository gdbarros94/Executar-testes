# Calculadora com bugs intencionais para exercício de testes
class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        # Bug: não valida se os parâmetros são números
        return a + b

    def subtrair(self, a, b):
        # Bug: inverte a ordem da subtração
        return b - a

    def multiplicar(self, a, b):
        # Bug: multiplica pelo mesmo número
        return a * a

    def dividir(self, a, b):
        # Bug: não verifica divisão por zero
        return a / b

    def calcular_porcentagem(self, valor, percentual):
        # Bug: não divide por 100
        return valor * percentual

    def adicionar_ao_historico(self, operacao, resultado):
        # Bug: não valida os parâmetros
        self.historico.append({
            'operacao': operacao,
            'resultado': resultado,
            'data': datetime.now()
        })

    def obter_historico(self):
        # Bug: retorna o histórico em ordem inversa
        return self.historico[::-1] 