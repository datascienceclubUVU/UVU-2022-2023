# Intermediate SQL: Subqueries
## Introduction
#### Welcome to the first tutorial in the Intermediate section of this learning series! In this tutorial, we will be discussing the semantics and use cases behind subqueries in SQL. **_Subqueries_** are queries that are nested inside a master SQL statement and provide more flexibility for filtering and aggregating. Let's take a look at the different use cases of subqueries.
## Subquery Use Cases
### Subqueries in the FROM Clause
#### Suppose you have a very large table that takes a long time to run a basic query. To aid in this, we can create a subquery to create a subset of the base table and query that temporary table. This type of query has the following syntax:
    SELECT [column_name], [column_name]
    FROM (SELECT [column_name], [column_name]
          FROM [base_table]
          GROUP BY [column_name] *This is optional) [query_name]
    WHERE [condition]
#### Example:
    SELECT customer_name, num_orders
    FROM (SELECT customer_name, COUNT(DISTINCT order_id) num_orders
          FROM dim_customers
          GROUP BY customer_name) customer_orders
    WHERE customer_name = 'John Wall'
