# 1- Importação das bibliotecas necessárias
import os # Biblioteca para interagir com o sistema operacional
import requests # Biblioteca para fazer requisições HTTP
import json # Biblioteca para trabalhar com dados em formato JSON
from pathlib import Path # Biblioteca para manipulação de caminhos de arquivos e diretórios
import pandas as pd #Biblioteca Pandas para DataFrames e limpeza de dados
from dotenv import load_dotenv # Biblioteca para carregar variáveis de ambiente de um arquivo .env
from datetime import datetime # Biblioteca para trabalhar com datas e horas
from sqlalchemy import create_engine, text # Biblioteca para criar uma conexão com o banco de dados
import time

# 2 - Carregar as variaveis do ambiente
load_dotenv()

ANOS = ["2025", "2024", "2023"]
LIGAS = {
    "Brasil - Brasileirão Série A": "BSA",
    "Inglaterra - Premier League": "PL",
    "Espanha - La Liga": "PD",
}
COLUNAS_FEMININO = [
    "Ano", "Fase", "Clube", "Partidas", "Vitorias", "Empates",
    "Derrotas", "Pontos", "Gols_Feitos", "Gols_Sofridos",
]
DDL_CLASSIFICACOES_FEMININO = """
    CREATE TABLE IF NOT EXISTS classificacoes_feminino (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Ano INT NOT NULL,
        Fase VARCHAR(50) NOT NULL,
        Clube VARCHAR(100) NOT NULL,
        Partidas INT NOT NULL,
        Vitorias INT NOT NULL,
        Empates INT NOT NULL,
        Derrotas INT NOT NULL,
        Pontos INT NOT NULL,
        Gols_Feitos INT NOT NULL,
        Gols_Sofridos INT NOT NULL,
        Saldo_Gols INT NOT NULL,
        `Aproveitamento_%` DECIMAL(5,2) NOT NULL,
        data_extracao DATETIME NOT NULL,
        INDEX idx_ano_fase (Ano, Fase),
        INDEX idx_clube (Clube)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

# Marcas fornecedoras dos clubes participantes do Brasileirão Série A de 2025.
# Os nomes alternativos correspondem aos retornados pela API football-data.org.
MARCAS_FORNECEDORAS_2025 = {
    "Atlético-MG": "Adidas",
    "Bahia": "Puma",
    "Botafogo": "Reebok",
    "Ceará": "Marcas próprias",
    "Corinthians": "Nike",
    "Cruzeiro": "Adidas",
    "Flamengo": "Adidas",
    "Fluminense": "Umbro",
    "Fortaleza": "Volt",
    "Grêmio": "Umbro",
    "Internacional": "Adidas",
    "Juventude": "Marcas próprias",
    "Mirassol": "Athleta",
    "Palmeiras": "Puma",
    "Red Bull Bragantino": "Puma",
    "Santos": "Umbro",
    "São Paulo": "New Balance",
    "Sport": "Umbro",
    "Vasco": "Kappa",
    "Vitória": "Volt",
}
# Nomes alternativos dos clubes para normalização com a API football-data.org.
NOMES_CLUBES_API = {
    "CA Mineiro": "Atlético-MG",
    "Atlético Mineiro": "Atlético-MG",
    "Atlético Mineiro SAF": "Atlético-MG",
    "EC Bahia": "Bahia",
    "Botafogo FR": "Botafogo",
    "Ceará SC": "Ceará",
    "SC Corinthians Paulista": "Corinthians",
    "Cruzeiro EC": "Cruzeiro",
    "Cruzeiro SAF": "Cruzeiro",
    "CR Flamengo": "Flamengo",
    "Fluminense FC": "Fluminense",
    "Fortaleza EC": "Fortaleza",
    "Fortaleza EC SAF": "Fortaleza",
    "Grêmio FBPA": "Grêmio",
    "SC Internacional": "Internacional",
    "EC Juventude": "Juventude",
    "Mirassol FC": "Mirassol",
    "SE Palmeiras": "Palmeiras",
    "RB Bragantino": "Red Bull Bragantino",
    "Red Bull Bragantino": "Red Bull Bragantino",
    "Santos FC": "Santos",
    "São Paulo FC": "São Paulo",
    "SC Recife": "Sport",
    "Sport Club do Recife": "Sport",
    "Sport Recife": "Sport",
    "Vasco da Gama": "Vasco",
    "CR Vasco da Gama": "Vasco",
    "EC Vitória": "Vitória",
}

# 3 - Funções para coletar dados da API e processar os dados
def getRequestFromLeague(league: str, year: str) -> dict:
    """Busca a classificação de uma liga na API football-data.org."""
    response = requests.get(
        f"https://api.football-data.org/v4/competitions/{league}/standings",
        headers={"X-Auth-Token": os.getenv("FOOTBALL_API_KEY", "")},
        params={"season": year},
        timeout=30,
    )
    if response.status_code == 200:
        return response.json()

    print(f"Erro na requisição da liga {league} ({response.status_code}).")
    return {}

# 4 - Funções para processar os dados e salvar no MySQL
def getTabelaDF(dados: dict) -> pd.DataFrame:
    if not dados or not dados.get("standings"):
        return pd.DataFrame()

    try:
        tabela_posicoes = dados["standings"][0]["table"]
        return pd.DataFrame([
            {
                "posicao": time["position"],
                "nome_time": time["team"]["name"],
                "total_jogos": time["playedGames"],
                "vitorias": time["won"],
                "empates": time["draw"],
                "derrotas": time["lost"],
                "gols_pro": time["goalsFor"],
                "gols_contra": time["goalsAgainst"],
                "saldo_de_gols": time["goalDifference"],
                "pontos": time["points"],
            }
            for time in tabela_posicoes
        ])
    except (KeyError, IndexError) as erro:
        print(f"Erro de estrutura ao mapear JSON: {erro}")
        return pd.DataFrame()


def adicionar_marcas_fornecedoras(df: pd.DataFrame) -> pd.DataFrame:
    resultado = df.copy()
    resultado["marca_fornecedora"] = pd.NA

    filtro_brasileirao_2025 = (
        (resultado["liga"] == "Brasil - Brasileirão Série A")
        & (resultado["ano"].astype(str) == "2025")
    )
    clubes_normalizados = resultado.loc[
        filtro_brasileirao_2025, "nome_time"
    ].replace(NOMES_CLUBES_API)
    resultado.loc[filtro_brasileirao_2025, "marca_fornecedora"] = (
        clubes_normalizados.map(MARCAS_FORNECEDORAS_2025)
    )
    return resultado


def adicionar_indice_oportunidade(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula a oportunidade de prospecção para os clubes da Série A 2025."""
    resultado = df.copy()
    resultado["indice_oportunidade"] = pd.NA

    filtro_brasileirao_2025 = (
        (resultado["liga"] == "Brasil - Brasileirão Série A")
        & (resultado["ano"].astype(str) == "2025")
        & resultado["marca_fornecedora"].notna()
    )
    marcas_gigantes = ["Adidas", "Umbro", "Puma", "Nike"]
    filtro_baixa = filtro_brasileirao_2025 & resultado[
        "marca_fornecedora"
    ].isin(marcas_gigantes)
    filtro_alta = (
        filtro_brasileirao_2025
        & ~resultado["marca_fornecedora"].isin(marcas_gigantes)
        & (resultado["posicao"] <= 10)
    )
    filtro_media = filtro_brasileirao_2025 & ~filtro_baixa & ~filtro_alta

    resultado.loc[filtro_baixa, "indice_oportunidade"] = "Baixa"
    resultado.loc[filtro_alta, "indice_oportunidade"] = "Alta"
    resultado.loc[filtro_media, "indice_oportunidade"] = "Média"
    return resultado

# 5 - Funções para coletar e salvar dados no MySQL
def coletar_classificacoes_masculinas() -> pd.DataFrame:
    tabelas = []
    data_extracao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for ano in ANOS:
        for nome_liga, sigla_liga in LIGAS.items():
            tabela = getTabelaDF(getRequestFromLeague(sigla_liga, ano))
            if tabela.empty:
                print(f"Não foi possível gerar a tabela para {nome_liga} em {ano}.")
                continue

            tabela["liga"] = nome_liga
            tabela["ano"] = ano
            tabela["data_extracao"] = data_extracao
            tabelas.append(tabela)
            time.sleep(6) # Pausa de 6 segundos entre as requisições para evitar sobrecarga na API'

    if not tabelas:
        return pd.DataFrame()

    classificacoes = pd.concat(tabelas, ignore_index=True)
    classificacoes = adicionar_marcas_fornecedoras(classificacoes)
    return adicionar_indice_oportunidade(classificacoes)

# 6 - Funções para coletar e salvar dados do Brasileirão Feminino
def coletar_dados_brasileirao_feminino() -> pd.DataFrame:
    caminho_dados = Path(__file__).parent / "data" / "classificacoes_feminino.json"
    try:
        with caminho_dados.open(encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError as erro:
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {caminho_dados}") from erro
    except json.JSONDecodeError as erro:
        raise ValueError(f"JSON inválido em {caminho_dados}: {erro}") from erro

    df = pd.DataFrame(dados)
    colunas_ausentes = set(COLUNAS_FEMININO) - set(df.columns)
    if colunas_ausentes:
        raise ValueError(
            "O JSON não possui as colunas obrigatórias: "
            + ", ".join(sorted(colunas_ausentes))
        )

    df = df[COLUNAS_FEMININO].copy()
    df["Saldo_Gols"] = df["Gols_Feitos"] - df["Gols_Sofridos"]
    df["Aproveitamento_%"] = (
        df["Pontos"] / (df["Partidas"] * 3) * 100
    ).round(2)
    df["data_extracao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df.sort_values(by=["Ano", "Fase", "Pontos"], ascending=[True, True, False])

# 7 - Funções para conectar e salvar dados no MySQL
def conectar_mysql():
    """Cria uma conexão SQLAlchemy com o MySQL configurado no .env."""
    url = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER', 'root')}:"
        f"{os.getenv('MYSQL_PASSWORD', '')}@"
        f"{os.getenv('MYSQL_HOST', 'localhost')}:"
        f"{os.getenv('MYSQL_PORT', '3306')}/"
        f"{os.getenv('MYSQL_DB', 'fut_analytica_db')}"
    )
    return create_engine(url)

# 8 - Funções para salvar dados no MySQL
def salvar_no_mysql(
    df: pd.DataFrame,
    tabela: str,
    ddl: str | None = None,
    limpar_tabela: bool = False,
) -> None:
    """Cria opcionalmente a tabela e grava um DataFrame no MySQL."""
    if df.empty:
        print(f"Nenhum dado disponível para a tabela '{tabela}'.")
        return

    engine = conectar_mysql()
    try:
        with engine.begin() as conn:
            if ddl:
                conn.execute(text(ddl))
            if limpar_tabela:
                conn.execute(text(f"TRUNCATE TABLE {tabela}"))

        df.to_sql(
            name=tabela,
            con=engine,
            if_exists="append" if limpar_tabela else "replace",
            index=False,
        )
        print(f"Sucesso! {len(df)} registros gravados em '{tabela}'.")
    except Exception as erro:
        print(f"Erro ao salvar no MySQL: {erro}")
    finally:
        engine.dispose()

# 9 - Funções para executar o ETL masculino e feminino
def executar_etl_masculino() -> None:
    """Executa a coleta e a carga das classificações masculinas."""
    salvar_no_mysql(coletar_classificacoes_masculinas(), "classificacoes")


def executar_etl_feminino() -> None:
    """Executa a leitura do JSON e a carga das classificações femininas."""
    salvar_no_mysql(
        coletar_dados_brasileirao_feminino(),
        "classificacoes_feminino",
        ddl=DDL_CLASSIFICACOES_FEMININO,
        limpar_tabela=True,
    )

# 10 - Execução do ETL masculino e feminino
if __name__ == "__main__":
    executar_etl_masculino()
    executar_etl_feminino()
