# Importação das bibliotecas necessárias
import os # Biblioteca para interagir com o sistema operacional
import requests # Biblioteca para fazer requisições HTTP
import json # Biblioteca para trabalhar com dados em formato JSON
import pandas as pd #Biblioteca Pandas para DataFrames e limpeza de dados
from dotenv import load_dotenv # Biblioteca para carregar variáveis de ambiente de um arquivo .env

# 1 - Carregar as variaveis do ambiente do arquivo .env
load_dotenv()
api_token = os.getenv("FOOTBALL_API_KEY") # Pegar a chave da API do arquivo .env
headers = {
    "X-Auth-Token": api_token
} # Cabeçalho da requisição HTTP, incluindo a chave da API para autenticação

# Endpoint, pegar os dados do brasileirão
url = "https://api.football-data.org/v4/competitions/BSA/standings"

def getTabelaDF(dados: list)->pd.DataFrame: #recebe o json de dados da API e retorna a tabela do campeonato como DataFrame
    dadosLimpos = []
    for time in dados['standings'][0]['table']: #para cada time da tabela, adiciona os dados importantes no array de dados limpos
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
    df = pd.DataFrame(dadosLimpos) #cria o data frame em cima dos dados já separados
    return df

resposta = requests.get (url, headers=headers) # Fazer uma requisição GET para o endpoint da API com os cabeçalhos definidos
if resposta.status_code == 200: # Verificar se a requisição foi bem-sucedida (código de status 200)
    dados = resposta.json() # Converter a resposta em formato JSON para um dicionário Python
    
    if dados: #caso a requisição retorne dados vazios, não chama a função de data frame
        tabela = getTabelaDF(dados)
        print(tabela)
    else:
        print('Dados vazios')
            
    # area_dados = dados.get('area') # Obter os dados do Brasil no JSON
    # estrutura_formatada = json.dumps(area_dados, indent=4, ensure_ascii=False)
    # print("Status Code:", resposta.status_code) # Imprimir o código de status da resposta
    # print(f"Nome: {dados.get('name')}") # Imprime o nome da competição
    # print(f"Área: {dados.get('area', {}).get('name')}") # Imprime o nome da área da competição
    # print(f"Temporada Atual: {dados.get('currentSeason', {}).get('startDate')} até {dados.get('currentSeason', {}).get('endDate')}") # Imprime o período da temporada atual
    # print("==================================")
    # print("ESTRUTURA COMPLETA DO JSON")
    # print("==================================\n")
    # print(estrutura_formatada)
else:
    print(f"Erro ao obter dados da API: {resposta.status_code}") # Imprimir uma mensagem de erro caso a requisição não tenha sido bem-sucedida
    