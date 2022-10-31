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
### Subqueries in the SELECT Clause
#### When you're wanting to construct a custom calculation between two columns from two different tables, a subquery is a common use case. This type of query doesn't have a specific syntax, though it does have the following constraints:
    - The subquery MUST have the same level of detail as the base query (i.e. if the base query has 3 columns, the subquery must also have 3 columns).
    - The subquery CANNOT have an ORDER BY clause.
#### Example:
    SELECT customer_id, (SELECT SUM(ship_charge) 
                        FROM orders
                        WHERE customer.customer_num = orders.customer_num) AS total_ship_chg
	FROM customers
### Subqueries in the WHERE Clause
#### This is by far the most common use case of subqueries. Subqueries in the WHERE clause are used to reference either a pre-created list of conditions or compare the query results with the query results of the subqueries. This type of query has the following syntax:
    SELECT [column_name], [column_name]
    FROM [table_name]
    WHERE [column_name] [logical operator or IN function] (SELECT [column_name] FROM [table_name] ORDER BY [column_name] [ASC/DESC])
#### Example:
    SELECT customer_id, first_name, last_name
    FROM customers
    WHERE customer_id IN (SELECT DISTINCT customer_id FROM lost_shipments)

## Conclusion
#### Subqueries can also be used in other statements such as INSERT and DELETE statements and Triggers. These use cases tend to be rarer, though are worth mentioning.

## Next Steps
#### Subqueries can be confusing, let's learn a more effective querying method:
- [CTEs](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/CTEs.md)
