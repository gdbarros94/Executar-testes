# Sistema de Criptografia com bugs intencionais para exercícios

class Criptografia:
    # Bug 1: Não valida entrada vazia
    def validar_senha(self, senha):
        return len(senha) >= 8 and any(c.isupper() for c in senha)

    # Bug 2: Não trata caracteres especiais
    def criptografar(self, texto):
        return ''.join(chr(ord(char) + 1) for char in texto)

    # Bug 3: Não verifica limites de caracteres
    def descriptografar(self, texto_criptografado):
        return ''.join(chr(ord(char) - 1) for char in texto_criptografado)

    # Bug 4: Hash fraco e previsível
    def gerar_hash(self, texto):
        return hex(sum(ord(c) for c in texto))[2:]

    # Bug 5: Não valida formato do token
    def validar_token(self, token):
        return len(token) == 32 