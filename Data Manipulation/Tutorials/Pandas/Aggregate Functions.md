# Pandas DataFrames: Aggregate Functions
## Introduction
#### When conducting data analyses, we soemtimes want to shift between levels of detail to look at the data from different perspectives. One way Pandas offers this functionality is by providing Aggregate Functions. The various aggregate functions provided by Pandas are listed and described below.
## DataFrames Used in This Tutorial
#### To keep the examples in this tutorial consistent, we will be using the following DataFrame:
#### vehicles
![This is an image](Pictures/vehicle_dataframe.png)
## Commonly Used Aggregate Functions
### count()
#### - Just like in Excel and SQL, this function is used to count the number of items within a specified group. In the context of DataFrames, you need to group categorical columns (where there are discrete values) and aggregate by a numerical column. To use this function, use the following syntax:
    [dataframe name].groupby([categorical column name])[[value column name]].aggregate('count')
#### Example:
    vehicles.groupby('Type')['Price'].aggregate('count')
![This is an image](Pictures/vehicle_count.png)
### sum()
#### - This is the most basic aggregate function used for analysis. This function is used to add together all the values of the numerical column within each category from the categorical column. To use this function, use the following syntax:
    [dataframe name].groupby([categorical column name])[[value column name]].aggregate('sum')
#### Example:
    vehicles.groupby('Type')['Price'].aggregate('sum')
![This is an image](Pictures/vehicle_sum.png)
