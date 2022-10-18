# Pandas DataFrames: Joins and Unions
## Introduction
#### <ins>This tutorial assumes the user has previous knowledge of Relational Databases.</ins> Just like in Relational Databases, Pandas allows you to join and union DataFrames to create comprehensive datasets using multiple DataFrames. In this tutorial, we will be going over the various types and methods of joins and how they differ from unions.
## The "Merge" Function
#### To join two DataFrames, you use the .merge function. The syntax for this function is described below:
    - pd.merge([name of the first dataframe], [name of second dataframe], how='[type of join]', left_on='[left key to join on]', right_on='[right key to match on]')
## Tables to be Used in the Examples:
#### To create a more cohesive tutorial, the following tables will be used:
### Product Table
![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip1.png)
### Customer Table
![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip2.png)
## Types of Joins
#### Just like in Relational Databases, Pandas allows you to join multiple DataFrames based on certain conditions. Listed below are the various types of joins allowed by Pandas:
### INNER
#### - This type of join returns all the columns from both DataFrames but only the rows that have matching keys.
    - Example: pd.merge(products, customers, how='inner', left_on='Product_ID', right_on='Product_ID')
#### Output: ![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip3.png)
### LEFT
#### - This type of join returns all the columns from both DataFrames and all the rows available from the left table. If there are rows that don't have matching keys, the column values will be marked as NaN (NumPy's version of NULL).
    - Example: pd.merge(products, customers, how='left', left_on='Product_ID', right_on='Product_ID')
#### Output: ![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip8.png)
### RIGHT
#### - This type of join is the complete opposite of the Left Join described above. It returns all the columns from both DataFrames and all the rows available from the right table. If there are rows that don't have matching keys, the column values will be marked as NaN.
    - Example: pd.merge(products, customers, how='right', left_on='Product_ID', right_on='Product_ID')
#### Output: ![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip9.png)
### FULL OUTER
#### - This is the least used type of join, mostly due to the fact that it usually doesn't serve any practical purpose. This returns all columns and rows from both DataFrames, whether or not they have matching keys. If there is no match between the keys, the column values will be marked as NaN.
    - Example: pd.merge(products, customers, how='outer', left_on='Product_ID', right_on='Product_ID')
#### Output: ![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip6-e1582610938663.png)
