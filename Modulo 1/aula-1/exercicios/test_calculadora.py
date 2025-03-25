import pytest
from calculadora_bugada import Calculadora

class TestCalculadora:
    @pytest.fixture
    def calc(self):
        return Calculadora()

    def test_operacoes_basicas_somar(self, calc):
        assert calc.somar(2, 3) == 5
        assert calc.somar(-1, 1) == 0

    def test_operacoes_basicas_subtrair(self, calc):
        assert calc.subtrair(5, 3) == 2
        assert calc.subtrair(1, 1) == 0

    def test_operacoes_basicas_multiplicar(self, calc):
        assert calc.multiplicar(2, 3) == 6
        assert calc.multiplicar(-2, 3) == -6

    def test_operacoes_basicas_dividir(self, calc):
        assert calc.dividir(6, 2) == 3
        assert calc.dividir(5, 2) == 2.5

    def test_operacoes_avancadas_calcular_porcentagem(self, calc):
        assert calc.calcular_porcentagem(100, 10) == 10
        assert calc.calcular_porcentagem(200, 5) == 10

    def test_historico(self, calc):
        calc.somar(2, 3)
        historico = calc.obter_historico()
        assert len(historico) == 1
        assert historico[0]['operacao'] == 'soma'
        assert historico[0]['resultado'] == 5

    # Testes que devem falhar (bugs intencionais)
    def test_deve_falhar_ao_dividir_por_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.dividir(5, 0)

    def test_deve_falhar_ao_somar_com_valores_nao_numericos(self, calc):
        with pytest.raises(TypeError):
            calc.somar('a', 3) 