# Pandas DataFrames: Filtering Techniques
## Introduction
#### When working with large amounts of data, filtering can be a saving grace in your querying practices. Pandas offers multiple options for how to filter your DataFrames, ranging from simple methods to advanced conditional statements. Let's take a look at what Pandas has to offer:
## DataFrames Used in This Tutorial
#### To help keep this tutorial consistent, we will be using the "products" and "customers" DataFrames as shown below:
### products
![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip1.png)
### customers
![This is an image!](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/jip2.png)
## Common Filtering Techniques
### Previewing a DataFrame
#### - When you are working with "larger than memory" DataFrames, it may be helpful to simply preview the first or last few rows. To do this, we can utilize Pandas' head() and tail() methods. These methods use the following syntaxes:
    - [dataframe name].head([# of rows]*)
    - [dataframe name].tail([# of rows]*)
        * If you don't specify a number of rows, Pandas will return a default of five rows. 
#### Examples:
##### products.head()
  ![This is an image!](Pictures/products.head.png)
##### customers.tail(3)
  ![This is an image!](Pictures/customers.tail.png)
### Filtering Using the .loc Method
#### - Similar to SQL, Pandas allows you to specify the columns to return and limit the rows to return based on certain conditions. We can complete these actions in Pandas by using the loc[] method. This method uses the following syntax:
    - [dataframe name].loc[[row conditions]*, [columns to return]**)[[start index]:[end index]]***
        * This is equivalent to the WHERE clause in SQL. See the examples below to understand the unique syntaxes.
        ** This is optional. If left empty, Pandas will return all columns. 
           To specify the columns to return, simply put the column names in a list.
        *** This is optional. This is used to specify the number of rows in the resulting query to return.
#### Examples:
##### products.loc[products['Category'] == 'Electronics', 
