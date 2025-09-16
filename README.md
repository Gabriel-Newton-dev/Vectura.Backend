# FiLL Backend - Sistema de Financiamento Veicular

Sistema de back-end para financiamento veicular com integração à rede Stellar, desenvolvido em Python com FastAPI.

## 🚀 Funcionalidades

- **API RESTful** para gerenciamento de financiamentos
- **Integração Stellar** para operações blockchain
- **Banco de dados SQLite** embutido
- **Documentação automática** (Swagger UI e ReDoc)
- **Smart contracts** simulados para financiamentos


## 🔗 Links do Projeto

## Backend

- **Contrato Inteligente Soroban:** [soroban-smart-contract](https://github.com/Gabriel-Newton-dev/soroban-smart-contract)

- **Repositório:** [Vectura.Backend](https://github.com/Gabriel-Newton-dev/Vectura.Backend)

API em produção: http://vecturabackend-production.up.railway.app/docs

## Frontend

- **Repositório:** [Vectura.Frontend](https://github.com/mateusgreg/Vectura.Frontend)

Aplicação em produção: http://vectura-frontend.vercel.app

## 📋 Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd FiLL.Backend
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
python main.py
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🔄 Fluxo de Financiamento

### 1. Criar Financiamento
```bash
POST /api/financiamento/
```
```json
{
  "valor_veiculo": 50000.0,
  "valor_entrada": 10000.0,
  "valor_financiado": 40000.0,
  "taxa_juros": 2.5,
  "prazo_meses": 60
}
```

### 2. Aprovar na Stellar
```bash
POST /api/stellar/aprovar_financiamento/{id}
```

### 3. Executar Pagamento
```bash
POST /api/stellar/executar_pagamento
```
```json
{
  "financiamento_id": 1,
  "destinatario": "GCKFBEIYTKP4R4M4TZQK7X2Y3Z4X5X6X7X8X9X0X1X2X3X4X5X6X7X8X9X0"
}
```

## 🗄️ Estrutura do Banco de Dados

### Tabela: financiamentos
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | ID único do financiamento |
| valor_veiculo | Float | Valor total do veículo |
| valor_entrada | Float | Valor da entrada |
| valor_financiado | Float | Valor a ser financiado |
| taxa_juros | Float | Taxa de juros mensal |
| prazo_meses | Integer | Prazo em meses |
| status_financiamento | String | Status atual (pendente, aprovado, pago) |
| data_criacao | DateTime | Data de criação |
| aprovado_em | DateTime | Data de aprovação |
| stellar_transaction_id | String | ID da transação Stellar |

## 🌟 Endpoints Principais

### Financiamentos
- `POST /api/financiamento/` - Criar financiamento
- `GET /api/financiamento/{id}` - Obter financiamento
- `PUT /api/financiamento/{id}` - Atualizar status
- `GET /api/financiamento/status/{status}` - Listar por status

### Stellar
- `POST /api/stellar/aprovar_financiamento/{id}` - Aprovar na blockchain
- `POST /api/stellar/executar_pagamento` - Executar pagamento
- `GET /api/stellar/saldo/{conta}` - Verificar saldo
- `GET /api/stellar/status/{id}` - Status na Stellar

## 🧪 Testando a API

Execute o script de teste:
```bash
python test_api.py
```

## 🔧 Configuração

As configurações podem ser ajustadas no arquivo `config.py`:

- **Banco de dados:** SQLite (padrão)
- **Rede Stellar:** Testnet (para desenvolvimento)
- **CORS:** Configurado para desenvolvimento

## 📦 Dependências

- **FastAPI** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **Stellar SDK** - Integração com blockchain
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

## 🚀 Deploy

Para produção, configure:
1. Variáveis de ambiente para chaves Stellar
2. Banco de dados PostgreSQL/MySQL
3. Rede Stellar mainnet
4. Configurações de CORS adequadas

## 📄 Licença

MIT License

## 👥 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request
