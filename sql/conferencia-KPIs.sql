USE fut_analytica_db;

-- 1. Total Geral de Gols (Todas as ligas e temporadas de Gemas Escondidas)
SELECT SUM(gols_pro) AS total_gols_masculino_geral
FROM vw_gemas_escondidas;

-- 2. Total de Gols por Liga (Para bater com o filtro quando clicar no Slicer)
SELECT 
    liga, 
    SUM(gols_pro) AS total_gols_por_liga
FROM vw_gemas_escondidas
GROUP BY liga;

-- Média de Gols Marcados por time/temporada em Gemas Escondidas
SELECT 
    ROUND(AVG(gols_pro), 2) AS media_gols_masculino_geral
FROM vw_gemas_escondidas;

-- Média por Liga (Para conferir quando o filtro de liga estiver ativo)
SELECT 
    liga, 
    ROUND(AVG(gols_pro), 2) AS media_gols_por_liga
FROM vw_gemas_escondidas
GROUP BY liga;

-- Total de Gols Marcados na 1ª Fase do Futebol Feminino
SELECT SUM(Gols_Feitos) AS total_gols_feminino
FROM vw_feminino_gemas_escondidas;

-- Contagem distinta de clubes no radar do futebol feminino
SELECT COUNT(DISTINCT Clube) AS total_equipes_feminino
FROM vw_feminino_gemas_escondidas;