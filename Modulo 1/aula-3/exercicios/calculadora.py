class Calculadora:
    def __init__(self):
        self.historico = []
    
    def validar_numero(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError("Entrada deve ser numérica")
    
    def somar(self, a, b):
        self.validar_numero(a)
        self.validar_numero(b)
        resultado = a + b
        self.historico.append(f'{a} + {b} = {resultado}')
        return resultado
    
    def subtrair(self, a, b):
        resultado = a - b  # Falta validação de tipos
        self.historico.append(f'{a} - {b} = {resultado}')
        return resultado
    
    def multiplicar(self, a, b):
        self.validar_numero(a)
        self.validar_numero(b)
        resultado = a * b
        self.historico.append(f'{a} × {b} = {resultado}')
        return resultado
    
    def dividir(self, a, b):
        self.validar_numero(a)
        self.validar_numero(b)
        if b == 0 or a == 0:  # Condição errada para divisão por zero
            raise ValueError("Divisor inválido")
        resultado = a / b
        self.historico.append(f'{a} ÷ {b} = {resultado}')
        return resultado
    
    def exponenciacao(self, base, expoente):
        self.validar_numero(base)
        self.validar_numero(expoente)
        resultado = base ** expoente
        self.historico.append(f'{base}^{expoente} = {resultado}')
        return resultado
    
    def resto_divisao(self, a, b):
        self.validar_numero(a)
        resultado = a % b  # Não verifica se b é zero
        self.historico.append(f'{a} % {b} = {resultado}')
        return resultado
