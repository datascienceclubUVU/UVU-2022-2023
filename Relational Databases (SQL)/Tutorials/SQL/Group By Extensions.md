# Intermediate SQL: Group By Extensions
## Introduction
#### When you are aggregating data, it's helpful to alter the level of detail to look at the different layers of analysis. Since SQL has been around for nearly 50 years, many level of detail extensions have been added including the following:
  - ROLLUP
  - CUBE
  - GROUPING_ID
  - GROUPING_SETS
## Group By Extensions Explained
#### As mentioned above, there are four primary extensions to the GROUP BY clause of a SQL statement. In this section, we will take a closer look at each of them:
### ROLLUP
#### The ROLLUP extension is primarily used to look at the cumulative aggregation either over a period of time or over different categories/groups. This extension has the following syntax:
    SELECT [column_name], [column_name], [aggregate_function]([column_name]) [new_column_name]
    FROM [table_name]
    GROUP BY ROLLUP([column_name], [column_name])
#### Example
##### In the example below, we will be looking at the cumulative sales by different departments and product categories in a store:
    SELECT department_name, category, SUM(sales) cum_sales
    FROM sales_totals
    GROUP BY ROLLUP(department_name, category)
##### Output:
    department_name  |  category  |  cum_sales
             baking  |     sugar  |      10000
             baking  |       oil  |       8500
             baking  | pots/pans  |       3000
               NULL  |      NULL  |      21500  *The NULLs in the categorical columns indicate the overall total
### CUBE
#### The CUBE extension enables you to look at every combination of data. This is a great tool for looking at aggregations between categories at various levels of detail. This extension has the following syntax:
    SELECT [column_name], [column_name], [aggregate_function]([column_name]) [new_column_name]
    FROM [table_name]
    GROUP BY CUBE([column_name], [column_name])
#### Example
##### In the example below, we will be looking at the sales by different car makes, models, and drivetrains:
