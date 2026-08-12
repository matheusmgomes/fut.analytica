-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence - Expansão Futebol Feminino)
-- ARQUIVO: 03_validacao_feminino.sql
-- DESCRIÇÃO: Consultas de auditoria da carga de dados do futebol feminino
-- =============================================================================

USE fut_analytica_db;

-- 1. Total de registros inseridos pelo script Python
SELECT COUNT(*) AS total_registros_feminino FROM classificacoes_feminino;

-- 2. Distribuição de registros por Fase e Ano
SELECT Ano, Fase, COUNT(*) AS Qtd_Clubes 
FROM classificacoes_feminino 
GROUP BY Ano, Fase 
ORDER BY Ano DESC, Fase ASC;

-- 3. Validação do retorno das Views
SELECT * FROM vw_feminino_gemas_escondidas WHERE Temporada = 2024 LIMIT 5;
SELECT * FROM vw_feminino_consistencia_3anos LIMIT 10;