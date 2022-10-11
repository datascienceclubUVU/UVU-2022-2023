# SQL for Beginners
## <ins>Introduction</ins>
#### Interested in learning more about the world of databases? Look no further than SQL! This tutorial will be your guide to learn the basic SQL statements. Enjoy!


## <ins>Definitions</ins>
#### A <i>column</i>, also called an "attribute" or "field", describes an aspect of a data point. For example, height, weight, and age may all be columns.
#### A <i>row</i>, also called a record, is a collection of columns that represent a single data point. For example, one row may represent one hospital patient and may have attributes like age, weight, and height.
#### A <i>table</i> is a collection of rows and columns. This is the most basic unit found in a database and will be the foundation of this tutorial.
#### A <i>query</i> is a specific selection of columns from a table that can include filters to limit the rows retrieved. A google search is an example of a query.

## <ins>The 5 Basic SQL Statements</ins>
#### - Since this is a tutorial for beginners, I’m going to show you how to write a query if you wanted to extract data from one table.
#### - There are five components to a basic query:
   - _SELECT_ **(mandatory)**
      - This is how to start a query and is used to specify the columns to return.
   - _FROM_ **(mandatory)**
   -  - This is used to specify the table to query.
   - _WHERE_ (optional)
      - This is used to filter the rows that are returned.
   - _GROUP BY_ (optional)
      - This is used in conjunction with aggregate functions (SUM, COUNT, MAX, etc.) to specify the level of detail to provide.
   - _ORDER BY_ (optional)
      - This is used to specify the sort order of the results.
#### - The structure is as follows:
      - SELECT [column1], [column2]
      - FROM [table_name]
      - WHERE [condition]
      - GROUP BY [all columns NOT being aggregated]
      - ORDER BY [DESC | ASC (default)]
### EXAMPLE
      - SELECT customer_id, name, age, SUM(num_orders)
      - FROM customers
      - WHERE age > 20 and city = 'Chicago'
      - GROUP BY customer_id, name, age
      - ORDER BY customer_id;

## Next Steps:
### So you want to learn more? Here is a list of resources to help you continue your SQL learning journey:
#### - [Aggregate Functions](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/Aggregate%20Functions.md)
