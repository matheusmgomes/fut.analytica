# Importação das bibliotecas necessárias
import os # Biblioteca para interagir com o sistema operacional
import requests # Biblioteca para fazer requisições HTTP
import json # Biblioteca para trabalhar com dados em formato JSON
import pandas as pd #Biblioteca Pandas para DataFrames e limpeza de dados
from dotenv import load_dotenv # Biblioteca para carregar variáveis de ambiente de um arquivo .env
from datetime import datetime # Biblioteca para trabalhar com datas e horas

# 1 - Carregar as variaveis do ambiente do arquivo .env
load_dotenv()
api_token = os.getenv("FOOTBALL_API_KEY") # Pegar a chave da API do arquivo .env
headers = {
    "X-Auth-Token": api_token
} # Cabeçalho da requisição HTTP, incluindo a chave da API para autenticação

#leagues = ['BSA', 'PL', 'PD']
years = ['2025', '2024', '2023']

leagues = {
    "Brasil - Brasileirão Série A": "BSA",
    "Inglaterra - Premier League": "PL",
    "Espanha - La Liga": "PD"
}

def getRequestFromLeague(league: str, year: str)->dict:
    url = f"https://api.football-data.org/v4/competitions/{league}/standings"

    response = requests.get(url, headers=headers, params={"season": year})

    if response.status_code == 200:
        return response.json()
    else:
        print("Houve um erro na requisição")
        return {}

def getTabelaDF(dados: dict)->pd.DataFrame: #recebe o json de dados da API e retorna a tabela do campeonato como DataFrame
    
    if not dados or 'standings' not in dados or not dados['standings']:
        print("Aviso: 'standings' veio vazio ou não existe para esta temporada/liga.")
        return pd.DataFrame() # Retorna DataFrame vazio seguro
    
    dadosLimpos = []
    
    try: # Tente mapear os dados do JSON para o DataFrame
        tabela_posicoes = dados['standings'][0]['table']
        for time in tabela_posicoes: #para cada time da tabela, adiciona os dados importantes no array de dados limpos
            dadosLimpos.append({
                'posicao': time['position'],
                'nome_time': time['team']['name'],
                'total_jogos': time['playedGames'],
                'vitorias': time['won'],
                'empates': time['draw'],
                'derrotas': time['lost'],
                'gols_pro': time['goalsFor'],
                'gols_contra': time['goalsAgainst'],
                'saldo_de_gols': time['goalDifference'],
                'pontos': time['points']
            })
    except (KeyError, IndexError) as e: # Captura erros de chave ou indice caso a estrutura do JSON não seja a esperada
        print(f"Erro de estrutura ao mapear JSON: {e}")
        return pd.DataFrame()

    return pd.DataFrame(dadosLimpos) # Retorna o DataFrame com os dados limpos 

# Função para salvar a tabela em um arquivo CSV, ajustei por que tava dadno erro na minha maquina
def saveTabela(df, league, year):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, 'data')
    
    os.makedirs(output_dir, exist_ok=True) 
    
    file_path = os.path.join(output_dir, f'tabela_{league}_{year}.csv')
    df.to_csv(file_path, index=False)

todas_tabelas = []

hora = datetime.now()
timestamp_coluna = hora.strftime('%Y-%m-%d %H:%M:%S') 
timestamp_arquivo = hora.strftime('%Y%m%d_%H%M%S')

for year in years:
    for nome_liga, sigla_liga in leagues.items():
        dados = getRequestFromLeague(sigla_liga, year)
        tabela = getTabelaDF(dados)

        if not tabela.empty:
            tabela['liga'] = nome_liga
            tabela['ano'] = year
            tabela['data_extracao'] = timestamp_coluna
            todas_tabelas.append(tabela)
        else:
            print(f"Não foi possível gerar a tabela para a liga '{nome_liga}' no ano {year}.")
            
if todas_tabelas:

    df_final = pd.concat(todas_tabelas, ignore_index=True)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, 'data')
    os.makedirs(output_dir, exist_ok=True) 
    
    nome_arquivo = f'todas_tabelas_{timestamp_arquivo}.csv'
    file_path = os.path.join(output_dir, nome_arquivo)

    df_final.to_csv(file_path, index=False)

else:
    print("Nenhum dado foi extraído de nenhuma liga/ano.")