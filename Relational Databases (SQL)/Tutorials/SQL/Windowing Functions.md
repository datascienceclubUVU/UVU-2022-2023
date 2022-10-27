# Advanced SQL: Windowing Functions
## Introduction
#### One of the most common methods to analyze large amounts of data is to partition the data into individual groups. This can be done using various **_Windowing Functions_**. A **_Windowing Function_** splits the data into individual groups based on a specified boundary (e.g., id, name, date). These are widely used for creating rolling functions, grouping data without changing the level of detail, and making it easier to identify potential duplicates. Let's take a closer look at the different types of windowing functions:
## Types of Windowing Functions
#### As you might expect, there are several windowing functions available in SQL. These include the following:
    - Aggregate Functions (SUM, AVG, and COUNT)
    - ROW_NUMBER
    - RANK
    - DENSE_RANK
    - LAG
    - LEAD
    - NTILE
    - FIRST_VALUE
    - LAST_VALUE
    - CUME_DIST
    - PERCENT_RANK
#### It should be noted that all window functions have the following syntax:
    [window_function]() OVER(PARTITION BY [column_name] ORDER BY [column_name] [ASC/DESC])
#### Because there are many functions listed, we will group them into the following groups: Ranking Functions, Aggregate Functions, Comparison Functions, and Statistical Functions.
### Ranking Functions
#### ROW_NUMBER
##### The purpose of this function is to specify the index number of each row in each partition. In the example below, we will illustrate how this function can be used in conjunction with CTEs:
    # We are trying to find the first orders placed by our customers
    WITH customer_orders AS (SELECT id AS customer_id, first_name, last_name, order_amt, num_items, order_date, order_id, 
                            ROW_NUMBER() OVER(PARTITION BY id ORDER BY order_date) row_num 
                            FROM customers 
                            JOIN orders ON customers.id = orders.customer_id)
    SELECT * FROM customer_orders WHERE row_num = 1;
##### Output:
    - CTE:
    customer_id  |  first_name  |  last_name  |  order_amt  |  num_items  |  order_date  |  order_id  |  row_num
       15219091  |       Jerry  |   Seinfeld  |     787.90  |          4  |   4-12-2020  |   7610923  |         1
       15219091  |       Jerry  |   Seinfeld  |     329.17  |          2  |   7-09-2020  |   7856719  |         2
       15219091  |       Jerry  |   Seinfeld  |     432.09  |          2  |   7-28-2020  |   7856798  |         3
       15223175  |      Robert  |       Ross  |     178.10  |          3  |  11-13-2018  |   7561329  |         1
       15223175  |      Robert  |       Ross  |     219.08  |          5  |  11-28-2018  |   7561422  |         2
       15223175  |      Robert  |       Ross  |      89.00  |          1  |  12-15-2018  |   7578903  |         3
       
    - Result Query
    customer_id  |  first_name  |  last_name  |  order_amt  |  num_items  |  order_date  |  order_id  |  row_num
       15219091  |       Jerry  |   Seinfeld  |     787.90  |          4  |   4-12-2020  |   7610923  |         1
       15223175  |      Robert  |       Ross  |     178.10  |          3  |  11-13-2018  |   7561329  |         1
