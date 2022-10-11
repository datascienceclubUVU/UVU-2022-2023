Data Definition Language (DDL) Basics
## <ins>Description</ins>
#### - Data Definition Language (DDL) is the part of SQL that allows you to create, alter, and drop objects within a relational database. These objects include tables, views, schemas, databases, indexes, stored procedures, and triggers.
## <ins>DDL Statements</ins>
#### - DDL offers a wide array of statements to create, alter, and drop database objects. The list below describes the most common DDL statements used when creating and maintaining a Relational Database Management System (RDBMS):
    - CREATE DATABASE [database_name];
    - CREATE SCHEMA [schema_name];
    - CREATE TABLE [schema_name].[table_name] ([column1] [data type], [column2] [data type], [constraint1]);
    - CREATE VIEW [view_name] AS ([SQL Query]);
    - ALTER TABLE [schema_name].[table_name] ADD [column_name] [data type]
    - ALTER TABLE [schema_name].[table_name] ALTER COLUMN [column_name] [new data type]
    - DROP TABLE [table_name];
    - DROP VIEW [view_name];
    - DROP DATABASE [database_name];
    - DROP SCHEMA [schema_name];
