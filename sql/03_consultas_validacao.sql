-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence)
-- ARQUIVO: 03_consultas_validacao.sql
-- DESCRIÇÃO: Consultas de auditoria para validação de dados e checagem de Views
-- =============================================================================
USE USE fut_analytica_db;

-- 1. Conferência do volume total de registros gravados
SELECT COUNT(*) AS total_registros_base FROM classificacoes;

-- 2. Validação do balanceamento de times por liga e temporada
SELECT 
    liga, 
    ano, 
    COUNT(*) AS total_times 
FROM classificacoes 
GROUP BY liga, ano 
ORDER BY liga ASC, ano DESC;

-- 3. Teste de retorno da View de Gemas Escondidas (Temporada 2023)
SELECT * FROM vw_gemas_escondidas WHERE temporada = '2023' LIMIT 5;

-- 4. Teste de retorno da View de Consistência e Risco
SELECT * FROM vw_consistencia_clubes ORDER BY media_gols_pro DESC LIMIT 10;