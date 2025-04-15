Segue abaixo uma apostila completa e robusta para sua aula de Selenium com Python. O material está dividido em capítulos que abordam desde a introdução ao Selenium e a preparação do ambiente, passando pelos principais métodos e casos de uso, até cenários práticos e atividades de fixação. Sinta-se à vontade para ajustar exemplos e atividades conforme o perfil da sua turma.

---

# Apostila: Selenium com Python – Do Básico ao Avançado

## Sumário

1. [Introdução](#introdução)
2. [Configuração do Ambiente](#configuração-do-ambiente)
   - Instalação do Python e do Selenium
   - Drivers de Navegador e WebDriver Manager
3. [Conceitos e Arquitetura do Selenium](#conceitos-e-arquitetura-do-selenium)
   - Componentes do Selenium (IDE, WebDriver, Grid)
   - Vantagens, limitações e casos de uso
4. [Principais Métodos e “Receitas de Bolo”](#principais-métodos-e-receitas-de-bolo)
   - Navegação, localização de elementos, interação e espera
   - Código exemplo: Acessando o Google e realizando uma pesquisa
5. [Cenários Práticos – Atividades Propostas](#cenários-práticos)
   - Cenário 1: Pesquisa no Google e coleta de URLs dos resultados
   - Cenário 2: Coleta de dados de uma página de notícias (exemplo)
   - Cenário 3: Automação de formulário (exemplo de login)
6. [Conclusão e Próximos Passos](#conclusão-e-próximos-passos)

---

## 1. Introdução

O Selenium é uma ferramenta de automação de testes para aplicações web que permite simular a interação de um usuário com o navegador. Em conjunto com o Python, essa ferramenta se torna uma poderosa solução para automatizar desde testes funcionais até a coleta de dados (web scraping). Nesta apostila, você encontrará desde a instalação e configuração do ambiente até exemplos práticos e cenários para fixação do conteúdo.

Alguns dos objetivos do uso do Selenium com Python são:
- **Automação de testes:** Verificar o funcionamento de aplicativos web antes de lançá-los.
- **Web scraping:** Extrair informações de páginas web de forma programática.
- **Automação de tarefas repetitivas:** Simular ações que um usuário faria manualmente, como preencher formulários.

---

## 2. Configuração do Ambiente

### 2.1 Instalação do Python e do Selenium

1. **Instale o Python:**  
   Acesse [python.org/downloads](https://www.python.org/downloads) e faça o download da versão mais recente. Durante a instalação, marque a opção “Add Python to PATH” (ou adicione manualmente a variável de ambiente).

2. **Instale o Selenium:**  
   Abra o terminal ou prompt de comando e execute:
   ```bash
   pip install selenium
   ```

### 2.2 Drivers de Navegador e WebDriver Manager

Para que o Selenium controle um navegador, é necessário ter um driver compatível. Os exemplos abaixo utilizam o Google Chrome, mas o conceito é semelhante para Firefox (geckodriver), Edge, Opera, etc.

1. **Download manual do ChromeDriver:**  
   Faça o download em [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) e coloque-o em uma pasta que esteja no PATH ou na mesma pasta do seu projeto.

2. **Automatizando a gestão do driver:**  
   Utilize o **WebDriver Manager** para que o driver seja baixado automaticamente.
   ```bash
   pip install webdriver-manager
   ```
   Em seu script, use:
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service
   from webdriver_manager.chrome import ChromeDriverManager

   service = Service(ChromeDriverManager().install())
   driver = webdriver.Chrome(service=service)
   ```

> **Dica:** A utilização do WebDriver Manager elimina problemas de incompatibilidade de versão entre navegador e driver.

---

## 3. Conceitos e Arquitetura do Selenium

### 3.1 Componentes do Selenium

- **Selenium IDE:**  
  Uma ferramenta integrada em navegadores (Firefox/Chrome) que permite gravar e reproduzir testes, ideal para quem está começando.

- **Selenium WebDriver:**  
  A API central e moderna, que permite escrever scripts de teste em várias linguagens (como Python, Java, C# etc.) e interagir diretamente com os navegadores.

- **Selenium Grid:**  
  Permite executar testes em paralelo em múltiplos navegadores e sistemas operacionais, o que é útil para testes de compatibilidade.

### 3.2 Vantagens e Casos de Uso

**Vantagens:**
- **Flexibilidade:** Suporta diversos navegadores e linguagens.
- **Automação avançada:** Pode simular ações complexas (cliques, digitação, movimentos do mouse).
- **Integração:** Funciona bem com frameworks de teste como unittest e pytest.

**Casos de Uso:**
- Automatização de testes para garantir a qualidade de aplicações web.
- Coleta de dados para análise de conteúdo e web scraping.
- Execução de tarefas repetitivas em sistemas web (ex: preencher formulários).

---

## 4. Principais Métodos e “Receitas de Bolo”

Nesta seção, veremos os principais métodos do Selenium com exemplos e comentários que servem de “receita de bolo” para cenários comuns.

### 4.1 Navegação e Interação

#### Abrindo uma Página
```python
# Importa a biblioteca e inicializa o driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre o site do Google
driver.get("https://www.google.com")
```

#### Encontrando Elementos

- **find_element:** Encontra o primeiro elemento que corresponde ao seletor.
- **find_elements:** Retorna uma lista de elementos.

Exemplo com busca pelo atributo name:
```python
from selenium.webdriver.common.by import By

# Localiza a caixa de pesquisa pelo atributo "name"
search_box = driver.find_element(by=By.NAME, value="q")
```

#### Interagindo com Elementos

Você pode enviar texto, clicar e limpar elementos:
```python
from selenium.webdriver.common.keys import Keys

# Limpa a caixa de pesquisa, digita o texto e submete
search_box.clear()
search_box.send_keys("Selenium com Python")
search_box.send_keys(Keys.RETURN)
```

#### Esperas Explícitas

É importante aguardar que elementos estejam carregados antes de interagir:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Espera até que um elemento com a classe "g" (resultado do Google) esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "g"))
)
```

#### Fechando o Navegador

```python
driver.quit()
```

### 4.2 Exemplo Completo: Pesquisa no Google

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa o driver usando WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Abre o Google
    driver.get("https://www.google.com")
    
    # Localiza a caixa de pesquisa pelo nome "q"
    search_box = driver.find_element(By.NAME, "q")
    
    # Limpa a caixa, envia o texto e submete (pressiona ENTER)
    search_box.clear()
    search_box.send_keys("Selenium com Python")
    search_box.send_keys(Keys.RETURN)
    
    # Aguarda os resultados aparecerem
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "g"))
    )
    
    # Imprime o título da página e o URL atualizado
    print("Título da Página:", driver.title)
    print("URL Atual:", driver.current_url)
    
    # Opcional: extrair os links dos resultados
    resultados = driver.find_elements(By.XPATH, "//div[@class='g']//a")
    print("Links encontrados:")
    for elemento in resultados:
        href = elemento.get_attribute("href")
        if href:
            print(href)
finally:
    # Encerra a sessão do navegador
    driver.quit()
```

> **Explicação do código:**  
> - O script abre o navegador, acessa o Google, pesquisa “Selenium com Python” e aguarda os resultados (elementos com a classe "g").  
> - Depois, ele imprime o título e a URL atual e ainda extrai links dos resultados.  
> - Por fim, a sessão é finalizada com `driver.quit()`.

---

## 5. Cenários Práticos – Atividades Propostas

### Cenário 1: Pesquisa no Google com Coleta de Dados

**Objetivo:**  
Automatizar a pesquisa no Google e coletar os URLs dos resultados.

**Atividades:**
1. Abra o navegador.
2. Acesse “https://www.google.com”.
3. Realize uma pesquisa (o termo pode ser definido pelo aluno).
4. Aguarde os resultados e extraia, pelo menos, os 5 primeiros links.
5. Armazene os links em um arquivo de texto ou exiba na tela.

**Exemplo de Código:** (base no exemplo acima, com ajuste para salvar os links)
```python
# Continua do exemplo completo, acrescente após a impressão dos links:
with open("resultados.txt", "w", encoding="utf-8") as f:
    for elemento in resultados[:5]:
        href = elemento.get_attribute("href")
        if href:
            f.write(href + "\n")
```

### Cenário 2: Coleta de Dados de uma Página de Notícias

**Objetivo:**  
Acessar uma página de notícias (ex.: "https://www.example-news.com") e coletar os títulos das matérias.

**Atividades:**
1. Abra o navegador e acesse a página de notícias.
2. Utilize métodos para localizar os elementos que contêm os títulos (por exemplo, tags `<h2>` ou classes específicas).
3. Extraia o texto dos títulos e imprima-os ou salve em um arquivo CSV.

**Exemplo de Código:**
```python
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Substitua pela URL real da página de notícias
    driver.get("https://www.example-news.com")
    
    # Supondo que os títulos estejam dentro de tags h2 com a classe "titulo-noticia"
    titulos = driver.find_elements(By.CSS_SELECTOR, "h2.titulo-noticia")
    
    # Coleta e exibe os títulos
    lista_titulos = [titulo.text for titulo in titulos if titulo.text.strip() != ""]
    print("Títulos encontrados:")
    for t in lista_titulos:
        print(t)
    
    # Salva os títulos num arquivo CSV
    with open("titulos_noticias.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Título"])
        for t in lista_titulos:
            writer.writerow([t])
finally:
    driver.quit()
```

### Cenário 3: Automação de Formulário (Exemplo de Login)

**Objetivo:**  
Simular o processo de login em um site de exemplo e verificar se o login foi efetuado com sucesso.

**Atividades:**
1. Acesse um site de exemplo de login (pode ser um site de testes ou ambiente local).
2. Localize os elementos de usuário e senha.
3. Preencha o formulário com dados de teste.
4. Clique no botão de login.
5. Verifique se a autenticação foi bem-sucedida, por exemplo, conferindo a presença de um elemento como “Bem-vindo” ou redirecionamento para uma página específica.

**Exemplo de Código:**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Acessa a página de login de um site de exemplo
    driver.get("https://www.exemplo-login.com")
    
    # Localiza o campo de usuário (exemplo com atributo id="username")
    usuario = driver.find_element(By.ID, "username")
    usuario.clear()
    usuario.send_keys("usuario_teste")
    
    # Localiza o campo de senha (exemplo com atributo id="password")
    senha = driver.find_element(By.ID, "password")
    senha.clear()
    senha.send_keys("senha_teste")
    
    # Localiza o botão de login (por exemplo, com id="btn-login") e clica
    botao_login = driver.find_element(By.ID, "btn-login")
    botao_login.click()
    
    # Aguarda a verificação (exemplo: elemento com texto "Bem-vindo")
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Bem-vindo")
    )
    
    print("Login efetuado com sucesso!")
finally:
    driver.quit()
```

---

## 6. Conclusão e Próximos Passos

Nesta apostila, você aprendeu:
- A importância e os componentes do Selenium.
- Como configurar o ambiente (instalação do Python, Selenium, drivers).
- Os principais métodos para navegação, localização de elementos, interação e gerenciamento de esperas.
- Exemplos práticos que demonstram desde uma simples pesquisa no Google até a coleta de dados e automação de formulários.

### Dicas para Avançar:
- **Estude as locators avançados:** XPath e CSS Selectors podem ser afinados para cenários mais complexos.
- **Integre com frameworks de teste:** Explore o uso do `pytest` ou `unittest` para organizar seus testes de forma modular.
- **Explore o Selenium Grid:** Aprenda a executar testes paralelos em diferentes navegadores ou sistemas.
- **Pratique a manutenção de scripts:** Em automação real, páginas sofrem alterações e scripts precisam ser ajustados.

### Atividades para Fixação:
1. **Exercício 1:** Modifique o exemplo do Google para receber o termo de pesquisa como entrada do usuário via `input()` e salve os primeiros 10 URLs de resultados em um arquivo.
2. **Exercício 2:** Crie um script que acesse um site de cotação (ex.: de ações ou moedas), colete os valores e exiba-os.
3. **Exercício 3:** Implemente um teste automatizado utilizando pytest para validar a funcionalidade de login de um site de testes.

Aprofunde seus conhecimentos experimentando e integrando essas soluções em um projeto maior. Com a prática, você estará apto a desenvolver automações robustas que poupam tempo e garantem a qualidade das aplicações web.

---

## Recursos Adicionais

- [Documentação oficial do Selenium Python](https://selenium-python.readthedocs.io/)
- Cursos e tutoriais no YouTube e plataformas de ensino (Ex.: Udemy, Coursera)
- Comunidades e fóruns (StackOverflow, GitHub, grupos no Telegram/Discord)

Espero que este material seja útil para sua aula e estimule os alunos a explorarem o universo da automação com Selenium e Python. Bom trabalho e bons testes!

---
