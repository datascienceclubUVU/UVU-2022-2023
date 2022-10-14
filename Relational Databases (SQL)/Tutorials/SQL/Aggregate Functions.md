# Introduction to SQL Aggregate Functions
## Description
#### _Aggregate Functions_ allow you to alter the level of detail within a database query to view basic statistics within specified groups. All aggregate functions are used in conjunction with the GROUP BY clause (See [Basic SQL Statements](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/Basic%20SQL%20Statements.md))
## Aggregate Functions
#### The most common aggregate functions used in SQL include SUM, AVG (Average), MIN, MAX, and COUNT. These are described in more detail below:
### SUM
##### The _SUM_ function is used to add together the values of specified columns in order to collect a total. This is useful for comparing items across groups (e.g., sales by state) and identifying anomalies in your data.
    - Example:
    SELECT state, SUM(sales) gross_sales
    FROM dbo.sales
    WHERE state != 'Puerto Rico'
    GROUP BY state
    ORDER BY gross_sales
    
    Results:
          state     |   gross_sales
    [1]  California   559080.97
    [2]  Texas        521399.00
    [3]  Ohio         389773.22
    [4]  Arizona      344787.19
    ...
### AVG (Average)
##### The _AVG_ function calculates the sum of each specified column and then divides that values by the number of rows in each group. This is useful for finding trends in your data.
    - Example:
    SELECT state, month, AVG(sales) avg_sales
    FROM dbo.sales
    WHERE year BETWEEN 2019 AND 2021
    GROUP BY state, month
    ORDER BY avg_sales
    
    Results:
          state     |  month     |   avg_sales
    [1]  Texas        January      27880.00
    [2]  Texas        February     29399.13
    [3]  Texas        March        29887.66
    [4]  Texas        April        34581.11
