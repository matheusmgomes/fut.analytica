-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence)
-- ARQUIVO: 02_views_marcas.sql
-- DESCRIÇÃO: Visões de negócio sobre marcas fornecedoras (patrocínio material)
-- TABELA FONTE: classificacoes (colunas marca_fornecedora e indice_oportunidade,
--               populadas apenas para liga = 'Brasil - Brasileirão Série A' e ano = '2025')
-- =============================================================================

USE fut_analytica_db;

-- -----------------------------------------------------------------------------
-- VIEW 1: vw_marcas_desempenho_clubes
-- OBJETIVO: Visão completa clube x marca x desempenho, base para os demais recortes.
-- RESPONDE: "Quem veste quem, e como cada um está performando na tabela?"
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_marcas_desempenho_clubes AS
SELECT
    nome_time,
    posicao,
    pontos,
    gols_pro,
    gols_contra,
    saldo_de_gols,
    marca_fornecedora,
    indice_oportunidade
FROM classificacoes
WHERE liga = 'Brasil - Brasileirão Série A'
  AND ano = '2025'
  AND marca_fornecedora IS NOT NULL
ORDER BY posicao ASC;


-- -----------------------------------------------------------------------------
-- VIEW 2: vw_prospeccao_patrocinio
-- OBJETIVO: Shortlist de clubes com bom desempenho esportivo e SEM marca gigante
--           (Adidas/Nike/Puma/Umbro) como fornecedora atual — potenciais alvos
--           de prospecção comercial para novos patrocínios de material esportivo.
-- RESPONDE: "Onde o cliente Gol de Placa deveria bater a porta primeiro?"
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_prospeccao_patrocinio AS
SELECT
    nome_time,
    posicao,
    pontos,
    gols_pro,
    saldo_de_gols,
    marca_fornecedora
FROM classificacoes
WHERE liga = 'Brasil - Brasileirão Série A'
  AND ano = '2025'
  AND indice_oportunidade = 'Alta'
ORDER BY posicao ASC;


-- -----------------------------------------------------------------------------
-- VIEW 3: vw_desempenho_medio_por_marca
-- OBJETIVO: Agregar o desempenho esportivo médio dos clubes patrocinados por
--           cada marca — mede se o "portfólio" de uma marca tende a estar
--           concentrado no topo ou na base da tabela.
-- RESPONDE: "Qual marca tem o portfólio de clubes mais forte esportivamente?"
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_desempenho_medio_por_marca AS
SELECT
    marca_fornecedora,
    COUNT(*) AS total_clubes,
    ROUND(AVG(posicao), 2) AS posicao_media,
    ROUND(AVG(pontos), 2) AS pontos_medio,
    ROUND(AVG(gols_pro), 2) AS gols_pro_medio,
    MIN(posicao) AS melhor_posicao,
    MAX(posicao) AS pior_posicao
FROM classificacoes
WHERE liga = 'Brasil - Brasileirão Série A'
  AND ano = '2025'
  AND marca_fornecedora IS NOT NULL
GROUP BY marca_fornecedora
ORDER BY posicao_media ASC;