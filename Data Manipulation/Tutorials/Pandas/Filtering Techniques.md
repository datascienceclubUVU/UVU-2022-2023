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
  1. ![This is an image!](C:/Users/Chase/OneDrive/Pictures/products.head.png)
