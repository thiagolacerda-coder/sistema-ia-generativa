# 🤖 Sistema IA Generativa

Projeto desenvolvido em Python que gera dados fictícios de clientes bancários, expõe esses dados via API REST local e utiliza IA generativa para criar mensagens personalizadas de marketing financeiro para cada usuário.

---

## 📋 Sobre o Projeto

O sistema realiza as seguintes etapas:

1. Gera 500 clientes fictícios com dados bancários em formato JSON
2. Converte os dados para CSV organizado com pandas
3. Sobe uma API REST local com FastAPI para consultar e atualizar os dados
4. Consome a API com a biblioteca `requests`
5. Usa IA generativa (via OpenRouter) para gerar mensagens personalizadas no campo `news` de cada usuário

---

## 🗂️ Estrutura do Projeto

```
sistema-bancario-python/
│
├── api.py              # API REST com FastAPI
├── pandas.ipynb        # Notebook com geração de dados, consumo da API e IA
├── data.csv            # Base de dados dos clientes
└── README.md
```

---

## 📦 Bibliotecas Utilizadas

Instale todas as dependências com:

```bash
pip install fastapi uvicorn pandas requests openai
```

| Biblioteca | Uso |
|---|---|
| `pandas` | Leitura, manipulação e exportação do CSV |
| `fastapi` | Criação da API REST local |
| `uvicorn` | Servidor ASGI para rodar o FastAPI |
| `requests` | Consumo da API dentro do notebook |
| `openai` | Integração com modelos de IA via OpenRouter |
| `json` | Manipulação de dados JSON |

---

## 🚀 Como Rodar a API Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/sistema-ia-generativa.git
cd sistema-ia-generativa
```

### 2. Instale as dependências

```bash
pip install fastapi uvicorn pandas requests openai
```

### 3. Ajuste o caminho do CSV no `api.py`

Abra o arquivo `api.py` e altere o caminho na linha do `read_csv`:

```python
df = pd.read_csv(r"C:\caminho\para\seu\data.csv")
```

### 4. Suba o servidor

```bash
uvicorn api:app --reload
```

### 5. Acesse as rotas

| Rota | Método | Descrição |
|---|---|---|
| `http://127.0.0.1:8000/` | GET | Verifica se a API está no ar |
| `http://127.0.0.1:8000/users` | GET | Lista todos os usuários |
| `http://127.0.0.1:8000/users/{id}` | GET | Busca usuário por ID |
| `http://127.0.0.1:8000/users/{id}` | PUT | Atualiza dados do usuário |
| `http://127.0.0.1:8000/docs` | GET | Documentação interativa automática |

---

## 🤖 Integrando IA Generativa (OpenRouter)

O projeto usa o **OpenRouter** para acessar modelos de IA gratuitamente, incluindo o `arcee-ai/trinity-large-preview:free`.

### Como obter sua chave de API gratuita

1. Acesse **[openrouter.ai](https://openrouter.ai)**
2. Crie uma conta ou faça login
3. Vá em **Keys → Create Key**
4. Copie a chave gerada (começa com `sk-or-v1-...`)

### Como usar no projeto

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-SUA_CHAVE_AQUI",
)

def generate_ai_news(user):
    completion = client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        max_tokens=300,
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário. Responda em no máximo 2 frases."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos"
            }
        ]
    )
    return completion.choices[0].message.content
```

> ⚠️ **Nunca suba sua chave de API para o GitHub!**  
> Use variáveis de ambiente ou um arquivo `.env` para protegê-la.

---

## 🔒 Boas Práticas de Segurança

Crie um arquivo `.env` na raiz do projeto:

```
OPENROUTER_API_KEY=sk-or-v1-SUA_CHAVE_AQUI
```

E adicione ao `.gitignore`:

```
.env
__pycache__/
.ipynb_checkpoints/
*.pyc
```

---

## 📊 Estrutura dos Dados

Cada usuário possui os seguintes campos:

```json
{
  "id": 1,
  "name": "Henrique",
  "account": {
    "id": 8721,
    "number": "52272-1",
    "agency": "0005",
    "balance": 7772.08,
    "limit": 2000
  },
  "card": {
    "id": 1,
    "number": "**** **** **** 1362",
    "limit": 15000
  },
  "features": ["discount"],
  "news": []
}
```

---

## 👤 Autor

Desenvolvido como projeto de estudo em Python, pandas, FastAPI e IA generativa.
