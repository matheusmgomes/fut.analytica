# Fut.Analytica ⚽

**Scouting Intelligence para o cliente fictício Gol de Placa (Agência de Marketing Esportivo)**

Projeto desenvolvido no bootcamp **Generation Brasil**, squad Fut.Analytica.

O objetivo da solução é substituir a extração manual de dados por um fluxo relacional integrado e automatizado: consumindo dados de campeonatos de futebol via API, tratando-os em Python/Pandas, armazenando-os em banco de dados MySQL relacional com views analíticas e disponibilizando as visões para consumo no Power BI Desktop e interface interativa em Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Relational%20DB-4479A1?style=flat&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboards-F2C811?style=flat&logo=powerbi&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-Em%20desenvolvimento-FF4B4B?style=flat&logo=streamlit&logoColor=white)

---

## 📑 Sumário

- [📌 Status do Projeto](#-status-do-projeto)
- [👥 Arquitetura da Equipe e Fonte de Dados](#-arquitetura-da-equipe-e-fonte-de-dados)
  - [Ligas Masculinas Integradas](#ligas-masculinas-integradas)
  - [Futebol Feminino](#futebol-feminino)
  - [Atenção: calendários e limites do plano gratuito](#atenção-calendários-e-limites-do-plano-gratuito)
- [📂 Estrutura do Repositório](#-estrutura-do-repositório)
- [🚀 Setup e Instalação](#-setup-e-instalação)
  - [1. Clonar o repositório e preparar o ambiente](#1-clonar-o-repositório-e-preparar-o-ambiente)
  - [2. Configuração das variáveis de ambiente (.env)](#2-configuração-das-variáveis-de-ambiente-env)
- [🗄️ Guia de Reprodução no MySQL (Local)](#️-guia-de-reprodução-no-mysql-local)
  - [1️⃣ Futebol Masculino](#1️⃣-futebol-masculino)
  - [2️⃣ Futebol Feminino](#2️⃣-futebol-feminino)
  - [3️⃣ Auditoria e Validação](#3️⃣-auditoria-e-validação)
- [⚙️ Principais Funções (app.py)](#️-principais-funções-apppy)
- [🛠️ Tratamento de Erros](#️-tratamento-de-erros)
- [📊 Dados Extraídos por Time](#-dados-extraídos-por-time)
- [🔮 Próximos Passos](#-próximos-passos)
- [📄 Licença e Créditos](#-licença-e-créditos)

---

## 📌 Status do Projeto

| Status | Entrega |
| :---: | :--- |
| ✅ | Conexão com a API (football-data.org) e autenticação via token (`.env`) |
| ✅ | Extração e tratamento da tabela de classificação (`standings`) por liga (masculina e feminina) |
| ✅ | Tratamento de JSON aninhado para DataFrame Pandas (formato tidy) |
| ✅ | Tratamento de erros de requisição, chaves e temporadas sem dados |
| ✅ | Persistência relacional em banco de dados MySQL via SQLAlchemy / PyMySQL |
| ✅ | Criação de scripts DDL para criação do schema e tabelas fatos |
| ✅ | Compilação de views analíticas no MySQL (Gemas Escondidas, Risco/Consistência e Ligas) |
| ✅ | Scripts de auditoria e validação de carga para bases masculina e feminina |
| ⬜ | Estratégia de upsert por chave (liga + ano) no MySQL |
| ⬜ | Dashboard interativo em Streamlit |
| ⬜ | Finalização dos relatórios no Power BI Desktop |

---

## 👥 Arquitetura da Equipe e Fonte de Dados

O projeto é mantido por uma equipe de **6 integrantes**, cobrindo da camada de ingestão via API/Web Scraping até a modelagem SQL e os dashboards finais.

| Item | Detalhe |
| :--- | :--- |
| **API Base** | [football-data.org](https://www.football-data.org/) (v4) |
| **Endpoint principal** | `GET /v4/competitions/{liga}/standings?season={ano}` |

### Ligas Masculinas Integradas

| Código | Liga |
| :---: | :--- |
| `BSA` | Campeonato Brasileiro Série A |
| `PL` | Premier League (Inglaterra) |
| `PD` | La Liga (Espanha) |

### Futebol Feminino

Dados estruturados das edições do **Brasileirão Feminino (2023 a 2025)**.

### Atenção: calendários e limites do plano gratuito

> Calendários europeus e sul-americanos diferem entre si. Buscas por temporadas não iniciadas ou fora do plano gratuito da API retornam `standings` vazio, o que é tratado automaticamente sem interromper o pipeline.

---

## 📂 Estrutura do Repositório

```plaintext
fut.analytica/
├── sql/
│   ├── 01_setup_database.sql       # Criação do schema fut_analytica_db e tabelas masculinas
│   ├── 02_views_negocio.sql        # Views analíticas (Gemas Escondidas, Risco e Ligas)
│   ├── 03_consultas_validacao.sql  # Queries de auditoria da base masculina
│   ├── 01_setup_feminino.sql       # Criação da tabela fato 'classificacoes_feminino'
│   ├── 02_views_feminino.sql       # Views analíticas do futebol feminino
│   └── 03_validacao_feminino.sql   # Queries de auditoria da base feminina
├── data/                           # Armazenamento de CSVs temporários (não versionado)
├── .env                            # Token da API + credenciais MySQL (NÃO versionado)
├── .gitignore
├── app.py                          # Script ETL das ligas masculinas
├── feminino_etl.py                 # Script ETL do Brasileirão Feminino
├── requirements.txt                # Dependências Python
└── README.md                       # Documentação do projeto
```

---

## 🚀 Setup e Instalação

### 1. Clonar o repositório e preparar o ambiente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fut.analytica.git
cd fut.analytica

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração das variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto contendo a chave da API e as credenciais do MySQL:

```env
FOOTBALL_API_KEY=seu_token_aqui

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=fut_analytica_db
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
```

> Obtenha o token gratuito em [football-data.org](https://www.football-data.org/client/register).

---

## 🗄️ Guia de Reprodução no MySQL (Local)

Execute os passos a seguir no MySQL Workbench e no terminal Python **na ordem indicada**.

### 1️⃣ Futebol Masculino

**Passo 1. Inicializar o banco masculino**

Execute no MySQL o script `sql/01_setup_database.sql` para criar o schema `fut_analytica_db`.

**Passo 2. Executar o ETL masculino**

No terminal, rode o script Python para coletar e carregar os dados na tabela fato `classificacoes`:

```bash
python app.py
```

**Passo 3. Compilar as views masculinas**

Execute no MySQL o script `sql/02_views_negocio.sql` para gerar:

| View | Descrição |
| :--- | :--- |
| `vw_gemas_escondidas` | Clubes de alto apelo/mídia fora do Top 4 |
| `vw_consistencia_clubes` | Estabilidade e desvio padrão de gols (σ) no ciclo de 3 anos |
| `vw_comparativo_ligas` | Média de gols por jogo e volume por liga/temporada |

### 2️⃣ Futebol Feminino

**Passo 1. Preparar a fonte de dados**

Os dados estáticos estão em `data/classificacoes_feminino.json`. O ETL cria a tabela `classificacoes_feminino` automaticamente, caso ela ainda não exista.

**Passo 2. Executar o ETL feminino**

No terminal, rode a carga de dados do Brasileirão Feminino (2023 a 2025):

```bash
python feminino_etl.py
```

O script principal `python app.py` executa as cargas masculina e feminina. O
arquivo `feminino_etl.py` permanece como um atalho para executar somente a
carga feminina.

**Passo 3. Compilar as views femininas**

Execute no MySQL o script `sql/02_views_feminino.sql` para compilar:

| View | Descrição |
| :--- | :--- |
| `vw_feminino_gemas_escondidas` | Clubes de destaque fora das primeiras colocações |
| `vw_feminino_desempenho_mata_mata` | Desempenho das equipes na fase eliminatória |
| `vw_feminino_consistencia_3anos` | Estabilidade de resultados no ciclo de 3 anos |

### 3️⃣ Auditoria e Validação

Rode os scripts no MySQL para verificar a integridade da carga:

```plaintext
sql/03_consultas_validacao.sql
sql/03_validacao_feminino.sql
```

---

## ⚙️ Principais Funções (app.py)

| Função | Responsabilidade |
| :--- | :--- |
| `getRequestFromLeague(league, year)` | Realiza requisição GET à API para uma liga/temporada e retorna o JSON bruto |
| `getTabelaDF(dados)` | Valida `standings`, trata JSONs aninhados e constrói o DataFrame Pandas limpo |
| `saveTabela(df, league, year)` | Exporta CSVs individuais utilizando caminhos absolutos portáveis |
| `conectar_mysql()` | Estabelece a conexão via SQLAlchemy utilizando as credenciais do `.env` |
| `salvar_no_mysql(df, tabela)` | Persiste o DataFrame consolidado no MySQL via `df.to_sql` |
| `consultar_mysql(query)` | Executa queries arbitrárias no banco e retorna os resultados como DataFrame |

---

## 🛠️ Tratamento de Erros

| Cenário | Comportamento |
| :--- | :--- |
| **Falha de requisição HTTP** | Trata retornos com `status != 200` retornando dicionários vazios para evitar a interrupção do loop |
| **`standings` ausente ou vazio** | Retorna DataFrames vazios em cenários de temporadas não iniciadas ou fora do plano da API |
| **Estrutura inesperada de JSON** | Capturado via bloco `try/except (KeyError, IndexError)` em nível de item |

---

## 📊 Dados Extraídos por Time

| Coluna | Descrição |
| :--- | :--- |
| `posicao` | Posição final/atual na tabela |
| `nome_time` | Nome da equipe |
| `total_jogos` | Total de partidas disputadas |
| `vitorias` / `empates` / `derrotas` | Métricas de desempenho |
| `gols_pro` / `gols_contra` | Métricas de ataque e defesa |
| `saldo_de_gols` | Saldo absoluto de gols |
| `pontos` | Pontuação acumulada |

---

## 🔮 Próximos Passos

1. Substituir `if_exists='replace'` por estratégia de **upsert por chave** (liga + ano).
2. Construir a **interface visual interativa em Streamlit**.
3. Publicar os **dashboards analíticos finalizados no Power BI Desktop**.

---

## 📄 Licença e Créditos

Projeto desenvolvido no bootcamp **Generation Brasil**, squad **Fut.Analytica**, para o cliente fictício **Gol de Placa**.

Dados fornecidos por [football-data.org](https://www.football-data.org/).
