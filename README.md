

Gemini

Conversa

Spark
Beta
Nova conversa
Pesquisar conversas
Imagens
Vídeos
Biblioteca
Gems
Novo notebook
Projeto final - FUT.ANALYTICA
ATA DE REUNIÃO DIÁRIA -
Todos os notebooks
Benefícios Educacionais e Ferramentas Gratuitas
Caminho de Carreira em Dados
Otimização de Treino para Hipertrofia e Performance
Sistema de Controle de Estoque PWA
Portabilidade de Containers
Coloração Castanho Escuro
Java VS Code: Erros de Execução e Soluções
Método C.O.R.E. para Escrita
Concurso Público RJ: Nível Superior
Dockerizando Frontend e Dashboard
Qualificações TI para Banco
Hidratação e Emagrecimento: Guia Prático
README.md Generation for Fut.Analytica
Extração de Dados com Python e IA
Perguntas de Negócio para Análise Esportiva
Duas Curiosidades Marcantes e Únicas
Agulha para Linha Anne Brilho
Explorando API de Dados Esportivos
Cobrança Incorreta: Bar do Zé
Plano de Rota e Visita Cliente
Atribuir Tarefa a Si Mesmo no Trello
Formatação de README para GitHub
Configurar API Key em Arquivo .env
README.md Pronto para GitHub
Power BI: Domínio Próprio e Compartilhamento
Perfil Gupy: Engenharia e Dados
Receber Alertas de E-mail Host1
Refinando Alertas de Eventos Tech
Envio de RG para Diploma
Métodos de Amostragem Estatística Explicados
Diâmetro e Circunferência: Entendendo Bolos
Prompt para Foto Profissional LinkedIn
Excel para Analistas: Do Básico ao Pleno
Criação de Textos para Plaquinhas de PDV
Criatividade para Promoção de Caneca
Conversa com o Gemini
seja capaz de criar um .md desse projeto. Pronto para copiar e colar no github. # Fut.Analytica ⚽ (Scouting Intelligence)



Aplicação desenvolvida para o cliente fictício **Gol de Placa** (Agência de Marketing Esportivo) que automatiza a substituição de extrações manuais de dados por um fluxo relacional integrado.



---



## 📂 Estrutura dos Scripts SQL



A pasta `sql/` contém a modelagem DDL do banco e as visões de negócio preparadas para consumo no **Power BI Desktop**:



```text

fut.analytica/

└── sql/

    ├── 01_setup_database.sql        # Criação do schema fut_analytica_db

    ├── 02_views_negocio.sql         # Views analíticas (Gemas Escondidas, Risco e Ligas)

    ├── 03_consultas_validacao.sql    # Queries de auditoria e validação de carga

    ├── 01_setup_feminino.sql        # Criação da tabela fato 'classificacoes_feminino'

    ├── 02_views_feminino.sql        # Views analíticas para a modalidade feminina

    └── 03_validacao_feminino.sql    # Queries de auditoria da base feminina 🗄️ Guia de Reprodução no MySQL (Local)

Para configurar o banco de dados no seu MySQL Workbench local, execute os scripts na ordem abaixo:

sql/01_setup_database.sql: Inicializa o banco de dados fut_analytica_db.

python app.py: Alimenta a tabela fato classificacoes com os dados das ligas masculinas.

sql/02_views_negocio.sql: Compila as Views analíticas:

vw_gemas_escondidas: Mapeamento de clubes de alta mídia fora do Top 4.

vw_consistencia_clubes: Análise de estabilidade e risco ($\sigma$) no ciclo de 3 anos.

vw_comparativo_ligas: Média de gols por jogo e volume por liga/temporada.

sql/01_setup_feminino.sql: Inicializa a estrutura da tabela classificacoes_feminino.

python feminino_etl.py: Alimenta a tabela fato com os dados do Brasileirão Feminino (2023–2025).

sql/02_views_feminino.sql: Compila as Views analíticas do futebol feminino (vw_feminino_gemas_escondidas, vw_feminino_desempenho_mata_mata, vw_feminino_consistencia_3anos).

sql/03_consultas_validacao.sql e sql/03_validacao_feminino.sql: Validação final de auditoria.

Projeto desenvolvido no bootcamp Generation Brasil, squad Fut.Analytica.

📊 Views Analíticas & Regras de Negócio
As visões relacionais foram modeladas no MySQL para rápido consumo no Power BI Desktop:

⚽ Futebol Masculino
vw_gemas_escondidas: Mapeamento de clubes de alto apelo/mídia posicionados fora do Top 4.

vw_consistencia_clubes: Análise de estabilidade e risco (σ) no ciclo contínuo de 3 anos.

vw_comparativo_ligas: Média de gols por jogo, volume competitivo e métricas comparativas por liga/temporada.

♀️ Futebol Feminino
vw_feminino_gemas_escondidas: Mapeamento de destaques e oportunidades na categoria feminina.

vw_feminino_desempenho_mata_mata: Métricas detalhadas de performance em fases eliminatórias.

vw_feminino_consistencia_3anos: Análise do histórico e regularidade das equipes no ciclo 2023–2025.

🗄️ Guia de Reprodução no MySQL (Local)
Para configurar o banco de dados e executar o pipeline completo no seu MySQL Workbench local, siga os passos na ordem indicada:

Inicializar o Banco de Dados Masculino
Executar o script SQL para criar o schema e estruturas base:

Bash
sql/01_setup_database.sql
Executar ETL Masculino
Alimentar a tabela fato classificacoes com os dados das ligas masculinas:

Bash
python app.py
Compilar Views Analíticas Masculinas
Criar as regras de negócio e visões relacionais:

Bash
sql/02_views_negocio.sql
Inicializar o Schema Feminino
Criar a estrutura da tabela fato classificacoes_feminino:

Bash
sql/01_setup_feminino.sql
Executar ETL Feminino
Alimentar a tabela fato com dados do Brasileirão Feminino (2023–2025):

Bash
python feminino_etl.py
Compilar Views Analíticas Femininas
Criar as visões de inteligência para o futebol feminino:

Bash
sql/02_views_feminino.sql
Validação e Auditoria
Executar os scripts de auditoria para garantir a integridade da carga de dados:

Bash
sql/03_consultas_validacao.sql
sql/03_validacao_feminino.sql
🛠️ Tecnologias Utilizadas
Linguagem & ETL: Python 3.x

Banco de Dados Relacional: MySQL / MySQL Workbench

Visualização & Dashboard: Power BI Desktop

Versionamento & Governança: Git & GitHub

👥 Equipe & Créditos
Projeto desenvolvido como entrega prática do bootcamp Generation Brasil pela squad Fut.Analytica.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("FILE_CREATED: README.md")


```text?code_stdout&code_event_index=1
FILE_CREATED: README.md

Seu arquivo README.md foi gerado com sucesso!

Ícone do app MD
README
 MD 
Aberto
Abaixo está o conteúdo completo formatado em Markdown, pronto para você copiar e colar diretamente no seu arquivo README.md no repositório do GitHub:

Markdown
# Fut.Analytica ⚽ (Scouting Intelligence)

> **Projeto desenvolvido no bootcamp Generation Brasil — Squad Fut.Analytica**

![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-CC292B?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)

---

## 📌 Sobre o Projeto

O **Fut.Analytica** é uma solução de *Scouting Intelligence* desenvolvida para o cliente fictício **Gol de Placa** (Agência de Marketing Esportivo). 

A aplicação automatiza e substitui processos manuais e fragmentados de extração de dados por um **fluxo relacional integrado e automatizado**, permitindo análises preditivas, métricas de consistência e identificação de oportunidades no futebol masculino e feminino.

---

## 📂 Estrutura do Repositório

```text
fut.analytica/
├── sql/
│   ├── 01_setup_database.sql         # Criação do schema fut_analytica_db e tabelas masculinas
│   ├── 02_views_negocio.sql          # Views analíticas (Gemas Escondidas, Risco e Ligas)
│   ├── 03_consultas_validacao.sql    # Queries de auditoria e validação de carga masculina
│   ├── 01_setup_feminino.sql        # Criação da tabela fato 'classificacoes_feminino'
│   ├── 02_views_feminino.sql        # Views analíticas para a modalidade feminina
│   └── 03_validacao_feminino.sql    # Queries de auditoria da base feminina
├── app.py                            # ETL para carga de dados das ligas masculinas
├── feminino_etl.py                   # ETL para carga do Brasileirão Feminino (2023–2025)
└── README.md                         # Documentação do projeto
📊 Views Analíticas & Regras de Negócio
As visões relacionais foram modeladas no MySQL para rápido consumo no Power BI Desktop:

⚽ Futebol Masculino
vw_gemas_escondidas: Mapeamento de clubes de alto apelo/mídia posicionados fora do Top 4.

vw_consistencia_clubes: Análise de estabilidade e risco (σ) no ciclo contínuo de 3 anos.

vw_comparativo_ligas: Média de gols por jogo, volume competitivo e métricas comparativas por liga/temporada.

♀️ Futebol Feminino
vw_feminino_gemas_escondidas: Mapeamento de destaques e oportunidades na categoria feminina.

vw_feminino_desempenho_mata_mata: Métricas detalhadas de performance em fases eliminatórias.

vw_feminino_consistencia_3anos: Análise do histórico e regularidade das equipes no ciclo 2023–2025.

🗄️ Guia de Reprodução no MySQL (Local)
Para configurar o banco de dados e executar o pipeline completo no seu MySQL Workbench local, siga os passos na ordem indicada:

Inicializar o Banco de Dados Masculino
Executar o script SQL para criar o schema e estruturas base:

Bash
sql/01_setup_database.sql
Executar ETL Masculino
Alimentar a tabela fato classificacoes com os dados das ligas masculinas:

Bash
python app.py
Compilar Views Analíticas Masculinas
Criar as regras de negócio e visões relacionais:

Bash
sql/02_views_negocio.sql
Inicializar o Schema Feminino
Criar a estrutura da tabela fato classificacoes_feminino:

Bash
sql/01_setup_feminino.sql
Executar ETL Feminino
Alimentar a tabela fato com dados do Brasileirão Feminino (2023–2025):

Bash
python feminino_etl.py
Compilar Views Analíticas Femininas
Criar as visões de inteligência para o futebol feminino:

Bash
sql/02_views_feminino.sql
Validação e Auditoria
Executar os scripts de auditoria para garantir a integridade da carga de dados:

Bash
sql/03_consultas_validacao.sql
sql/03_validacao_feminino.sql
🛠️ Tecnologias Utilizadas
Linguagem & ETL: Python 3.x

Banco de Dados Relacional: MySQL / MySQL Workbench

Visualização & Dashboard: Power BI Desktop

Versionamento & Governança: Git & GitHub

👥 Equipe & Créditos
Projeto desenvolvido como entrega prática do bootcamp Generation Brasil pela squad Fut.Analytica.

esse readme.md é excelente. Mas eu preciso respeitar a estrutura desse readme a seguir. eles usam .env Inclua isso e mantenha as intruções importantes que tem nesse readme: # Fut.Analytica ⚽



Nesse projeto, nossa equipe trabalçhou para a aplicação de extração, tratamento e visualização de dados de futebol, desenvolvida como projeto do bootcamp **Generation Brasil**.



O objetivo é consumir dados históricos de campeonatos de futebol via API, tratá-los com Python/Pandas, exibi-los em um dashboard interativo com Streamlit e exportar um CSV limpo para consumo no **Power BI**.



## Status do projeto



Em desenvolvimento, módulo de extração e tratamento de dados (Python).



- [x] Conexão com a API e autenticação via token

- [x] Extração da tabela de classificação (standings) por liga

- [x] Tratamento de JSON aninhado → DataFrame Pandas

- [x] Tratamento de erros (requisição falha, temporada/liga sem dados)

- [x] Parametrização dinâmica de liga e temporada

- [x] Consolidação de todos os dados em um único CSV (formato tidy, com colunas `liga`, `ano`, `data_extracao`)

- [x] Persistência em banco de dados MySQL via SQLAlchemy

- [ ] Estratégia de upsert no MySQL (evitar sobrescrita total ou duplicação, em decisão)

- [ ] Interface Streamlit

- [ ] Gráficos exploratórios (Plotly/Pandas)

- [ ] Exportação final para consumo no Power BI



## Arquitetura da equipe



O time é composto por 6 integrantes. Desde a camada de extração de dados via API e toda a lógica em Python (este repositório/módulo) até a exportação final para o Dashboard no **Power BI**.



## Fonte de dados



- **API:** [football-data.org](https://www.football-data.org/) (v4)

- **Endpoint principal:** `GET /v4/competitions/{liga}/standings?season={ano}`

- **Ligas cobertas atualmente:**

  | Código | Liga |

  |---|---|

  | `BSA` | Campeonato Brasileiro Série A |

  | `PL`  | Premier League (Inglaterra) |

  | `PD`  | La Liga (Espanha) |



> **Atenção:** o calendário de ligas europeias não coincide com o calendário brasileiro (ano civil). Buscas por temporadas que ainda não começaram, ou fora da cobertura do plano gratuito da API, podem retornar `standings` vazio. O código trata esse cenário sem quebrar a execução (ver seção [Tratamento de erros](#-tratamento-de-erros)).



## Estrutura do projeto



```

fut.analytica/

├── app.py              # Script principal de extração, tratamento e persistência

├── data/                # CSVs consolidados gerados (não versionado o conteúdo, apenas a pasta)

├── .env                 # Token da API + credenciais MySQL (NÃO versionado)

├── .gitignore

├── requirements.txt

└── README.md

```



## Setup e instalação



1. Clone o repositório e crie um ambiente virtual:

   ```bash

   python -m venv venv

   source venv/bin/activate  # Linux/Mac

   ```



2. Instale as dependências:

   ```bash

   pip install -r requirements.txt

   ```



3. Crie um arquivo `.env` na raiz do projeto com sua chave da API e as credenciais do MySQL:

   ```

   FOOTBALL_API_KEY=seu_token_aqui



   MYSQL_HOST=localhost

   MYSQL_PORT=3306

   MYSQL_DB=fut_analytica_db

   MYSQL_USER=root

   MYSQL_PASSWORD=sua_senha

   ```

   > Obtenha seu token gratuito em [football-data.org](https://www.football-data.org/client/register). As variáveis de MySQL têm valores padrão (`localhost`, `3306`, `root`, senha vazia) caso não sejam definidas, mas isso é pensado apenas para ambiente local de desenvolvimento.



4. Execute o script:

   ```bash

   python app.py

   ```



## Principais funções (`app.py`)



| Função | Responsabilidade |

|---|---|

| `getRequestFromLeague(league, year)` | Faz a requisição GET à API para uma liga/temporada específica e retorna o JSON bruto. Trata falhas de requisição (status != 200) retornando um dicionário vazio. |

| `getTabelaDF(dados)` | Recebe o JSON bruto, valida a existência de `standings`, extrai os dados de cada time via loop e retorna um DataFrame Pandas limpo. Trata `KeyError`/`IndexError` de estrutura inesperada. |

| `saveTabela(df, league, year)` | Salva o DataFrame de uma liga/temporada em CSV individual, usando caminho absoluto baseado na localização do script (portável entre máquinas). |

| `conectar_mysql()` | Monta a engine de conexão SQLAlchemy com o MySQL a partir das credenciais do `.env`. |

| `salvar_no_mysql(df, tabela)` | Persiste o DataFrame consolidado na tabela `classificacoes` do MySQL via `df.to_sql`. |

| `consultar_mysql(query)` | Executa uma query SQL arbitrária no banco e retorna o resultado como DataFrame, usado hoje para validar a carga (contagem de registros). |



O fluxo principal do script: para cada combinação de **ano** × **liga**, busca os dados na API, trata e junta todos os DataFrames em um único consolidado (formato tidy, com colunas `liga`, `ano` e `data_extracao`), salva esse consolidado em CSV com timestamp no nome, e por fim persiste o mesmo DataFrame no MySQL.



## Tratamento de erros



O pipeline foi desenhado para **nunca quebrar a execução** diante de dados ausentes ou inesperados, tratando três camadas de falha:



1. **Falha na requisição HTTP** (token inválido, rate limit, indisponibilidade) → `getRequestFromLeague` captura o status de erro e retorna dicionário vazio, sem interromper o loop de ligas/temporadas.

2. **`standings` vazio ou ausente** (temporada não iniciada, calendário europeu x brasileiro divergente, cobertura fora do plano gratuito) → validado no início de `getTabelaDF`, retornando um DataFrame vazio de forma segura.

3. **Estrutura de JSON inesperada** (chaves ausentes dentro de `table`) → capturado via `try/except (KeyError, IndexError)`, evitando que uma mudança na API quebre o script inteiro.



## Dados extraídos por time



| Coluna | Descrição |

|---|---|

| `posicao` | Posição na tabela |

| `nome_time` | Nome do time |

| `total_jogos` | Jogos disputados |

| `vitorias` / `empates` / `derrotas` | Resultados |

| `gols_pro` / `gols_contra` | Gols marcados/sofridos |

| `saldo_de_gols` | Saldo de gols |

| `pontos` | Pontuação total |



## Persistência em banco de dados (MySQL)



Além do CSV consolidado, o DataFrame final é gravado em uma tabela MySQL (`classificacoes`) via SQLAlchemy + PyMySQL. Isso permite que outras partes do time consultem os dados diretamente via SQL, sem depender de arquivos.



> **Decisão de arquitetura em aberto:** hoje a gravação usa `if_exists='replace'`, o que apaga e recria a tabela inteira a cada execução, inclusive dados de ligas/temporadas que não fazem parte do run atual. Como a maioria das temporadas cobertas (2023, 2024) já está encerrada e não muda, e apenas a temporada corrente (2025) pode ter dados novos a cada rodada, a estratégia planejada é migrar para um **upsert por chave** (`liga` + `ano`): apagar apenas as linhas da combinação sendo reprocessada antes de inserir os dados novos, preservando o restante do histórico já carregado.



## Próximos passos



- Implementar estratégia de upsert no MySQL (substituir `if_exists='replace'` por exclusão seletiva + inserção, por `liga`/`ano`)

- Construir interface interativa em Streamlit (seletor de liga e temporada)

- Criar visualizações exploratórias (saldo de gols, eficiência ofensiva/defensiva, distribuição de vitórias/empates/derrotas)

- Exportação final do CSV tratado para consumo pela equipe de Power BI



---

*Projeto desenvolvido no bootcamp Generation Brasil, squad Fut.Analytica, para o cliente fictício Gol de Placa.* o meu objetivo é mais acrescentar os scripts mysql e ensinar a executa-los. brevemente.

🚀 Setup e Instalação
1. Clonar o Repositório e Preparar o Ambiente
Bash
# Clone o repositório
git clone [https://github.com/seu-usuario/fut.analytica.git](https://github.com/seu-usuario/fut.analytica.git)
cd fut.analytica

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
2. Configuração das Variáveis de Ambiente (.env)
Crie um arquivo .env na raiz do projeto com o seu token da API e as credenciais de acesso ao seu MySQL local:

Snippet de código
FOOTBALL_API_KEY=seu_token_aqui

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=fut_analytica_db
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
Obtain your free token at football-data.org.

🗄️ Guia de Execução & Reprodução no MySQL Local
Siga a ordem dos passos abaixo no MySQL Workbench (ou cliente SQL de sua preferência) e terminal Python para estruturar o banco e rodar os pipelines:

1️⃣ Futebol Masculino (Setup, ETL e Views)
Criar o Banco e Estrutura Masculina:

Execute no MySQL o script sql/01_setup_database.sql para inicializar o schema fut_analytica_db.

Executar ETL Masculino (Python):

No terminal, execute o script para coletar os dados da API e gravar na tabela fato classificacoes:

Bash
python app.py
Compilar Views Analíticas Masculinas:

Execute no MySQL o script sql/02_views_negocio.sql para compilar:

vw_gemas_escondidas: Clubes de alto apelo/mídia fora do Top 4.

vw_consistencia_clubes: Análise de estabilidade e risco (σ) no ciclo de 3 anos.

vw_comparativo_ligas: Média de gols por jogo e volume competitivo por liga/temporada.

2️⃣ Futebol Feminino (Setup, ETL e Views)
Criar Estrutura Feminina:

Execute no MySQL o script sql/01_setup_feminino.sql para criar a tabela classificacoes_feminino.

Executar ETL Feminino (Python):

No terminal, rode a carga de dados do Brasileirão Feminino (2023–2025):

Bash
python feminino_etl.py
Compilar Views Analíticas Femininas:

Execute no MySQL o script sql/02_views_feminino.sql para compilar vw_feminino_gemas_escondidas, vw_feminino_desempenho_mata_mata e vw_feminino_consistencia_3anos.

3️⃣ Auditoria e Validação
Validação Final:

Execute os scripts de auditoria para verificar a integridade e contagem de registros das tabelas fato e visões:

Bash
sql/03_consultas_validacao.sql
sql/03_validacao_feminino.sql
⚙️ Principais Funções (app.py)
Função	Responsabilidade
getRequestFromLeague(league, year)	Realiza requisições GET à API para uma liga/temporada específica e retorna o JSON bruto.
getTabelaDF(dados)	Valida standings, trata JSONs aninhados e constrói o DataFrame Pandas tidy.
saveTabela(df, league, year)	Exporta CSVs individuais com caminhos portáveis baseados no diretório do script.
conectar_mysql()	Estabelece a conexão via SQLAlchemy utilizando as credenciais definidas no .env.
salvar_no_mysql(df, tabela)	Persiste o DataFrame na tabela MySQL via df.to_sql.
consultar_mysql(query)	Executa consultas SQL arbitrárias no banco e retorna os resultados como DataFrame.
🛠️ Tratamento de Erros no Pipeline
O pipeline foi projetado para resiliência total:

Falha de Requisição HTTP: Captura status != 200 e retorna dicionário vazio sem parar o loop.

Dados Ausentes / Standings Vazio: Retorna DataFrames vazios de maneira segura para ligas sem dados na API.

Estrutura de JSON Inesperada: Tratado via try/except (KeyError, IndexError) em nível de registro.

📊 Dados Extraídos por Time
Coluna	Descrição
posicao	Posição final/atual na tabela
nome_time	Nome da equipe
total_jogos	Total de partidas disputadas
vitorias / empates / derrotas	Desempenho detalhado
gols_pro / gols_contra	Métricas de ataques e defesas
saldo_de_gols	Saldo absoluto de gols
pontos	Pontuação acumulada
🔮 Próximos Passos
Implementar estratégia de Upsert por Chave (liga + ano) no MySQL para substituir o if_exists='replace'.

Desenvolver a interface visual interativa em Streamlit.

Finalizar a integração e publicação dos Dashboards no Power BI Desktop.

Projeto desenvolvido no bootcamp Generation Brasil, squad Fut.Analytica, para o cliente fictício Gol de Placa.
"""

with open("README_FINAL.md", "w", encoding="utf-8") as f:
f.write(full_readme)

print("FILE_CREATED: README_FINAL.md")


```text?code_stdout&code_event_index=1
FILE_CREATED: README_FINAL.md

O arquivo README.md foi reestruturado unindo todas as diretrizes solicitadas:

Mantém rigorosamente as instruções do modelo enviado (uso de .env, setup com venv, tratamento de erros, funções do app.py, fonte de dados e próximos passos).

Acrescenta os scripts SQL, a nova estrutura de pastas (sql/) e o guia passo a passo para execução do MySQL (masculino, feminino e auditoria).

Ícone do app MD
README_FINAL
 MD 
Aberto
Aqui está o código pronto para você copiar e colar no seu projeto do GitHub:

Markdown
# Fut.Analytica ⚽

Aplicação de extração, tratamento, modelagem relacional e visualização de dados de futebol, desenvolvida para o cliente fictício **Gol de Placa** (Agência de Marketing Esportivo) como projeto do bootcamp **Generation Brasil**.

O objetivo do projeto é substituir processos manuais de extração por um **fluxo relacional integrado e automatizado**: consumindo dados via API, tratando-os em Python/Pandas, estruturando em banco MySQL relacional com views analíticas e disponibilizando para o **Power BI Desktop** e interface interativa em **Streamlit**.

---

## Status do projeto

Em desenvolvimento e evolução contínua da arquitetura de dados e modelagem analítica:

- [x] Conexão com a API e autenticação via token (`.env`)
- [x] Extração da tabela de classificação (standings) por liga (masculina e feminina)
- [x] Tratamento de JSON aninhado → DataFrame Pandas (formato tidy)
- [x] Tratamento robusto de erros (requisição falha, temporada/liga sem dados)
- [x] Parametrização dinâmica de liga e temporada
- [x] Persistência relacional em banco MySQL via SQLAlchemy/PyMySQL
- [x] Criação da modelagem DDL (tabelas fato para ligas masculinas e `classificacoes_feminino`)
- [x] Construção de **Views Analíticas** no MySQL (Gemas Escondidas, Risco/Consistência e Ligas)
- [x] Queries de auditoria e validação de carga (masculino e feminino)
- [ ] Estratégia de upsert no MySQL (evitar sobrescrita total ou duplicação)
- [ ] Interface visual interativa em Streamlit
- [ ] Visualização final dos dashboards analíticos no Power BI

---

## Arquitetura da equipe

O time **Fut.Analytica** é composto por 6 integrantes, cobrindo todo o ciclo de engenharia e análise de dados: desde a ingestão da API, tratamento e modelagem relacional no MySQL, até a construção das visões de *Scouting Intelligence* e dashboards no **Power BI**.

---

## Fonte de dados

- **API Base:** [football-data.org](https://www.football-data.org/) (v4)
- **Endpoint Principal:** `GET /v4/competitions/{liga}/standings?season={ano}`
- **Ligas Masculinas Integradas:**
  | Código | Liga |
  |---|---|
  | `BSA` | Campeonato Brasileiro Série A |
  | `PL`  | Premier League (Inglaterra) |
  | `PD`  | La Liga (Espanha) |
- **Futebol Feminino:** Cobertura das edições do Brasileirão Feminino (2023–2025).
---

## Estrutura do projeto

```text
fut.analytica/
├── sql/
│   ├── 01_setup_database.sql         # Criação do schema fut_analytica_db e tabelas masculinas
│   ├── 02_views_negocio.sql          # Views analíticas (Gemas Escondidas, Risco e Ligas)
│   ├── 03_consultas_validacao.sql    # Queries de auditoria e validação de carga masculina
│   ├── 01_setup_feminino.sql        # Criação da tabela fato 'classificacoes_feminino'
│   ├── 02_views_feminino.sql        # Views analíticas para a modalidade feminina
│   └── 03_validacao_feminino.sql    # Queries de auditoria da base feminina
├── data/                             # CSVs consolidados gerados (não versionado)
├── .env                              # API Key + Credenciais MySQL (NÃO versionado)
├── .gitignore
├── app.py                            # Script de ETL das ligas masculinas e persistência MySQL
├── feminino_etl.py                   # Script de ETL do Brasileirão Feminino
├── requirements.txt
└── README.md                         # Documentação do projeto
Setup e instalação
1. Clonar o Repositório e Preparar o Ambiente
Bash
# Clone o repositório
git clone [https://github.com/seu-usuario/fut.analytica.git](https://github.com/seu-usuario/fut.analytica.git)
cd fut.analytica

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
2. Configuração das Variáveis de Ambiente (.env)
Crie um arquivo .env na raiz do projeto com o seu token da API e as credenciais de acesso ao seu MySQL local:

Snippet de código
FOOTBALL_API_KEY=seu_token_aqui

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=fut_analytica_db
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
Obtenha seu token gratuito em football-data.org. As variáveis de MySQL têm valores padrão (localhost, 3306, root, senha vazia) caso não sejam definidas, mas isso é pensado apenas para ambiente local de desenvolvimento.

🗄️ Guia de Reprodução no MySQL (Local)
Siga a ordem dos passos abaixo no MySQL Workbench (ou cliente SQL de sua preferência) e terminal Python para estruturar o banco e rodar os pipelines:

1️⃣ Futebol Masculino (Setup, ETL e Views)
Criar o Banco e Estrutura Masculina:

Execute no MySQL o script sql/01_setup_database.sql para inicializar o schema fut_analytica_db.

Executar ETL Masculino (Python):

No terminal, execute o script para coletar os dados da API e gravar na tabela fato classificacoes:

Bash
python app.py
Compilar Views Analíticas Masculinas:

Execute no MySQL o script sql/02_views_negocio.sql para compilar:

vw_gemas_escondidas: Mapeamento de clubes de alta mídia posicionados fora do Top 4.

vw_consistencia_clubes: Análise de estabilidade e risco (σ) no ciclo de 3 anos.

vw_comparativo_ligas: Média de gols por jogo e volume competitivo por liga/temporada.

2️⃣ Futebol Feminino (Setup, ETL e Views)
Criar Estrutura Feminina:

Execute no MySQL o script sql/01_setup_feminino.sql para criar a tabela classificacoes_feminino.

Executar ETL Feminino (Python):

No terminal, rode a carga de dados do Brasileirão Feminino (2023–2025):

Bash
python feminino_etl.py
Compilar Views Analíticas Femininas:

Execute no MySQL o script sql/02_views_feminino.sql para compilar vw_feminino_gemas_escondidas, vw_feminino_desempenho_mata_mata e vw_feminino_consistencia_3anos.

3️⃣ Auditoria e Validação
Validação Final:

Execute os scripts de auditoria para verificar a integridade e contagem de registros das tabelas fato e visões:

Bash
sql/03_consultas_validacao.sql
sql/03_validacao_feminino.sql
Principais funções (app.py)
Função	Responsabilidade
getRequestFromLeague(league, year)	Faz a requisição GET à API para uma liga/temporada específica e retorna o JSON bruto. Trata falhas de requisição (status != 200) retornando um dicionário vazio.
getTabelaDF(dados)	Recebe o JSON bruto, valida a existência de standings, extrai os dados de cada time via loop e retorna um DataFrame Pandas limpo. Trata KeyError/IndexError de estrutura inesperada.
saveTabela(df, league, year)	Salva o DataFrame de uma liga/temporada em CSV individual, usando caminho absoluto baseado na localização do script (portável entre máquinas).
conectar_mysql()	Monta a engine de conexão SQLAlchemy com o MySQL a partir das credenciais do .env.
salvar_no_mysql(df, tabela)	Persiste o DataFrame consolidado na tabela classificacoes do MySQL via df.to_sql.
consultar_mysql(query)	Executa uma query SQL arbitrária no banco e retorna o resultado como DataFrame, usado hoje para validar a carga (contagem de registros).
O fluxo principal do script: para cada combinação de ano × liga, busca os dados na API, trata e junta todos os DataFrames em um único consolidado (formato tidy, com colunas liga, ano e data_extracao), salva esse consolidado em CSV com timestamp no nome, e por fim persiste o mesmo DataFrame no MySQL.

Tratamento de erros
O pipeline foi desenhado para nunca quebrar a execução diante de dados ausentes ou inesperados, tratando três camadas de falha:

Falha na requisição HTTP (token inválido, rate limit, indisponibilidade) → getRequestFromLeague captura o status de erro e retorna dicionário vazio, sem interromper o loop de ligas/temporadas.

standings vazio ou ausente (temporada não iniciada, calendário europeu x brasileiro divergente, cobertura fora do plano gratuito) → validado no início de getTabelaDF, retornando um DataFrame vazio de forma segura.

Estrutura de JSON inesperada (chaves ausentes dentro de table) → capturado via try/except (KeyError, IndexError), evitando que uma mudança na API quebre o script inteiro.

Dados extraídos por time
Coluna	Descrição
posicao	Posição na tabela
nome_time	Nome do time
total_jogos	Jogos disputados
vitorias / empates / derrotas	Resultados
gols_pro / gols_contra	Gols marcados/sofridos
saldo_de_gols	Saldo de gols
pontos	Pontuação total
Persistência em banco de dados (MySQL)
Além do CSV consolidado, o DataFrame final é gravado em uma tabela MySQL (classificacoes) via SQLAlchemy + PyMySQL. Isso permite que outras partes do time consultem os dados diretamente via SQL, sem depender de arquivos.

Decisão de arquitetura em aberto: hoje a gravação usa if_exists='replace', o que apaga e recria a tabela inteira a cada execução, inclusive dados de ligas/temporadas que não fazem parte do run atual. Como a maioria das temporadas cobertas (2023, 2024) já está encerrada e não muda, e apenas a temporada corrente (2025) pode ter dados novos a cada rodada, a estratégia planejada é migrar para um upsert por chave (liga + ano): apagar apenas as linhas da combinação sendo reprocessada antes de inserir os dados novos, preservando o restante do histórico já carregado.

Próximos passos
Implementar estratégia de upsert no MySQL (substituir if_exists='replace' por exclusão seletiva + inserção, por liga/ano)

Construir interface interativa em Streamlit (seletor de liga e temporada)

Criar visualizações exploratórias (saldo de gols, eficiência ofensiva/defensiva, distribuição de vitórias/empates/derrotas)

Exportação final do CSV tratado para consumo pela equipe de Power BI

Projeto desenvolvido no bootcamp Generation Brasil, squad Fut.Analytica, para o cliente fictício Gol de Placa.




O Gemini é uma IA e pode cometer erros.


# Fut.Analytica ⚽ (Scouting Intelligence)

Aplicação de extração, tratamento, modelagem relacional e visualização de dados de futebol, desenvolvida para o cliente fictício **Gol de Placa** (Agência de Marketing Esportivo) como projeto do bootcamp **Generation Brasil**.

O objetivo do projeto é substituir processos manuais de extração por um **fluxo relacional integrado e automatizado**: consumindo dados via API, tratando-os em Python/Pandas, estruturando em banco MySQL relacional com views analíticas e disponibilizando para o **Power BI Desktop** e interface interativa em **Streamlit**.

---

## 📌 Status do Projeto

Em desenvolvimento e evolução contínua da arquitetura de dados e modelagem analítica:

- [x] Conexão com a API e autenticação via token (`.env`)
- [x] Extração da tabela de classificação (standings) por liga (masculina e feminina)
- [x] Tratamento de JSON aninhado → DataFrame Pandas (formato tidy)
- [x] Tratamento robusto de erros (requisição falha, temporada/liga sem dados)
- [x] Parametrização dinâmica de liga e temporada
- [x] Persistência relacional em banco MySQL via SQLAlchemy/PyMySQL
- [x] Criação da modelagem DDL (tabelas fato para ligas masculinas e `classificacoes_feminino`)
- [x] Construção de **Views Analíticas** no MySQL (Gemas Escondidas, Risco/Consistência e Ligas)
- [x] Queries de auditoria e validação de carga (masculino e feminino)
- [ ] Estratégia de upsert no MySQL (evitar sobrescrita total ou duplicação)
- [ ] Interface visual interativa em Streamlit
- [ ] Visualização final dos dashboards analíticos no Power BI

---

## 👥 Arquitetura da Equipe

O time **Fut.Analytica** é composto por 6 integrantes, cobrindo todo o ciclo de engenharia e análise de dados: desde a ingestão da API, tratamento e modelagem relacional no MySQL, até a construção das visões de *Scouting Intelligence* e dashboards no **Power BI**.

---

## 🌐 Fonte de Dados & Cobertura

- **API Base:** [football-data.org](https://www.football-data.org/) (v4)
- **Endpoint Principal:** `GET /v4/competitions/{liga}/standings?season={ano}`
- **Ligas Masculinas Integradas:**
  | Código | Liga |
  |---|---|
  | `BSA` | Campeonato Brasileiro Série A |
  | `PL`  | Premier League (Inglaterra) |
  | `PD`  | La Liga (Espanha) |
- **Futebol Feminino:** Cobertura das edições do Brasileirão Feminino (2023–2025).

> **Atenção:** O calendário europeu e o brasileiro divergem. Buscas por temporadas não iniciadas ou fora do plano gratuito da API podem retornar `standings` vazio. O código trata essa variação sem interromper a execução.

---

## 📂 Estrutura do Repositório

```text
fut.analytica/
├── sql/
│   ├── 01_setup_database.sql         # Criação do schema fut_analytica_db e tabelas masculinas
│   ├── 02_views_negocio.sql          # Views analíticas (Gemas Escondidas, Risco e Ligas)
│   ├── 03_consultas_validacao.sql    # Queries de auditoria e validação de carga masculina
│   ├── 01_setup_feminino.sql        # Criação da tabela fato 'classificacoes_feminino'
│   ├── 02_views_feminino.sql        # Views analíticas para a modalidade feminina
│   └── 03_validacao_feminino.sql    # Queries de auditoria da base feminina
├── data/                             # CSVs consolidados gerados (não versionado)
├── .env                              # API Key + Credenciais MySQL (NÃO versionado)
├── .gitignore
├── app.py                            # Script de ETL das ligas masculinas e persistência MySQL
├── feminino_etl.py                   # Script de ETL do Brasileirão Feminino
├── requirements.txt
└── README.md                         # Documentação do projeto
```

---

## 🚀 Setup e Instalação

### 1. Clonar o Repositório e Preparar o Ambiente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fut.analytica.git
cd fut.analytica

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração das Variáveis de Ambiente (`.env`)

Crie um arquivo `.env` na raiz do projeto com o seu token da API e as credenciais de acesso ao seu MySQL local:

```env
FOOTBALL_API_KEY=seu_token_aqui

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=fut_analytica_db
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
```

> Obtain your free token at [football-data.org](https://www.football-data.org/client/register).

---

## 🗄️ Guia de Execução & Reprodução no MySQL Local

Siga a ordem dos passos abaixo no **MySQL Workbench** (ou cliente SQL de sua preferência) e terminal Python para estruturar o banco e rodar os pipelines:

### 1️⃣ Futebol Masculino (Setup, ETL e Views)
1. **Criar o Banco e Estrutura Masculina:**  
   Execute no MySQL o script `sql/01_setup_database.sql` para inicializar o schema `fut_analytica_db`.
2. **Executar ETL Masculino (Python):**  
   No terminal, execute o script para coletar os dados da API e gravar na tabela fato `classificacoes`:
   ```bash
   python app.py
   ```
3. **Compilar Views Analíticas Masculinas:**  
   Execute no MySQL o script `sql/02_views_negocio.sql` para compilar:
   * `vw_gemas_escondidas`: Clubes de alto apelo/mídia fora do Top 4.
   * `vw_consistencia_clubes`: Análise de estabilidade e risco ($\sigma$) no ciclo de 3 anos.
   * `vw_comparativo_ligas`: Média de gols por jogo e volume competitivo por liga/temporada.

### 2️⃣ Futebol Feminino (Setup, ETL e Views)
4. **Criar Estrutura Feminina:**  
   Execute no MySQL o script `sql/01_setup_feminino.sql` para criar a tabela `classificacoes_feminino`.
5. **Executar ETL Feminino (Python):**  
   No terminal, rode a carga de dados do Brasileirão Feminino (2023–2025):
   ```bash
   python feminino_etl.py
   ```
6. **Compilar Views Analíticas Femininas:**  
   Execute no MySQL o script `sql/02_views_feminino.sql` para compilar `vw_feminino_gemas_escondidas`, `vw_feminino_desempenho_mata_mata` e `vw_feminino_consistencia_3anos`.

### 3️⃣ Auditoria e Validação
7. **Validação Final:**  
   Execute os scripts de auditoria para verificar a integridade e contagem de registros das tabelas fato e visões:
   ```bash
   sql/03_consultas_validacao.sql
   sql/03_validacao_feminino.sql
   ```

---

## ⚙️ Principais Funções (`app.py`)

| Função | Responsabilidade |
|---|---|
| `getRequestFromLeague(league, year)` | Realiza requisições GET à API para uma liga/temporada específica e retorna o JSON bruto. |
| `getTabelaDF(dados)` | Valida `standings`, trata JSONs aninhados e constrói o DataFrame Pandas tidy. |
| `saveTabela(df, league, year)` | Exporta CSVs individuais com caminhos portáveis baseados no diretório do script. |
| `conectar_mysql()` | Estabelece a conexão via SQLAlchemy utilizando as credenciais definidas no `.env`. |
| `salvar_no_mysql(df, tabela)` | Persiste o DataFrame na tabela MySQL via `df.to_sql`. |
| `consultar_mysql(query)` | Executa consultas SQL arbitrárias no banco e retorna os resultados como DataFrame. |

---

## 🛠️ Tratamento de Erros no Pipeline

O pipeline foi projetado para **resiliência total**:
1. **Falha de Requisição HTTP:** Captura status `!= 200` e retorna dicionário vazio sem parar o loop.
2. **Dados Ausentes / Standings Vazio:** Retorna DataFrames vazios de maneira segura para ligas sem dados na API.
3. **Estrutura de JSON Inesperada:** Tratado via `try/except (KeyError, IndexError)` em nível de registro.

---

## 📊 Dados Extraídos por Time

| Coluna | Descrição |
|---|---|
| `posicao` | Posição final/atual na tabela |
| `nome_time` | Nome da equipe |
| `total_jogos` | Total de partidas disputadas |
| `vitorias` / `empates` / `derrotas` | Desempenho detalhado |
| `gols_pro` / `gols_contra` | Métricas de ataques e defesas |
| `saldo_de_gols` | Saldo absoluto de gols |
| `pontos` | Pontuação acumulada |

---

## 🔮 Próximos Passos

- Implementar estratégia de **Upsert por Chave** (`liga` + `ano`) no MySQL para substituir o `if_exists='replace'`.
- Desenvolver a interface visual interativa em **Streamlit**.
- Finalizar a integração e publicação dos Dashboards no **Power BI Desktop**.

---
*Projeto desenvolvido no bootcamp Generation Brasil, squad Fut.Analytica, para o cliente fictício Gol de Placa.*
README_FINAL.md
Exibindo README_FINAL.md.