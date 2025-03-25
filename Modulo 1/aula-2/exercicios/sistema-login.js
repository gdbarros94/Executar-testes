// Sistema de Login com bugs intencionais para exercício de testes
class SistemaLogin {
    constructor() {
        this.usuarios = new Map();
        this.tentativasLogin = new Map();
        this.maxTentativas = 3;
    }

    cadastrarUsuario(email, senha) {
        // Bug: não valida formato do email
        if (this.usuarios.has(email)) {
            throw new Error('Usuário já existe');
        }
        this.usuarios.set(email, senha);
        return true;
    }

    login(email, senha) {
        // Bug: não verifica se o usuário existe antes de tentar login
        const senhaCorreta = this.usuarios.get(email);
        
        // Bug: não incrementa tentativas de login
        if (!senhaCorreta) {
            throw new Error('Usuário não encontrado');
        }

        // Bug: comparação insegura de senhas
        if (senha !== senhaCorreta) {
            throw new Error('Senha incorreta');
        }

        // Bug: não limpa tentativas após login bem-sucedido
        return {
            token: 'token-fake-' + Date.now(),
            email: email
        };
    }

    verificarTentativas(email) {
        // Bug: não inicializa contador de tentativas
        const tentativas = this.tentativasLogin.get(email) || 0;
        return tentativas >= this.maxTentativas;
    }

    redefinirSenha(email) {
        // Bug: não verifica se o usuário existe
        const novaSenha = 'nova-senha-' + Date.now();
        this.usuarios.set(email, novaSenha);
        return novaSenha;
    }

    logout(token) {
        // Bug: não valida o token
        return true;
    }

    obterPerfil(email) {
        // Bug: retorna dados sensíveis
        return {
            email: email,
            senha: this.usuarios.get(email),
            ultimoAcesso: new Date()
        };
    }
}

module.exports = SistemaLogin; 