-- =============================================================================
-- PROJETO: Fut.Analytica (Scouting Intelligence)
-- ARQUIVO: 01_setup_database.sql
-- DESCRIÇÃO: Criação do schema relacional com codificação UTF-8
-- =============================================================================

-- 1. Criação do Banco de Dados (Schema) caso não exista
CREATE DATABASE IF NOT EXISTS fut_analytica_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

-- 2. Seleção do banco de dados para uso nas sessões subsequentes
USE fut_analytica_db;