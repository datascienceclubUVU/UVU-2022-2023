# Data Manipulation Language (DML) Basics
## Description
#### Data Manipulation Language (DML) is the part of SQL that allows you to append, update, and delete items to/from objects within a relational database. These objects include tables, views and schemas.
## DML Statements
#### DML offers a simple assortment of statements to add items to, update items in, and delete items from database objects. The list below describes the most common DML statements used when maintaining a Relational Database:
`INSERT INTO [table_name] VALUES ([values in order of table columns]);`
##### This allows you to load a single item into a database table.
`INSERT INTO [table_name] VALUES ([values in order of table columns]), ([values in order of table columns]), ([values in order of table columns]);`
##### This allows you to load multiple items into a database table
`UPDATE [table_name] SET [column_name] = [value] // WHERE [condition] (This is optional);`
##### This allows you to update column values in a database table.
`DELETE FROM [table_name] WHERE [condition];`
##### This allows you to delete items from a database table based on a specified condition.
## Example
#### In the example below, I will show you how to use these statements to organize your Relational Database. This example follows the example from the DDL Tutorial where the makeshift company now has a sales database but needs to load data into it and make some changes to existing data:
    -- The purpose of the USE statement is to specify the database you are using
    USE sales;
    -- Add new records to the table from the most recent hires
    INSERT INTO managers.sales_rep VALUES (123, 'Josh', 'Tyson', '7/2/2022', NULL, 1756.00, 130.12), (124, 'Abbie', 'Tomlinson', '8/16/2022', NULL, 1455.90, 98.77);
    -- Make change to the total_sales_by_rep view to reflect a lost sale
    UPDATE VIEW total_sales_by_rep SET net_sales = net_sales - 50.00 WHERE last_name = 'Johnson' AND first_name = 'Jack';
    -- Delete records that were placed in the table on or before the start of 2017 to get rid of invalid entries
    DELETE FROM sales_rep WHERE hire_date <= '1/1/2017';
## NEXT STEPS
- Falling in love with SQL? You're not alone! Here are some more tutorials to aid you in your SQL learning journey:
- Basic SQL Statements
- Aggregate Functions
- Subqueries
