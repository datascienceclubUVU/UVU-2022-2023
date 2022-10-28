# Advanced SQL: Window Functions
## Introduction
#### One of the most common methods to analyze large amounts of data is to partition the data into individual groups. This can be done using various **_Window Functions_**. A **_Window Function_** splits the data into individual groups based on a specified boundary (e.g., id, name, date). These are widely used for creating rolling functions, grouping data without changing the level of detail, and making it easier to identify potential duplicates. Let's take a closer look at the different types of windowing functions:
## Types of Window Functions
#### As you might expect, there are several window functions available in SQL. These include the following:
    - ROW_NUMBER
    - RANK
    - DENSE_RANK
    - SUM 
    - AVG
    - LAG
    - LEAD
    - FIRST_VALUE
    - LAST_VALUE
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
    WITH customer_orders AS 
    (SELECT id AS customer_id, first_name, last_name, order_amt, num_items, order_date, order_id, 
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
### SUM
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
### AVG
#### When working with metrics that are based on continuous measures rather than discrete, it can be daunting to calculate the moving average. To help solve this, the average window function allows us to see have averages within a group changes over time.
#### Example:
    # For this example, we will be comparing the moving average of wait times at different hospitals.
    SELECT hospital_name, date, wait_time, AVG(wait_time) OVER(PARTITION BY hospital_name ORDER BY date) moving_average
    FROM wait_times
    WHERE date BETWEEN '10-09-2021' AND '10-12-2021'
    ORDER BY hospital_name, date
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
## Comparison Functions
#### Have you ever wondered how stock brokers get rich fast? They take past data and compare it with current data. This is the basic premise of comparison window functions. It takes the current row value and compares it with either the first value, last value, previous value, or future value in the group.
### LAG
#### As mentioned above, stock brokers compare past data with current data to predict future outcomes. This is the basic premise of the LAG function. It simply takes the value of the previous row and compares it with the current row.
#### Example:
    # For this example, we will compare the stocks of a company over time and compare the past and present values.
    SELECT company_lbl, date, stock_price, LAG(stock_price, 1) OVER(PARTITION BY company_lbl ORDER BY date) yesterday_price
    FROM stock_prices
    WHERE date BETWEEN '7-01-2022' AND '7-04-2022'
    ORDER BY company_lbl, date
##### Output:
    company_lbl  |       date  |  stock_price  |  yesterday_price
           TSLA  |  7-01-2022  |        75.80  |             NULL
           TSLA  |  7-02-2022  |        77.50  |            75.80
           TSLA  |  7-03-2022  |        72.35  |            77.50
           TSLA  |  7-04-2022  |        65.88  |            72.35
           AAPL  |  7-01-2022  |       102.44  |             NULL
           AAPL  |  7-02-2022  |        99.09  |           102.44
           AAPL  |  7-03-2022  |       105.97  |            99.09
           AAPL  |  7-04-2022  |       112.90  |           105.97
### LEAD
#### As you might imagine, the LEAD function does the complete opposite of the LAG function. Rather than comparing previous values with current values, the LEAD function compares current values with future values.
#### Example:
    # We will be using the same query as the LAG example.
    SELECT company_lbl, date, stock_price, LEAD(stock_price, 1) OVER(PARTITION BY company_lbl ORDER BY date) yesterday_price
    FROM stock_prices
    WHERE date BETWEEN '7-01-2022' AND '7-04-2022'
    ORDER BY company_lbl DESC, date
##### Output:
    company_lbl  |       date  |  stock_price  |  yesterday_price
           TSLA  |  7-01-2022  |        75.80  |            77.50
           TSLA  |  7-02-2022  |        77.50  |            72.35
           TSLA  |  7-03-2022  |        72.35  |            65.88
           TSLA  |  7-04-2022  |        65.88  |             NULL
           AAPL  |  7-01-2022  |       102.44  |            99.09
           AAPL  |  7-02-2022  |        99.09  |           105.97
           AAPL  |  7-03-2022  |       105.97  |           112.90
           AAPL  |  7-04-2022  |       112.90  |             NULL
### FIRST_VALUE
#### When comparing items within a specified partition, it may be useful to reference a specific item the the partition as a column value rather than having to scroll up or down to see the value to be compared. To help with this, the FIRST_VALUE function finds the first value in the partition and repeats the value in the new column to make comparisons easier.
#### Example:
    # We will be using the same query as the LAG example to find the difference between stocks.
    WITH first_values AS (
    SELECT company_lbl, date, stock_price, FIRST_VALUE(stock_price) OVER(PARTITION BY company_lbl ORDER BY date) first_price
    FROM stcok_prices
    WHERE date BETWEEN '7-01-2022' AND '7-04-2022'),
    
    price_difference AS (
    SELECT fv.*, SUM(stock_price - first_price) AS price_difference 
    FROM first_values fv
    ORDER BY company_lbl, date
##### Output:
    company_lbl  |       date  |  stock_price  |  first_price  |  price_difference
           TSLA  |  7-01-2022  |        75.80  |        75.80  |              0.00
           TSLA  |  7-02-2022  |        77.50  |        75.80  |              1.70
           TSLA  |  7-03-2022  |        72.35  |        75.80  |             -3.45
           TSLA  |  7-04-2022  |        65.88  |        75.80  |             -9.92
           AAPL  |  7-01-2022  |       102.44  |       102.44  |              0.00
           AAPL  |  7-02-2022  |        99.09  |       102.44  |             -3.35
           AAPL  |  7-03-2022  |       105.97  |       102.44  |             -3.53
           AAPL  |  7-04-2022  |       112.90  |       102.44  |             10.46
### LAST_VALUE
#### The LAST_VALUE function does the complete opposite of the FIRST_VALUE function, it simply finds the last value in a partition and repeats in as the column value.
#### Example:
    # We will be using the same query as the LAG example to find the difference between stocks.
    WITH last_values AS (
    SELECT company_lbl, date, stock_price, LAST_VALUE(stock_price) OVER(PARTITION BY company_lbl ORDER BY date) last_price
    FROM stcok_prices
    WHERE date BETWEEN '7-01-2022' AND '7-04-2022'),
    
    price_difference AS (
    SELECT lv.*, SUM(stock_price - last_price) AS price_difference 
    FROM last_values lv
    ORDER BY company_lbl, date
##### Output:
    company_lbl  |       date  |  stock_price  |   last_price  |  price_difference
           TSLA  |  7-01-2022  |        75.80  |        65.88  |              9.92
           TSLA  |  7-02-2022  |        77.50  |        65.88  |             11.62
           TSLA  |  7-03-2022  |        72.35  |        65.88  |              6.47
           TSLA  |  7-04-2022  |        65.88  |        65.88  |              0.00
           AAPL  |  7-01-2022  |       102.44  |       112.90  |            -10.46
           AAPL  |  7-02-2022  |        99.09  |       112.90  |            -13.81
           AAPL  |  7-03-2022  |       105.97  |       112.90  |             -6.93
           AAPL  |  7-04-2022  |       112.90  |       112.90  |              0.00
