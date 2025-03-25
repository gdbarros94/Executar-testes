// Sistema de Criptografia com bugs intencionais para exercícios

class Criptografia {
    // Bug 1: Não valida entrada vazia
    validarSenha(senha) {
        return senha.length >= 8 && /[A-Z]/.test(senha);
    }

    // Bug 2: Não trata caracteres especiais
    criptografar(texto) {
        return texto
            .split('')
            .map(char => String.fromCharCode(char.charCodeAt(0) + 1))
            .join('');
    }

    // Bug 3: Não verifica limites de caracteres
    descriptografar(textoCriptografado) {
        return textoCriptografado
            .split('')
            .map(char => String.fromCharCode(char.charCodeAt(0) - 1))
            .join('');
    }

    // Bug 4: Hash fraco e previsível
    gerarHash(texto) {
        let hash = 0;
        for (let i = 0; i < texto.length; i++) {
            hash += texto.charCodeAt(i);
        }
        return hash.toString(16);
    }

    // Bug 5: Não valida formato do token
    validarToken(token) {
        return token.length === 32;
    }
}

module.exports = Criptografia; 