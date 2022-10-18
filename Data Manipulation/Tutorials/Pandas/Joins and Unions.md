# Pandas DataFrames: Joins and Unions
## Introduction
#### <ins>This tutorial assumes the user has previous knowledge of Relational Databases.</ins>Just like in Relational Databases, Pandas allows you to join and union DataFrames to create comprehensive datasets using multiple DataFrames. In this tutorial, we will be going over the various types and methods of joins and how they differ from unions.
## The "Merge" Function
#### To join two DataFrames, you use the .merge function. The syntax for this function is described below:
    - df.merge([name of second dataframe], how='[type of join]', left_on='[left key to join on]', right_on='[right key to match on]')
## Types of Joins
#### Just like in Relational Databases, Pandas allows you to join multiple DataFrames based on certain conditions. Listed below are the various types of joins allowed by Pandas:
  #### - Inner: This type of join returns values from the original DataFrame that have matching records in the new DataFrame.
      - Example: df1.merge(df2, how='inner', left_on='id', right_on='customerID')
