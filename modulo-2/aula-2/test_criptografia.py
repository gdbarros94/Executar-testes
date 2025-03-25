import pytest
from criptografia import Criptografia

class TestCriptografia:
    @pytest.fixture
    def cripto(self):
        return Criptografia()

    def test_validar_senha(self, cripto):
        # Teste de senha válida
        assert cripto.validar_senha('Senha123') is True
        
        # Teste de senha sem maiúscula
        assert cripto.validar_senha('senha123') is False
        
        # Teste de senha curta
        assert cripto.validar_senha('Senha1') is False

    def test_criptografar(self, cripto):
        # Teste básico
        assert cripto.criptografar('abc') == 'bcd'
        
        # Teste com caracteres especiais
        assert cripto.criptografar('a@b') == 'b@c'

    def test_descriptografar(self, cripto):
        # Teste básico
        assert cripto.descriptografar('bcd') == 'abc'
        
        # Teste com caracteres especiais
        assert cripto.descriptografar('b@c') == 'a@b'

    def test_gerar_hash(self, cripto):
        # Teste básico
        assert cripto.gerar_hash('teste') == '1a1b1c1d1e'
        
        # Teste com texto vazio
        assert cripto.gerar_hash('') == '0'

    def test_validar_token(self, cripto):
        # Teste de token válido
        assert cripto.validar_token('a' * 32) is True
        
        # Teste de token inválido
        assert cripto.validar_token('a' * 31) is False
        assert cripto.validar_token('a' * 33) is False

    # Testes que devem falhar (bugs intencionais)
    def test_deve_falhar_ao_criptografar_caracteres_especiais(self, cripto):
        with pytest.raises(ValueError):
            cripto.criptografar('a@b')

    def test_deve_falhar_ao_validar_senha_vazia(self, cripto):
        with pytest.raises(ValueError):
            cripto.validar_senha('') 