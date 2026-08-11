# Fut.Analytica ⚽

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
*Projeto desenvolvido no bootcamp Generation Brasil, squad Fut.Analytica, para o cliente fictício Gol de Placa.*
