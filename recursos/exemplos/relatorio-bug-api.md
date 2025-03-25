# Relatório de Bug: Race Condition na API de Pagamentos

## Informações do Bug
- **ID:** BUG-057
- **Tipo:** Race Condition
- **Severidade:** Alta
- **Prioridade:** Alta
- **Status:** Aberto
- **Reportado por:** Ana Silva
- **Data:** 2024-02-20
- **Versão:** 2.3.4

## Descrição
Race condition identificada na API de pagamentos durante processamento simultâneo de transações para o mesmo cartão. Em cenários de alto volume, algumas transações são processadas duas vezes, gerando cobranças duplicadas.

## Ambiente
- **Produção:** v2.3.4
- **Staging:** v2.3.4-rc1
- **Carga:** 100 req/s

## Reprodução

### Pré-requisitos
- Sistema em ambiente de teste
- Ferramenta de teste de carga (ex: k6)
- Cartão de teste válido

### Passos
1. Configurar 50 usuários virtuais
2. Cada usuário tenta processar pagamento simultaneamente
3. Usar mesmo cartão para todas as transações
4. Executar por 1 minuto

### Script de Teste
```javascript
import http from 'k6/http';

export default function() {
    const payload = {
        cardNumber: '4111111111111111',
        amount: 100,
        currency: 'BRL'
    };

    http.post('https://api.pagamentos/v1/transactions', 
        JSON.stringify(payload),
        { headers: { 'Content-Type': 'application/json' } }
    );
}
```

## Evidências

### Logs de Erro
```
2024-02-20 14:23:15 ERROR TransactionProcessor - Duplicate transaction detected
Transaction ID: 789012
Original Amount: 100.00
Duplicate Amount: 100.00
Card: 411111******1111
```

### Métricas
- **Taxa de Duplicação:** 2.3%
- **Transações Afetadas:** 127 de 5000
- **Tempo Médio:** 234ms

### Impacto no Negócio
- Cobranças duplicadas
- Reclamações de clientes
- Necessidade de estorno manual
- Perda de confiança

## Análise Técnica

### Causa Raiz
O sistema não implementa bloqueio adequado durante a verificação de duplicidade de transações, permitindo que múltiplas requisições sejam processadas simultaneamente para o mesmo cartão.

### Código Problemático
```javascript
async processTransaction(transaction) {
    // Bug: Não há bloqueio aqui
    const existing = await this.findPendingTransaction(
        transaction.cardNumber
    );
    
    if (existing) {
        return existing;
    }
    
    // Janela de race condition
    return await this.createTransaction(transaction);
}
```

### Solução Proposta
```javascript
async processTransaction(transaction) {
    const lockKey = `card:${transaction.cardNumber}`;
    
    return await this.lock.acquire(lockKey, async () => {
        const existing = await this.findPendingTransaction(
            transaction.cardNumber
        );
        
        if (existing) {
            return existing;
        }
        
        return await this.createTransaction(transaction);
    });
}
```

## Recomendações

### Curto Prazo
1. Implementar bloqueio distribuído
2. Adicionar log de auditoria
3. Criar alerta para duplicações

### Longo Prazo
1. Refatorar arquitetura de processamento
2. Implementar sistema de idempotência
3. Melhorar monitoramento

## Workaround Temporário
- Limitar taxa de requisições por cartão
- Monitorar ativamente duplicações
- Processo manual de estorno

## Testes de Verificação
1. Executar teste de carga com bloqueio
2. Verificar logs de auditoria
3. Confirmar ausência de duplicações
4. Validar performance com bloqueio

## Documentação Relacionada
- [Design do Sistema de Pagamentos](docs/payment-system.md)
- [Política de Transações](docs/transaction-policy.md)
- [Procedimento de Estorno](docs/refund-process.md)

## Histórico de Atualizações
| Data | Autor | Descrição |
|------|-------|-----------|
| 2024-02-20 | Ana Silva | Criação do relatório |
| 2024-02-21 | João Santos | Análise técnica |
| 2024-02-22 | Pedro Costa | Solução proposta | 