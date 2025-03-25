const Calculadora = require('./calculadora-bugada');

describe('Calculadora', () => {
    let calc;

    beforeEach(() => {
        calc = new Calculadora();
    });

    describe('operações básicas', () => {
        test('somar deve retornar a soma dos números', () => {
            expect(calc.somar(2, 3)).toBe(5);
            expect(calc.somar(-1, 1)).toBe(0);
        });

        test('subtrair deve retornar a diferença entre os números', () => {
            expect(calc.subtrair(5, 3)).toBe(2);
            expect(calc.subtrair(1, 1)).toBe(0);
        });

        test('multiplicar deve retornar o produto dos números', () => {
            expect(calc.multiplicar(2, 3)).toBe(6);
            expect(calc.multiplicar(-2, 3)).toBe(-6);
        });

        test('dividir deve retornar o quociente dos números', () => {
            expect(calc.dividir(6, 2)).toBe(3);
            expect(calc.dividir(5, 2)).toBe(2.5);
        });
    });

    describe('operações avançadas', () => {
        test('calcularPorcentagem deve retornar o valor correto', () => {
            expect(calc.calcularPorcentagem(100, 10)).toBe(10);
            expect(calc.calcularPorcentagem(200, 5)).toBe(10);
        });
    });

    describe('histórico', () => {
        test('deve adicionar operações ao histórico', () => {
            calc.somar(2, 3);
            const historico = calc.obterHistorico();
            expect(historico).toHaveLength(1);
            expect(historico[0].operacao).toBe('soma');
            expect(historico[0].resultado).toBe(5);
        });
    });

    // Testes que devem falhar (bugs intencionais)
    test('deve falhar ao dividir por zero', () => {
        expect(() => calc.dividir(5, 0)).toThrow();
    });

    test('deve falhar ao somar com valores não numéricos', () => {
        expect(() => calc.somar('a', 3)).toThrow();
    });
}); 