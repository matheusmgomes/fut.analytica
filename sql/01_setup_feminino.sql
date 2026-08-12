-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence - Expansão Futebol Feminino)
-- ARQUIVO: 01_setup_feminino.sql
-- DESCRIÇÃO: Criação da Tabela Fato para a modalidade feminina
-- =============================================================================

USE fut_analytica_db;

-- Tabela Fato: Contempla tanto a Primeira Fase quanto o Mata-Mata
CREATE TABLE classificacoes_feminino (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Chave primária autoincrementada',
    Ano INT NOT NULL COMMENT 'Temporada do campeonato (2023, 2024, 2025)',
    Fase VARCHAR(50) NOT NULL COMMENT 'Fase da competição (Primeira Fase / Mata-Mata)',
    Clube VARCHAR(100) NOT NULL COMMENT 'Nome oficial do clube',
    Partidas INT NOT NULL COMMENT 'Partidas disputadas na fase',
    Vitorias INT NOT NULL COMMENT 'Vitórias conquistadas na fase',
    Empates INT NOT NULL COMMENT 'Empates na fase',
    Derrotas INT NOT NULL COMMENT 'Derrotas na fase',
    Pontos INT NOT NULL COMMENT 'Pontuação acumulada na fase',
    Gols_Feitos INT NOT NULL COMMENT 'Gols marcados na fase',
    Gols_Sofridos INT NOT NULL COMMENT 'Gols sofridos na fase',
    Saldo_Gols INT NOT NULL COMMENT 'Saldo de gols na fase',
    `Aproveitamento_%` DECIMAL(5,2) NOT NULL COMMENT 'Porcentagem de aproveitamento de pontos',
    data_extracao DATETIME NOT NULL COMMENT 'Data e hora do carregamento via Python',
    
    INDEX idx_ano_fase (Ano, Fase),
    INDEX idx_clube (Clube)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Tabela fato de desempenho do Brasileirão Feminino (2023-2025)';

SELECT *FROM classificacoes_feminino;