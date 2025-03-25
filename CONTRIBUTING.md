# Guia de Contribuição

## 👋 Bem-vindo!

Primeiramente, obrigado por considerar contribuir para o curso de Testes de Software! Pessoas como você tornam este curso uma ferramenta de aprendizado melhor para todos.

## 📝 Índice

1. [Código de Conduta](#código-de-conduta)
2. [Como Posso Contribuir?](#como-posso-contribuir)
3. [Processo de Pull Request](#processo-de-pull-request)
4. [Padrões de Código](#padrões-de-código)
5. [Reportando Bugs](#reportando-bugs)
6. [Sugerindo Melhorias](#sugerindo-melhorias)

## 📜 Código de Conduta

Este projeto e todos os participantes são regidos pelo [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, espera-se que você mantenha este código.

## 🤝 Como Posso Contribuir?

### 1. Contribuições em Conteúdo

- Correção de erros em materiais existentes
- Adição de novos exemplos práticos
- Melhorias na documentação
- Tradução de conteúdo
- Criação de novos exercícios

### 2. Contribuições em Código

- Correção de bugs em exemplos
- Melhorias em scripts de teste
- Otimização de performance
- Adição de novos casos de teste

### 3. Contribuições em Documentação

- Melhorias no README
- Atualização de guias
- Adição de comentários em código
- Criação de tutoriais

## 🔄 Processo de Pull Request

1. Fork do repositório
2. Clone do seu fork
3. Crie uma branch para sua feature
```bash
git checkout -b feature/nome-da-feature
```

4. Faça suas alterações
5. Commit das alterações
```bash
git commit -m "feat: adiciona novo exemplo de teste de API"
```

6. Push para o seu fork
```bash
git push origin feature/nome-da-feature
```

7. Crie um Pull Request

### Nomenclatura de Commits

Seguimos o padrão Conventional Commits:

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Alteração em documentação
- `style:` Formatação de código
- `refactor:` Refatoração de código
- `test:` Adição/modificação de testes
- `chore:` Alterações em build/configurações

## 💻 Padrões de Código

### JavaScript/TypeScript

```javascript
// Use const/let, nunca var
const exemplo = 'valor';

// Use arrow functions
const soma = (a, b) => a + b;

// Documente funções complexas
/**
 * Calcula média de valores
 * @param {number[]} valores - Array de números
 * @returns {number} Média calculada
 */
const calculaMedia = (valores) => {
    // implementação
};
```

### Testes

```javascript
describe('Módulo de Pagamento', () => {
    beforeEach(() => {
        // setup
    });

    it('deve processar pagamento com sucesso', async () => {
        // teste
    });

    afterEach(() => {
        // cleanup
    });
});
```

## 🐛 Reportando Bugs

### Template de Bug Report

```markdown
**Descrição do Bug**
Uma descrição clara e concisa do bug.

**Para Reproduzir**
Passos para reproduzir o comportamento:
1. Vá para '...'
2. Clique em '....'
3. Veja o erro

**Comportamento Esperado**
Uma descrição clara do que você esperava que acontecesse.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente:**
 - OS: [ex: Windows 10]
 - Node: [ex: 14.17.0]
 - npm: [ex: 6.14.13]
```

## 💡 Sugerindo Melhorias

### Template de Feature Request

```markdown
**Problema Relacionado**
Descrição clara e concisa do problema.

**Solução Desejada**
Descrição clara e concisa do que você quer que aconteça.

**Alternativas Consideradas**
Descrição clara e concisa de soluções alternativas.

**Contexto Adicional**
Qualquer outro contexto sobre a sugestão.
```

## ✅ Checklist antes do PR

- [ ] Testes passando
- [ ] Código documentado
- [ ] Exemplos atualizados
- [ ] Changelog atualizado
- [ ] Versão atualizada

## 📚 Recursos Adicionais

- [Documentação do Jest](https://jestjs.io/)
- [Guia de Testes](docs/testing-guide.md)
- [Boas Práticas](docs/best-practices.md)

## ❓ Dúvidas?

Se você tiver alguma dúvida, não hesite em:

1. Verificar as [Issues](https://github.com/seu-usuario/curso-testes/issues)
2. Criar uma nova issue
3. Entrar em contato via [Discord](link-do-discord)
4. Enviar email para suporte@cursotestes.com

## 🙏 Agradecimentos

Agradecemos a todos que já contribuíram para este projeto! 