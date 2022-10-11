# Data Definition Language (DDL) Basics
## <ins>Description</ins>
#### - Data Definition Language (DDL) is the part of SQL that allows you to create, alter, and drop objects within a relational database. These objects include tables, views, schemas, databases, indexes, stored procedures, and triggers.
## <ins>DDL Statements</ins>
#### - DDL offers a wide array of statements to create, alter, and drop database objects. The list below describes the most common DDL statements used when creating and maintaining a Relational Database Management System (RDBMS):
    - CREATE DATABASE [database_name];
        - This allows you to create a database.
    - CREATE SCHEMA [schema_name];
        - This allows you to create a schema within the database in which you are running the statement.
    - CREATE TABLE [schema_name].[table_name] ([column1] [data type], [column2] [data type], [constraint1]);
        - This allows you to create a table and specify its columns and their associated data types and specify 
          its schema within the database in which you are running the statement.
    - CREATE VIEW [view_name] AS ([SQL Query]);
        - This allows you to create a view (a custom table created from a SEELCT query) within 
          the database in which you are running the statement.
    - ALTER TABLE [schema_name].[table_name] ADD [column_name] [data type];
        - This allows you to add a new column to the specified table and specify its data type. 
    - ALTER TABLE [schema_name].[table_name] ALTER COLUMN [column_name] [new data type];
        - This allows you to change the data type of the specified column in the specified table.
    - DROP TABLE [table_name];
        - This allows you to remove the specified table from the database in which you are running the statement.
    - DROP VIEW [view_name];
        - This allows you to remove the specified view from the database in which you are running the statement.
    - DROP DATABASE [database_name];
        - This allows you to remove the specified database, along with its associated schemas, tables, and views
          from the server.
    - DROP SCHEMA [schema_name];
        - This allows you to remove the specified schema from the database in which you are running the statement.
