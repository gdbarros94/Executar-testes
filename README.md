# Curso de Testes de Software - Módulo 3: Performance

## 📚 Sobre o Módulo

Este repositório contém materiais e exemplos práticos focados em testes de performance e carga. O módulo aborda conceitos avançados de teste de software, com ênfase em:

- Testes de carga e stress
- Monitoramento de performance
- Análise de resultados
- Documentação de testes
- Relatórios técnicos

## 🎯 Objetivos

- Compreender conceitos de performance testing
- Aprender a usar ferramentas de teste de carga
- Desenvolver habilidades em análise de performance
- Criar documentação técnica de qualidade
- Identificar e resolver problemas de performance

## 📂 Estrutura do Repositório

```
.
├── aula-4/                    # Testes de Carga
│   ├── load-test/            # Exemplos de Testes de Carga
│   │   ├── checkout_test.py  # Teste de carga do checkout
│   │   └── api_test.py       # Teste de carga da API
│   └── recursos/             # Materiais de Apoio
└── recursos/                 # Recursos Gerais
    ├── templates/           # Templates para Documentação
    │   └── caso-teste-template.md
    └── exemplos/            # Exemplos Práticos
        ├── caso-teste-login.md
        ├── relatorio-bug-api.md
        └── relatorio-teste-carga.md
```

## 🛠️ Ferramentas Utilizadas

- **Testes de Carga**: k6, locust
- **Monitoramento**: Grafana
- **Documentação**: Markdown
- **CI/CD**: GitHub Actions
- **Relatórios**: pytest-html
- **Automação**: Playwright, pytest

## 📝 Conteúdo

### 1. Testes de Carga
- Configuração do ambiente
- Scripts de teste
- Métricas e KPIs
- Análise de resultados

### 2. Documentação
- Templates de casos de teste
- Relatórios de bugs
- Relatórios de performance
- Post-mortem de incidentes

### 3. Exemplos Práticos
- Testes de API
- Testes de UI
- Testes de banco de dados
- Análise de performance

## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/curso-testes.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute os testes de carga:
```bash
pytest load-test/checkout_test.py
```

## 📊 Recursos e Templates

### Templates Disponíveis
- [Template de Caso de Teste](recursos/templates/caso-teste-template.md)
- [Template de Relatório de Bug](recursos/exemplos/relatorio-bug-api.md)
- [Template de Relatório de Performance](recursos/exemplos/relatorio-teste-carga.md)

### Exemplos Práticos
- [Caso de Teste de Login](recursos/exemplos/caso-teste-login.md)
- [Relatório de Bug em API](recursos/exemplos/relatorio-bug-api.md)
- [Relatório de Teste de Carga](recursos/exemplos/relatorio-teste-carga.md)

## 📖 Documentação

- [Guia de Contribuição](CONTRIBUTING.md)
- [Código de Conduta](CODE_OF_CONDUCT.md)
- [Licença](LICENSE.md)

## 🎓 Avaliação

Para aprovação no módulo, é necessário:
- Completar os exercícios práticos
- Desenvolver relatórios técnicos
- Participar das discussões
- Apresentar um projeto final

## 👥 Contribuição

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) antes de submeter pull requests.

## 📫 Suporte

- Email: suporte@cursotestes.com
- Discord: [Link para servidor]
- Issues: [GitHub Issues]

## 📅 Atualizações

O módulo é atualizado regularmente com:
- Novos exemplos de testes
- Melhorias nos templates
- Atualizações de ferramentas
- Feedback dos alunos

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE.md). 