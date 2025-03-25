# Testes de carga com problemas intencionais

import pytest
from playwright.sync_api import sync_playwright
import time
import asyncio

# Bug 1: Timeout muito curto
pytest.mark.timeout(5)

# Bug 2: Não limpa dados entre testes
checkout_page = None

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        global checkout_page
        checkout_page = context.new_page()
        yield browser
        browser.close()

# Bug 3: Não considera tempo de resposta
async def checkout_flow():
    await checkout_page.goto('/checkout')
    await checkout_page.click('#add-to-cart')
    await checkout_page.click('#proceed-to-payment')
    await checkout_page.fill('#card-number', '4111111111111111')
    await checkout_page.click('#submit-payment')
    
    # Bug 4: Assertion frágil
    success = await checkout_page.is_visible('#success-message')
    assert success

# Bug 5: Não considera recursos do sistema
@pytest.mark.asyncio
async def test_checkout_concurrent():
    promises = [checkout_flow() for _ in range(100)]
    await asyncio.gather(*promises)

# Bug 6: Métricas incompletas
@pytest.mark.asyncio
async def test_checkout_performance():
    start = time.time()
    await checkout_flow()
    duration = time.time() - start
    
    assert duration < 1.0

# Bug 7: Não considera falhas parciais
@pytest.mark.asyncio
async def test_error_rate():
    errors = 0
    for _ in range(100):
        try:
            await checkout_flow()
        except:
            errors += 1
    
    assert errors < 1

# Bug 8: Não limpa recursos
@pytest.fixture(autouse=True)
def cleanup():
    yield
    if checkout_page:
        checkout_page.close() 