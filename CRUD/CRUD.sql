select DB_NAME()
-- Create a new database called 'Test'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'Test'
)
CREATE DATABASE Test
GO
USE Test
GO
CREATE SCHEMA Test
GO
-- Get a list of tables and views in the current database
SELECT table_catalog [database], table_schema [schema], table_name name, table_type type
FROM INFORMATION_SCHEMA.TABLES
GO

-- Create a new table called 'Vendas' in schema 'SchemaName'
-- Drop the table if it already exists
IF OBJECT_ID('Test.Vendas', 'U') IS NOT NULL
DROP TABLE Test.Vendas
GO
-- Create the table in the specified schema
CREATE TABLE Test.Vendas
(
    VendasId INT NOT NULL PRIMARY KEY, -- primary key column
    NomeProduto [NVARCHAR](45) NOT NULL,
    Valor INT NOT NULL
    -- specify more columns here
);
GO
-- Select rows from a Table or View 'Vendas' in schema 'SchemaName'
SELECT * FROM Test.Vendas	/* add search conditions here */
GO
-- Insert rows into table 'Test.Vendas'
INSERT INTO Test.Vendas VALUES(2, 'Todynho', 3);
-- add more rows here
GO
-- Delete rows from table 'Test.Vendas'
USE Test
DELETE FROM Test.Vendas
WHERE VendasId = 0
GO