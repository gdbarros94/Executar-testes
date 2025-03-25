// Calculadora com bugs intencionais para exercício de testes
class Calculadora {
    constructor() {
        this.historico = [];
    }

    somar(a, b) {
        // Bug: não valida se os parâmetros são números
        return a + b;
    }

    subtrair(a, b) {
        // Bug: inverte a ordem da subtração
        return b - a;
    }

    multiplicar(a, b) {
        // Bug: multiplica pelo mesmo número
        return a * a;
    }

    dividir(a, b) {
        // Bug: não verifica divisão por zero
        return a / b;
    }

    calcularPorcentagem(valor, percentual) {
        // Bug: não divide por 100
        return valor * percentual;
    }

    adicionarAoHistorico(operacao, resultado) {
        // Bug: não valida os parâmetros
        this.historico.push({
            operacao,
            resultado,
            data: new Date()
        });
    }

    obterHistorico() {
        // Bug: retorna o histórico em ordem inversa
        return this.historico.reverse();
    }
}

module.exports = Calculadora; 