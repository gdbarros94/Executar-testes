# Caso de Teste: Login de Usuário

## Informações Básicas
- **ID:** CT-001
- **Título:** Login de Usuário com Credenciais Válidas
- **Módulo:** Autenticação
- **Prioridade:** Alta
- **Tipo:** Funcional
- **Automação:** Automatizado

## Requisitos Relacionados
- **REQ-001:** Sistema deve permitir login com email e senha
- **REQ-002:** Sistema deve validar formato de email
- **REQ-003:** Sistema deve bloquear conta após 3 tentativas inválidas

## Objetivo
Verificar se o sistema permite login de usuário com credenciais válidas e redireciona para a página inicial após autenticação bem-sucedida.

## Pré-condições
1. Usuário cadastrado no sistema
2. Conta de usuário ativa
3. Sistema acessível via navegador

## Dados de Teste
### Entrada
```json
{
    "email": "usuario.teste@empresa.com",
    "senha": "Senha@123"
}
```

### Saída Esperada
```json
{
    "status": "success",
    "data": {
        "userId": "123456",
        "nome": "Usuário Teste",
        "token": "jwt-token-example"
    }
}
```

## Passos
1. Acessar a página de login do sistema
   - Resultado esperado: Página carrega com campos de email e senha
   - Critério de aceite: Formulário visível e campos editáveis

2. Preencher campo de email
   - Resultado esperado: Campo aceita entrada de texto
   - Critério de aceite: Formato de email validado

3. Preencher campo de senha
   - Resultado esperado: Campo mascara caracteres
   - Critério de aceite: Senha não visível

4. Clicar no botão "Entrar"
   - Resultado esperado: Sistema processa credenciais
   - Critério de aceite: Feedback visual durante processamento

5. Verificar redirecionamento
   - Resultado esperado: Usuário redirecionado para dashboard
   - Critério de aceite: URL da dashboard correta

## Pós-condições
1. Usuário logado no sistema
2. Token de autenticação armazenado
3. Sessão ativa

## Cenários Alternativos
### Cenário 1: Senha Incorreta
1. Inserir senha errada
2. Clicar em "Entrar"
- Resultado esperado: Mensagem "Credenciais inválidas"

### Cenário 2: Email Inválido
1. Inserir email mal formatado
2. Clicar em "Entrar"
- Resultado esperado: Validação impede envio

## Critérios de Aceitação
- [ ] Login bem-sucedido em menos de 2 segundos
- [ ] Mensagens de erro claras e em português
- [ ] Tentativas de login registradas no log

## Observações
- Teste deve ser executado em diferentes navegadores
- Verificar comportamento com cache limpo
- Testar em diferentes resoluções de tela

## Histórico de Execução
| Data | Executor | Resultado | Observações |
|------|----------|-----------|-------------|
| 2024-02-20 | João Silva | OK | Chrome 120 |
| 2024-02-20 | Maria Santos | OK | Firefox 115 |

## Anexos
- [Link para vídeo da execução](videos/login-test.mp4)
- [Link para logs de teste](logs/login-test.log)
- [Screenshots dos resultados](images/login-test/) 