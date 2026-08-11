-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence - Expansão Futebol Feminino)
-- ARQUIVO: 02_views_feminino.sql
-- DESCRIÇÃO: Visões de negócio para o Dashboard Único de Futebol Feminino
-- =============================================================================

USE fut_analytica_db;

-- -----------------------------------------------------------------------------
-- VIEW 1: vw_feminino_gemas_escondidas
-- OBJETIVO: Mapear clubes de alta eficiência ofensiva na Primeira Fase fora do Top 3
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_feminino_gemas_escondidas AS
SELECT 
    Clube,
    Ano AS Temporada,
    Pontos,
    Gols_Feitos,
    Gols_Sofridos,
    Saldo_Gols,
    `Aproveitamento_%`
FROM classificacoes_feminino
WHERE Fase = 'Primeira Fase' 
  AND Clube NOT IN ('Corinthians', 'Palmeiras', 'São Paulo')
ORDER BY Gols_Feitos DESC;

-- -----------------------------------------------------------------------------
-- VIEW 2: vw_feminino_desempenho_mata_mata
-- OBJETIVO: Avaliar o rendimento e resiliência dos clubes na fase eliminatória
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_feminino_desempenho_mata_mata AS
SELECT 
    Clube,
    Ano AS Temporada,
    Partidas AS Jogos_MataMata,
    Vitorias,
    Gols_Feitos,
    Gols_Sofridos,
    `Aproveitamento_%` AS Aproveitamento_MataMata
FROM classificacoes_feminino
WHERE Fase LIKE '%Mata-Mata%'
ORDER BY Ano DESC, Vitorias DESC;

-- -----------------------------------------------------------------------------
-- VIEW 3: vw_feminino_consistencia_3anos
-- OBJETIVO: Medir a estabilidade de pontos e saldo de gols no ciclo 2023-2025
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_feminino_consistencia_3anos AS
SELECT 
    Clube,
    COUNT(DISTINCT Ano) AS Temporadas_Disputadas,
    ROUND(AVG(Pontos), 2) AS Media_Pontos_PrimeiraFase,
    ROUND(AVG(Gols_Feitos), 2) AS Media_Gols_Feitos,
    ROUND(STDDEV_SAMP(Gols_Feitos), 2) AS Desvio_Padrao_Gols
FROM classificacoes_feminino
WHERE Fase = 'Primeira Fase'
GROUP BY Clube
ORDER BY Media_Gols_Feitos DESC;