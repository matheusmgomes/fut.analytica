-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence)
-- ARQUIVO: 02_views_negocio.sql
-- DESCRIÇÃO: Criação das Visões de Negócio (Views) para alimentar o Power BI
-- TABELA FONTE: classificacoes (gerada via pipeline ETL Python)
-- =============================================================================

USE fut_analytica_db;

-- -----------------------------------------------------------------------------
-- VIEW 1: vw_gemas_escondidas
-- OBJETIVO: Mapear clubes fora do Top 4 (posicao > 4) com alto volume ofensivo.
-- RESPONDE: Nível 1 - Pergunta 1 (Onde colocar o dinheiro com baixo custo/mídia alta).
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_gemas_escondidas AS
SELECT 
    nome_time,
    liga,
    ano AS temporada,
    posicao,
    pontos,
    gols_pro,
    gols_contra,
    saldo_de_gols
FROM classificacoes
WHERE posicao > 4
ORDER BY gols_pro DESC;


-- -----------------------------------------------------------------------------
-- VIEW 2: vw_consistencia_clubes
-- OBJETIVO: Avaliar estabilidade e volatilidade (desvio padrão) no ciclo de 3 anos.
-- RESPONDE: Nível 1 - Pergunta 3 (Mitigação de risco para investimento).
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_consistencia_clubes AS
SELECT 
    nome_time,
    liga,
    COUNT(DISTINCT ano) AS total_temporadas,
    ROUND(AVG(gols_pro), 2) AS media_gols_pro,
    ROUND(STDDEV_SAMP(gols_pro), 2) AS desvio_padrao_gols,
    MIN(posicao) AS melhor_posicao,
    MAX(posicao) AS pior_posicao,
    CASE 
        WHEN STDDEV_SAMP(gols_pro) IS NULL THEN 'Dados Insuficientes'
        WHEN STDDEV_SAMP(gols_pro) <= 3.0 THEN 'Porto Seguro (Baixo Risco)'
        WHEN STDDEV_SAMP(gols_pro) > 10.0 THEN 'Alto Risco'
        ELSE 'Risco Moderado'
    END AS classificacao_risco
FROM classificacoes
GROUP BY nome_time, liga;


-- -----------------------------------------------------------------------------
-- VIEW 3: vw_comparativo_ligas
-- OBJETIVO: Agrupar volume total de gols e média de gols por jogo por liga e ano.
-- RESPONDE: Nível 1 - Pergunta 2 e Nível 2 - Pergunta 2 (Volume e evolução do espetáculo).
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_comparativo_ligas AS
SELECT 
    liga,
    ano AS temporada,
    SUM(gols_pro) AS total_gols_pro_liga,
    SUM(gols_contra) AS total_gols_contra_liga,
    ROUND(AVG((gols_pro + gols_contra) / total_jogos), 2) AS media_gols_por_partida
FROM classificacoes
GROUP BY liga, ano;