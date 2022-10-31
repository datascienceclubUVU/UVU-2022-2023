# Advanced SQL: Data Cleaning Operations
## Introduction
#### As a Data Analyst, you won't be always working with pristine data. Due to this fact, it never hurts to learn basic data cleaning operations. The term **_data cleaning_** refers to preparing the data for analysis and making the changes to the data dynamic enough to change between use cases and reversible to return to its normal form. Listed below are some of the various data cleaning operations we will cover in this tutorial:
    - Temporary Data Type Conversion
    - Trimming Strings
    - Extracting Substrings
    - Concatenation
    - Extracting Parts of a Date
    - Coalesce Prodecures
## Temporary Data Type Conversion
#### When working with aggregate functions, the numeric precision can be the difference between "almost correct" and accurate. To help with this procedure, SQL provides two identical functions: CAST and CONVERT.
### Useful Functions
#### The CAST and CONVERT functions allow you to input a column and temporarily change it's data type. However, only certain types of conversions are allowed. Listed below as a list of the most common data type conversions allowed:
    - INT to VARCHAR/CHAR
    - FLOAT to VARCHAR/CHAR
    - INT to FLOAT
    - FLOAT to MONEY
    - VARCHAR/CHAR to DATETIME (Only if the string is similar to a date format)
#### Because there are so many types of conversions possible, here is a link for more details: [Click Here](https://www.mssqltips.com/sqlservertip/6874/sql-cast-function-for-data-type-conversions/). Due to the compelx nature of temporary data type conversion, it's recommended that you use the TRY_CAST or TRY_CONVERT functions instead. These functions have the following syntaxes:
    TRY_CAST([column OR value] AS [data type])
    TRY_CONVERT([data type], [column OR value])
## Trimming Strings
#### When working with large data pipelines that ingest terabytes of information daily, the strings provided may include some unwanted spaces and/or characters. To help with this process, SQL Server and many other RDBMSs offer the following functions:
    - TRIM([column]) -- This removes all leading and trailing spaces
    - LTRIM([column]) -- This removes only leading spaces
    - RTRIM([column]) -- This removes only trailing spaces
    - LEFT([column], [number of characters]) -- This returns only the number of characters specified 
                                                starting from the left side of the string
    - RIGHT([column], [number of characters]) -- This returns only the number of characters specified
                                                 starting from the right side of the string
#### Trimming strings is a very common task invovled with data analysis and manipulation and should be practiced on a regular basis. Although these functions seem to be very simple, they tend to be very inefficient. Because of this, it's useful to understand how to extract substrings.
