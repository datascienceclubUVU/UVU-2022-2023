# Introduction to SQL Aggregate Functions
## Description
#### _Aggregate Functions_ allow you to alter the level of detail within a database query to view basic statistics within specified groups. All aggregate functions are used in conjunction with the GROUP BY clause (See [Basic SQL Statements](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/Basic%20SQL%20Statements.md))
## Aggregate Functions
#### The most common aggregate functions used in SQL include SUM, AVG (Average), COUNT, MIN, and MAX. These are described in more detail below:
### SUM
##### The _SUM_ function is used to add together the values of specified columns in order to collect a total. This is useful for comparing items across groups (e.g., sales by state) and identifying anomalies in your data.
    - Example (find the gross sales amount per state that isn't Puerto Rico):
    SELECT state, SUM(sales) gross_sales
    FROM dbo.sales
    WHERE state != 'Puerto Rico'
    GROUP BY state
    ORDER BY gross_sales DESC
    
    Results:
          state     |   gross_sales
    [1]  California   559080.97
    [2]  Texas        521399.00
    [3]  Ohio         389773.22
    [4]  Arizona      344787.19
    ...
### AVG (Average)
##### The _AVG_ function calculates the sum of each specified column and then divides that values by the number of rows in each group. This is useful for finding trends in your data.
    - Example (Find the average sales per state by month between 2019 and 2021):
    SELECT state, month, AVG(sales) avg_sales
    FROM dbo.sales
    WHERE year BETWEEN 2019 AND 2021
    GROUP BY state, month
    
    Results:
          state     |  month     |   avg_sales
    [1]  Texas        January      27880.00
    [2]  Texas        February     29399.13
    [3]  Texas        March        29887.66
    [4]  Texas        April        34581.11
    ...
### COUNT
##### The _COUNT_ function simply counts the number of rows in a specified group. This is useful to identify metrics such as # of transactions per store, # of employees on a given shift, etc.
    - Example (find the number of stores in each state):
    SELECT state, COUNT(DISTINCT store_name) num_stores
    FROM dbo.store_info
    GROUP BY state
    ORDER BY num_stores DESC
    
    Results:
          state     |   num_stores
    [1]  California   47
    [2]  Texas        44
    [3]  Arizona      29
    [4]  Ohio         26    
    ...
### MIN
##### The _MIN_ function finds the smallest value in the column within the specified group. This is useful to analyze the impacts of economic uncertainty and other factors that may impact store sales within a given time period.
    - Example (find the lowest price of bananas across each store):
    SELECT store_name, product_name, MIN(item_price) lowest_price
    FROM dbo.product_info
    WHERE product_name = 'Bananas (by lb.)'
    GROUP BY store_name, product_name
    ORDER BY lowest_price
    
    Results:
          store_name       |   product_name     |  lowest_price
    [1]  U-Mart - Phoenix     Bananas (by lb.)     0.55
    [2]  P-Mart - Akron       Bananas (by lb.)     0.59
    [3]  L-Mart - Lincoln     Bananas (by lb.)     0.63
    [4]  B-Mart - Detroit     Bananas (by lb.)     0.67
    ...
### MAX
##### The _MAX_ function finds the largest value in the column within the specified group. This is useful for identifying high performing employees and visualizing trends across product growth.
    - Example (find the most expensive item in each store):
    SELECT store_name, product_name, MAX(item_price) highest_price
    FROM dbo.product_info
    GROUP BY store_name, product_name
    ORDER BY highest_price DESC
    
    Results:
          store_name              |   product_name            |  highest_price
    [1]  R-Mart - Los Angeles        Concrete (100 lb.)         469.55
    [2]  I-Mart - Newark             Plywood (15 Sheets)        415.99
    [3]  T-Mart - Salt Lake City     Plastic Shed (12'x17')     400.50
    [4]  S-Mart - Phoenix            HD Touch Mirror (12")      299.99
    ...
 ### Next Steps
 ##### If you enjoyed this tutorial, you've got to check these out:
 - [SQL Best Practices](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/SQL%20Best%20Practices.md)
 - [CTEs](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/CTEs.md)
 - [Subqueries](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/Subqueries.md)
