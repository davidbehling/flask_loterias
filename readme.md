# 🎲 **Flask Loterias**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=flat&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

Aplicação **web/API desenvolvida em Python com Flask** para **consulta, simulação e análise de resultados de loterias**.

O projeto tem foco **educacional e de portfólio**, demonstrando:
- Criação de APIs REST com Flask
- Organização de projeto backend
- Consumo e exposição de dados
- Boas práticas iniciais de arquitetura


## 📌 Visão Geral

Funcionalidades previstas / implementadas:

- 🎯 Consulta de resultados de loterias
- 🔢 Simulação de jogos
- 📊 Análise básica de números sorteados
- 🌐 API REST para consumo externo
- 🧩 Estrutura modular e extensível


## 🏗️ Arquitetura da Aplicação

Fluxo simplificado da aplicação:

```
Request (HTTP)
↓
Routes / Controllers (Flask)
↓
Services (Regras de Negócio)
↓
Repositories / Data Providers
↓
Data Sources (APIs, Banco de Dados, Arquivos)
```

## 📂 Estrutura de Diretórios

```
flask_loterias/
├── public
│   ├── files                           Diretório para armazenar arquivos Excel baixados das loterias
│   └── images                          Diretório para imagens do projeto
├── static
│   ├── css
│   │   ├── base.css                    Estilos base: layout geral, sidebar, responsividade
│   │   ├── select_numbers.css          Estilos para o componente de seleção manual de números (checkboxes estilizados)
│   │   └── table_macros.css            Estilos para tabelas de resultados (bordas, hover, zebra, scroll)
│   ├── script.js                       Função de ordenação de tabelas por coluna (data e números)
│   └── style.css                       Arquivo CSS principal que importa os demais estilos
├── templates
│   ├── aba1.html                       Template da Aba 1: exibição de números sorteados por modalidade
│   ├── aba2.html                       Template da Aba 2: geração de números aleatórios com diferentes métodos
│   ├── aba3.html                       Template da Aba 3: seleção manual de números com checkboxes
│   ├── components
│   │   ├── select_numbers.html         Macro Jinja2 para renderizar grid de checkboxes de seleção de números
│   │   ├── table_drawn_numbers.html    Macro Jinja2 para renderizar tabela de números sorteados
│   │   └── table_macros.html           Macro Jinja2 para renderizar tabela de resultados com acertos e pontuação
│   └── index.html                      Template base com sidebar de navegação e estrutura HTML principal
├── views
│   ├── aba1.py                         Blueprint Flask para Aba 1: endpoint que retorna números sorteados
│   ├── aba2.py                         Blueprint Flask para Aba 2: endpoint que gera números e verifica acertos
│   ├── aba3.py                         Blueprint Flask para Aba 3: endpoint que recebe números selecionados e verifica acertos
│   └── __pycache__                     Cache de bytecode Python das views
│       ├── aba1.cpython-*.pyc
│       ├── aba2.cpython-*.pyc
│       └── aba3.cpython-*.pyc
├── app.py                              Arquivo principal Flask: configura app, registra blueprints e inicia servidor
├── generate.py                         Funções para gerar números (aleatórios, não sorteados, mais/menos frequentes) e verificar acertos
├── global_values.py                    Variáveis globais para armazenar dados carregados (megasena, lotofacil, quina, recorrências)
├── loteria.py                          Funções para download, leitura e processamento de dados das loterias da Caixa
├── readme.txt                          Documentação do projeto: descrição das funcionalidades de cada aba
├── requirements.txt                    Dependências Python do projeto (Flask, pandas, requests)
└── utils.py                            Funções utilitárias (download de dados, geração de números, comparação) - arquivo legado

````

##  🔌 Endpoints (Exemplo)

```http
GET /loterias
GET /loterias/{nome}
GET /simulacao/{loteria}
````

**Exemplo de resposta**

```json
{
  "loteria": "mega_sena",
  "numeros": [4, 15, 23, 42, 48, 59]
}
```

## ⚙️ Tecnologias Utilizadas

**Backend:**
```
- Python 3.8+ - Linguagem de programação
- Flask - Framework web minimalista
- Pandas - Manipulação e análise de dados (DataFrames, leitura de Excel)
- Requests - Requisições HTTP para API da Caixa Econômica Federal
```
**Frontend:**
```
- HTML5 - Estrutura das páginas
- CSS3 - Estilização e responsividade
- CSS Grid e Flexbox para layouts
- Media queries para design responsivo
- JavaScript (Vanilla) - Interatividade (ordenação de tabelas)
- Jinja2 - Template engine do Flask (renderização server-side)
```
**Arquitetura:**
```
- Blueprints (Flask) - Modularização de rotas
- Macros Jinja2 - Componentes reutilizáveis
```
**Fonte de Dados:**
```
- API REST da Caixa Econômica Federal - Dados oficiais das loterias
- Arquivos Excel (.xlsx) - Cache local dos sorteios
```
**Padrões e Práticas:**
```
- MVC Pattern - Separação de responsabilidades (Views, Templates, Lógica)
- RESTful Routes - Organização das rotas
- Responsive Design - Interface adaptável para mobile
```
## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python **3.8+**
* pip

### (Opcional) Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar a aplicação

```bash
python app.py
```

A API ficará disponível em:

```
http://localhost:5000
```


## A aplicação possui 3 abas.

🖥️ **Aba 1:** 

Exibição dos numeros sorteados em uma tabela com as colunas data, Numeros do sorteio e números sorteados, com ordenação crescente e descendente por data e id.

![01 numeros sorteados](https://github.com/davidbehling/flask_loterias/blob/main/public/images/01_numeros_sorteados.png)

🖥️ **Aba 2:**

Geração de números de forma aleatória.

1. Modalidade: Mega Sena, Loto Fácil e Quina

2. Quantidade de números: mínimo e o máximo de numeros selecionados para a modalidade.

- Mega Sena: 6 - 10;
- Loto Fácil:  15 - 20;
- Quina: 5 -15.

3. Tipo de gerados:

- Números aleatórios;
- Números aleatórios não sorteados;
- Números mais sorteados;
- Números menos sorteados.

4. Depois de gerar o numero, é exibido uma tabela com as colunas Data, Numeros do sorteio, Bolas sorteadas, Bolas acertadas, Pontuação.

![02 gerar numeros aleatorios](https://github.com/davidbehling/flask_loterias/blob/main/public/images/02_gerar_numeros_aleatorios.png)

🖥️ **Aba 3:**

É exibido um quadro com numeros para seleção manual de acordo com a modalidade selecionada.

Após elecionar o numero, é exibido uma tabela com as colunas Data, Numeros do sorteio, Bolas sorteadas, Bolas acertadas, Pontuação.

![03 gerar numero manual](https://github.com/davidbehling/flask_loterias/blob/main/public/images/03_gerar_numero_manual.png)
