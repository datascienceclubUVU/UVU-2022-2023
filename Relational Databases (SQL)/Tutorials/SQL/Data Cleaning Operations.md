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
#### The CAST and CONVERT functions allow you to input a column and temporarily change it's data type. There is, however, some caveats with these functions:
    - You
