// Testes de carga com problemas intencionais

const { test, expect } = require('@playwright/test');

// Bug 1: Timeout muito curto
test.setTimeout(5000);

// Bug 2: Não limpa dados entre testes
let checkoutPage;

test.beforeAll(async ({ browser }) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    checkoutPage = page;
});

// Bug 3: Não considera tempo de resposta
async function checkoutFlow() {
    await checkoutPage.goto('/checkout');
    await checkoutPage.click('#add-to-cart');
    await checkoutPage.click('#proceed-to-payment');
    await checkoutPage.fill('#card-number', '4111111111111111');
    await checkoutPage.click('#submit-payment');
    
    // Bug 4: Assertion frágil
    const success = await checkoutPage.isVisible('#success-message');
    expect(success).toBeTruthy();
}

// Bug 5: Não considera recursos do sistema
test('deve processar 100 checkouts simultâneos', async () => {
    const promises = Array(100).fill(checkoutFlow());
    await Promise.all(promises);
});

// Bug 6: Métricas incompletas
test('deve completar checkout em menos de 1 segundo', async () => {
    const start = Date.now();
    await checkoutFlow();
    const duration = Date.now() - start;
    
    expect(duration).toBeLessThan(1000);
});

// Bug 7: Não considera falhas parciais
test('taxa de erro deve ser menor que 1%', async () => {
    let errors = 0;
    for (let i = 0; i < 100; i++) {
        try {
            await checkoutFlow();
        } catch {
            errors++;
        }
    }
    
    expect(errors).toBeLessThan(1);
});

// Bug 8: Não limpa recursos
test.afterAll(async () => {
    await checkoutPage.close();
}); 