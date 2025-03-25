# Sistema de Login com bugs intencionais para exercício de testes
class SistemaLogin:
    def __init__(self):
        self.usuarios = {}
        self.tentativas_login = {}
        self.max_tentativas = 3

    def cadastrar_usuario(self, email, senha):
        # Bug: não valida formato do email
        if email in self.usuarios:
            raise ValueError('Usuário já existe')
        self.usuarios[email] = senha
        return True

    def login(self, email, senha):
        # Bug: não verifica se o usuário existe antes de tentar login
        senha_correta = self.usuarios.get(email)
        
        # Bug: não incrementa tentativas de login
        if not senha_correta:
            raise ValueError('Usuário não encontrado')

        # Bug: comparação insegura de senhas
        if senha != senha_correta:
            raise ValueError('Senha incorreta')

        # Bug: não limpa tentativas após login bem-sucedido
        return {
            'token': f'token-fake-{int(time.time())}',
            'email': email
        }

    def verificar_tentativas(self, email):
        # Bug: não inicializa contador de tentativas
        tentativas = self.tentativas_login.get(email, 0)
        return tentativas >= self.max_tentativas

    def redefinir_senha(self, email):
        # Bug: não verifica se o usuário existe
        nova_senha = f'nova-senha-{int(time.time())}'
        self.usuarios[email] = nova_senha
        return nova_senha

    def logout(self, token):
        # Bug: não valida o token
        return True

    def obter_perfil(self, email):
        # Bug: retorna dados sensíveis
        return {
            'email': email,
            'senha': self.usuarios.get(email),
            'ultimo_acesso': datetime.now()
        } 