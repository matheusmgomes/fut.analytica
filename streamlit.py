import streamlit as st
import pandas as pd


st.set_page_config(layout="wide") #define a largura da página do streamlit para caber na tela toda

def load_data()->pd.DataFrame: #faz a conexão com o mysql e retorna um dataframe com os dados
    conn = st.connection('mysql', type='sql')
    df = conn.query("SELECT * FROM classificacoes")
    return df

#cria a aba lateral com os filtros de ano e liga e depois retorna o data frame filtrado de acordo com a seleção
def filter_data(df: pd.DataFrame)->pd.DataFrame:
    st.sidebar.header('Filtros')

    years = df['ano'].unique().tolist()
    selected_year = st.sidebar.selectbox(
      "Anos",
      options=years
    )

    leagues = df['liga'].unique().tolist()
    selected_league = st.sidebar.selectbox(
        "Liga",
        options=leagues
    )

    return df[
        (df['ano'] == selected_year) & (df['liga'] == selected_league)
    ]

#função principal que define o corpo da página
def main()->None:
    st.title("⚽ Fut.Analytica")

    df = load_data()
    filtered_df = filter_data(df)

    if filtered_df.empty:
        st.warning("Nenhum dado recuperado do banco.")
        st.stop()

    total_goals_pro = int(filtered_df['gols_pro'].sum())
    champion = filtered_df['nome_time'].iloc[0] #busca primeiro time na tabela do ano (ordenada por pontos, logo o campeão)
    most_goals_team = filtered_df.sort_values(by='gols_pro', ascending=False).iloc[0] #busca o primeiro time da tabela ordenada por gols_pro descrescente
    least_goals_team = filtered_df.sort_values(by='gols_contra').iloc[0] #busca o primeiro time da tabela ordenada por gols_contra crescente

    
    col1, col2, col3, col4, col5, col6 = st.columns(6) #divide a interface do streamlit em colunas e faz o visual de cards separados
    col1.metric('Campeão', champion)
    col2.metric('Total de Gols no Campeonato', total_goals_pro)
    col3.metric('Time de melhor ataque', most_goals_team['nome_time'])
    col4.metric('Total de Gols do melhor ataque', most_goals_team['gols_pro'])
    col5.metric('Time de melhor defesa', least_goals_team['nome_time'])
    col6.metric('Total de Gols da melhor defesa', least_goals_team['gols_contra'])
    
    st.subheader("Classificação Final")
    st.dataframe(filtered_df, hide_index=True)



if __name__ == '__main__':
    main()