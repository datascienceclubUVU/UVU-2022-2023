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
    FROM department_sales
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
    SELECT make, model, drivetrain, SUM(sales) vehicle_sales
    FROM vehicle_inventory
    GROUP BY CUBE(make, model, drivetrain)
##### Output:
    make  |  model  |  drivetrain  |  vehicle_sales
     Ford |   F-150 |          4WD |           545000
     Ford |   F-150 |          RWD |           200000
     Ford |  Ranger |          4WD |           185000
     Ford |  Ranger |          RWD |            70000
     NULL |   NULL  |          4WD |           730000  * This shows the total sales for all 4WD models
     NULL |   NULL  |          RWD |           270000  * This shows the total sales for all RWD models
     Ford |   F-150 |         NULL |           745000  * This shows the total sales for the Ford F-150
     Ford |  Ranger |         NULL |           255000  * This shows the total sales for the Ford Ranger
     Ford |   NULL  |         NULL |          1000000  * This shows the total sales for the "Ford" make
### ROLLUP with GROUPING_ID
#### To help identify which grouping set you're viewing, SQL offers the GROUPING_ID function that is used in conjunction with the ROLLUP extension. This extension has the following syntax:
    SELECT [column_name], [column_name], [aggregate_function]([column_name]) [new_column name], 
           GROUPING_ID([column_name], [column_name]) [new_column_name]
    FROM [table_name]
    GROUP BY ROLLUP([column_name], [column_name])
#### Example
##### In the example below, we will be using the same data as the first ROLLUP example:
    SELECT department_name, category, SUM(sales) cum_sales, GROUPING_ID(department_name, category)
    FROM department_sales
    GROUP BY ROLLUP(department_name, category)
##### Output
    department_name  |  category  |  cum_sales  |  grouping_id
             baking  |     sugar  |      10000  |            0
             baking  |       oil  |       8500  |            0 *These rows show the first level of detail
             baking  | pots/pans  |       3000  |            0
         automotive  |       oil  |       4500  |            0
            cookies  |     sugar  |       2500  |            0
               NULL  |     sugar  |      12500  |            1 *These rows show the second level of detail
               NULL  |       oil  |      13000  |            1
               NULL  |      NULL  |      28500  |            3 *This row displays the third level of detail
### GROUPING SETS
#### The GROUPING SETS extension is almost identical to the CUBE extension, except that you can specify which levels of detail you would like to include in the output. This extension has the following syntax:
    SELECT [column_name], [column_name], [aggregate_function]([column_name]) [new_column_name]
    FROM [table_name]
    GROUP BY GROUPING SETS([column_name], ([column_name], [column_name], ()) * This syntax can be changed depending on your needs
#### Example
##### In the example below, we will be using the same data as the first ROLLUP example:
    SELECT department_name, category, SUM(sales) cum_sales
    FROM department_sales
    GROUP BY GROUPING SETS(department_name, category, (department_name, category), ())
##### Output
    department_name  |  category  |  cum_sales
             baking  |     sugar  |      10000 
             baking  |       oil  |       8500  *These rows show the first level of detail
             baking  | pots/pans  |       3000
             baking  |      NULL  |      21500  *These rows show the second level of detail
         automotive  |       oil  |       4500
         automotive  |      NULL  |       4500 
            cookies  |     sugar  |       2500
            cookies  |      NULL  |       2500
               NULL  |     sugar  |      12500  *These rows show the second level of detail
               NULL  |       oil  |      13000
               NULL  | pots/pans  |       3000
               NULL  |      NULL  |      28500  *This row displays the third level of detail
## Next Steps
### Now that you know the analytical potential of SQL, let's take a deep dive into how developers use SQL to complete Data Science and Engineering tasks:
- [Windowing Functions](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/Windowing%20Functions.md)
