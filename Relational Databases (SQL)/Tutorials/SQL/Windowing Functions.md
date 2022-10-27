# Advanced SQL: Window Functions
## Introduction
#### One of the most common methods to analyze large amounts of data is to partition the data into individual groups. This can be done using various **_Window Functions_**. A **_Window Function_** splits the data into individual groups based on a specified boundary (e.g., id, name, date). These are widely used for creating rolling functions, grouping data without changing the level of detail, and making it easier to identify potential duplicates. Let's take a closer look at the different types of windowing functions:
## Types of Window Functions
#### As you might expect, there are several window functions available in SQL. These include the following:
    - ROW_NUMBER
    - RANK
    - DENSE_RANK
    - LAG
    - LEAD
    - FIRST_VALUE
    - LAST_VALUE
    - SUM 
    - AVG
    - COUNT
    - NTILE
    - CUME_DIST
    - PERCENT_RANK
#### It should be noted that all window functions have the following syntax:
    [window_function]() OVER(PARTITION BY [column_name] ORDER BY [column_name] [ASC/DESC])
#### Because there are many functions listed, we will group them into the following groups: Ranking Functions, Aggregate Functions, Comparison Functions, and Statistical Functions.
## Ranking Functions
#### Within every organization, there is a need to measure attributes between various groups or departments. This allows organizations to create more detailed Key Performance Indicators (KPIs) and allow managers to measure the performance of their employees. THis is the basic premis of ranking window functions.
### ROW_NUMBER
#### The purpose of this function is to specify the index number of each row in each partition. In the example below, we will illustrate how this function can be used in conjunction with CTEs:
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
### RANK
#### As you might assume, this function is used to rank items within a specified group. This is commonly used to identify the best-selling products, most-productive emmployees, and highest gross profit margins.
#### Example:
    # In this query, we are trying to find the best selling car manufacturer in each region of the US.
    SELECT region, make, num_sales, RANK() OVER(PARTITION BY region ORDER BY num_sales DESC) sales_rank 
    FROM regional_sales
##### Output:
    region  |       make  |  num_sales  |  sales_rank
     north  |  Chevrolet  |      89500  |           1
     north  |       Ford  |      89000  |           2
     north  |     Toyota  |      89000  |           2
     north  |      Honda  |      84295  |           4
     north  |    Hyundai  |      81100  |           5
     south  |       Ford  |      54900  |           1
     south  |     Toyota  |      51300  |           2
     south  |  Chevrolet  |      51300  |           2
     south  |    Hyundai  |      47860  |           4
     south  |      Mazda  |      41320  |           5
### DENSE_RANK
#### The main issue with the RANK function is that it skips ranks when there are duplicate values. This can make it difficult to interpret the results. To help with this, the DENSE_RANK function continues the rank rather than skips. This is usually used in place of the RANK function.
#### Example:
    # For this example, we will be running the same query as the RANK example
    SELECT region, make, num_sales, DENSE_RANK() OVER(PARTITION BY region ORDER BY num_sales DESC) sales_dense_rank
    FROM regional_sales
##### Output:
    region  |       make  |  num_sales  |  sales_dense_rank
     north  |  Chevrolet  |      89500  |           1
     north  |       Ford  |      89000  |           2
     north  |     Toyota  |      89000  |           2
     north  |      Honda  |      84295  |           3
     north  |    Hyundai  |      81100  |           4
     south  |       Ford  |      54900  |           1
     south  |     Toyota  |      51300  |           2
     south  |  Chevrolet  |      51300  |           2
     south  |    Hyundai  |      47860  |           3
     south  |      Mazda  |      41320  |           4
## Aggregate Functions
#### Have you ever heard the term "Running Total" or "Moving Average"? This is the basic premise of the aggregate window functions. These allow you to see the cumulative amounts or moving averages in each group. This method is very similar to the CUBE or ROLLUP Group By Extensions, though these provide a more sophisticated view of your data and tend to be more accurate.
## SUM
#### As mentioned above, this function is a more sophisticated version of the ROLLUP Group By Extension. This window function allows you to see the cumulative sum of values within a group over a period of time or a series of events.
#### Example:
    # For this example, we will be looking for the cumulative sum of sales by sales rep in each sales team.
    SELECT team, rep_id, rep_name, sales_amt, SUM(sales_amt) OVER(PARTITION BY team ORDER BY rep_name) running_total
    FROM team_sales
    ORDER BY team
##### Output:
    team  |    rep_id  |      rep_name  |      sales_amt  |  running_total
       A  |  16790130  |    Josh Smith  |         600.00  |         600.00
       A  |  15541210  |   Austin Dust  |         300.00  |         900.00
       A  |  15898820  | Beverly Starr  |         550.50  |        1450.50
       A  |  18790610  |    Clark Kent  |         130.75  |        1781.25
       B  |  17943280  |  Polly Carton  |         425.00  |         425.00
       B  |  13209930  | Patrick Johns  |        1050.70  |        1475.70
       B  |  19890410  |  Shelby Shark  |         215.00  |        1690.00
       B  |  19877610  |    John Adams  |         175.00  |        1865.00
## AVG
#### When working with metrics that are based on continuous measures rather than discrete, it can be daunting to calculate the moving average. To help solve this, the average window function allows us to see have averages within a group changes over time.
#### Example:
    # For this example, we will be comparing the moving average of wait times at different hospitals.
    SELECT hospital_name, date, wait_time, AVG(wait_time) OVER(PARTITION BY hospital_name ORDER BY date) moving_average
    FROM wait_times
    WHERE date BETWEEN '10-09-2021' AND '10-12-2021'
    ORDER BY hospital_name
##### Output:
        hospital_name  |         date  |  wait_time  |  moving_average
    St. Joins Central  |   10-09-2021  |      15.20  |           15.20
    St. Johns Central  |   10-10-2021  |      21.95  |           18.58
    St. Johns Central  |   10-11-2021  |      13.40  |           16.85
    St. Johns Central  |   10-12-2021  |      19.88  |           17.61
       St. Johns East  |   10-09-2021  |       8.71  |            8.71
       St. Johns East  |   10-10-2021  |      10.77  |            9.74
       St. Johns East  |   10-11-2021  |       5.44  |            8.31
       St. Johns East  |   10-12-2021  |       7.65  |            8.15
    St. Johns Central  |
