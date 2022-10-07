# Pandas Overview
### Description
#### Pandas is a Python library that is widely used for data analysis, manipulation, and ingestion. Built on top of the NumPy Python library, Pandas includes a multitude of methods, classes, and data structures.
### Data Types
#### Just like Python, Pandas includes a variety of data types. Listed below are some of the more widely used data types:
    * String (str) - This consists of a collection of letters and numbers in a textual numbers.
          - Example: "This is a String!"
          - Example: "125 days since last accident."
    * Integer (int) - This is a whole number with no decimal points.
          - Example: 25
    * Float (float) - This is a number with x number of decimal places.
          - Example: 5.255
          - Example: 2.5
    * Boolean (bool) - This is a True or False statement.
          - Example: True
          - Example: False
### Data Structures
#### Also like Python, Pandas includes a variety of data structures, including dome of its own. Listed below are some commonly used data structures:
    * List - This consists of an assorted catalog of items with the SAME data type. The items in a list can be changed later 
             in the program.
          - Example: ['Apple', 'Banana', 'Orange']
          - Example: [5, 7, 85]
    * Tuple - This is the same as a list, except the values in the tuple CAN'T be changed later in the program.
          - Example: ('apple', 'banana', 'orange')
    * Dictionary - This is a list of values identified by a key value. These are used when creating Dataframes (see below).
          - Example: {'Apples': 55, 'Bananas': 30, 'Oranges': 20}
    * Series - This is a one-dimensional data structure that is formed in the shape of a vertical list or column.
          - Example: 'Apple'
                     'Banana'
                     'Orange'
    * DataFrame - This is a two-dimensional data structure that is formed in the shape of a basic table. These can include 
                  indexes to reference specific items (shown below in the brackets). These are the most common data structure 
                  used in Pandas.
          - Example: 'Store'  'Apples' 'Bananas' 'Oranges'
                [0]  'Orem'   55       30        20
                [1]  'Provo'  30       55        20
                [2]  'Lindon' 20       30        55
### Data Manipulation Techniques
#### Pandas offers hundreds of different techniques to analyze and manipulate data. In this section, I'll give a breif overview of some of the techniques used in the Example project with some code samples. TO FOLLOW ALONG, SIMPLY COPY THE CODE SAMPLES INTO A JUPYTER NOTEBOOK.
      * Change Data Types
            - At times, you want to convert a column's data type to save RAM, create a calculation, 
              or use a field as a dimension in a Data Visualization. To change a column's data type, 
              complete the following steps:
                  0. If you haven't installed Pandas yet:
                        pip install pandas
                     If you have installed Pandas copy and paste the code sample below into a Jupyter Notebook.
                  1. Create dictionary for data to add to the dataframe
                  2. Create the dataframe
                  3. Call the dataframe column as set it to a new value by using the "astype" method
                  CODE SAMPLE:
                     import pandas as pd
                     
                     # Create dictionary for data to add to the dataframe
                     data = {'Store': ['Orem', 'Provo', 'Lindon'], 'Item': ['Apple', 'Banana', 'Orange'], 'Price': [2, 3, 4]}
                     
                     # create the dataframe
                     df = pd.DataFrame(data=data)
                     
                     # change the Price column's data type
                     df['Price'] = df['Price'].astype(float)
                     
                     # preview new dataframe
                     df
       * Join Dataframes
            - Just like in a database, joining tables (or in this case, dataframes) is a great way to get related data from 
              multiple sources. To join two dataframes, complete the following steps:
              0. If you haven't installed Pandas yet:
                    pip install pandas
                 If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
              1. Create dictionaries for data to add to the dataframes.
              2. Create the dataframes.
              3. Join dataframes by calling the "merge" method.
              SYNTAX: df.merge([second dataframe], how='[type of join]', left_on='[primary key]', right_on='[foreign key]'
              CODE SAMPLE:
                  import pandas as pd
                  
                  # create dictionaries to hold the data
                  data1 = {'Store': ['Orem', 'Provo', 'Lindon'], 'Item': ['Apple', 'Banana', 'Orange'], 'Price': [2.0, 3.0, 4.0]}
                  data2 = {'Store': ['Orem', 'Provo', 'Lindon'], 'Item': ['Grapes', 'Strawberries', 'Mangoes'], 'Price': [1.25, 0.85, 4.75]}
                  
                  # create the dataframes
                  df1 = pd.DataFrame(data=data1)
                  df2 = pd.DataFrame(data=data2)
                  
                  # join the dataframes
                  df = df1.merge(df2, how='inner', left_on='Store', right_on='Store')
                  df
      * Union Dataframes
            - Just like in SQL, you can union two queries or tables to combine the results, whether or not they match a key.
              To union two dataframes, complete the following steps:
              0. If you haven't installed Pandas yet:
                    pip install pandas
                 If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
              1. Create dictionaries for data to add to the dataframes.
              2. Create the dataframes.
              3. Union the dataframes by calling the "concat" method.
              SYNTAX: .concat([list of dataframes])
              CODE SAMPLE
                  import pandas as pd
                  
                  # create dictionaries for data to add to the dataframes
                  data1 = {'Store': ['Orem', 'Provo', 'Lindon'], 'Item': ['Apple', 'Banana', 'Orange'], 'Price': [2.0, 3.0, 4.0]}
                  data2 = {'Store': ['Draper', 'Sandy', 'Murray'], 'Item': ['Grapes', 'Strawberries', 'Mangoes'], 'Price': [1.25, 0.85, 4.75]}
                  
                  # create the dataframes
                  df1 = pd.DataFrame(data=data1)
                  df2 = pd.DataFrame(data=data2)
                  
                  # union the dataframes
                  df = pd.concat([df1, df2])
                  df
      * Query a Dataframe
            - The most commonly used tool in data analysis is querying. This involves writing out a statement 
              to specify the columns to view, row conditions, and the sorting order. To query a dataframe,
              complete the following steps:
              0. If you haven't installed Pandas yet:
                    pip install pandas
                 If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
              1. Create the dictionary to hold the data.
              2. Create the dataframe.
              3. Query the dataframe by calling the "loc" method
              SYNTAX: df.loc([row condition], [columns to show])
              CODE SAMPLE:
              
              # create the dictionary to hold the data
              data = {'Store':['Orem', 'Orem', 'Orem', 'Provo', 'Provo', 'Lindon'], 'Item':['Apple','Banana','Orange','Apple','Banana','Orange'], 'Price':[4.0, 5.25, 6.0, 7.25, 8.0, 1.25]}
              
              # create the dataframe
              df = pd.DataFrame(data=data)
              
              # query the dataframe
              df.loc[df['Store'] == 'Provo', :]
      * Append Rows to a Dataframe
            - Dataframes are anything but static, thus allowing you to alter them whenever you like. To add new rows
              to a dataframe, complete the following steps:
              0. If you haven't installed Pandas yet:
                    pip install pandas
                 If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
              1. Create the dictionary to hold the data.
              2. Create the dataframe.
              3. Add new rows to the dataframe by calling the "append" method.
              SYNTAX: df.append({'[column1]':[value], '[column2]':[value], '[column3]':[value]}, ignore_index=True)
              CODE SAMPLE:
              
              # create the dictionary to hold the data
              data = {'Store':['Orem', 'Provo', 'Lindon'], 'Item':['Apple', 'Banana', 'Orange'], 'Price':[0.55, 0.95, 1.05]}
              
              # create the dataframe
              df = pd.DataFrame(data=data)
              
              # add new row to the dataframe
              df.append({'Store':'Orem', 'Item':'Grapes', 'Price': 2.25}, ignore_index=True)
