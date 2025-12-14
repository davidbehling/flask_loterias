# 🎲 **Flask Loterias**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

Aplicação **web/API desenvolvida em Python com Flask** para **consulta, simulação e análise de resultados de loterias**.

O projeto tem foco **educacional e de portfólio**, demonstrando:
- Criação de APIs REST com Flask
- Organização de projeto backend
- Consumo e exposição de dados
- Boas práticas iniciais de arquitetura


 📌 **Visão Geral**

Funcionalidades previstas / implementadas:

- 🎯 Consulta de resultados de loterias
- 🔢 Simulação de jogos
- 📊 Análise básica de números sorteados
- 🌐 API REST para consumo externo
- 🧩 Estrutura modular e extensível


 🏗️ **Arquitetura da Aplicação**

A aplicação segue uma arquitetura simples e clara:

```

Request (HTTP)
↓
Routes / Controllers (Flask)
↓
Services (Regras de Negócio)
↓
Repositories / Data Providers

```

Essa separação facilita manutenção, testes e evolução do sistema.


 📂 Estrutura de Diretórios

```

flask_loterias/
├── app/                       # Aplicação principal
│   ├── **init**.py            # Inicialização do Flask
│   ├── routes.py              # Definição das rotas/endpoints
│   ├── services.py            # Regras de negócio
│   ├── repository.py          # Acesso e manipulação de dados
│   └── utils.py               # Funções utilitárias
│
├── static/                    # Arquivos estáticos (se aplicável)
│
├── templates/                 # Templates HTML (caso use renderização)
│
├── tests/                     # Testes automatizados (futuro)
│
├── app.py                     # Ponto de entrada da aplicação
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação

````

> A estrutura pode ser facilmente expandida para Blueprints, banco de dados ou autenticação.



 🔌 **Endpoints (Exemplo)**

```http
GET /loterias
GET /loterias/{nome}
GET /simulacao/{loteria}
````

# Exemplo de resposta

```json
{
  "loteria": "mega_sena",
  "numeros": [4, 15, 23, 42, 48, 59]
}
```

 ⚙️ Instalação e Execução

# Pré-requisitos

* Python **3.8+**
* pip

# (Opcional) Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

# Instalar dependências

```bash
pip install -r requirements.txt
```

# Executar a aplicação

```bash
python app.py
```

A API ficará disponível em:

```
http://localhost:5000
```
