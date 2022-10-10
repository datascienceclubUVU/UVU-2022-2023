# Pandas Overview
### <ins>Description</ins>
#### Pandas is a Python library that is widely used for data analysis, manipulation, and ingestion. Built on top of the NumPy Python library, Pandas includes a multitude of methods, classes, and data structures.
### <ins>Data Types</ins>
#### Just like Python, Pandas includes a variety of data types. Listed below are some of the more widely used data types:
#### <i>String (str)</i> 
##### - This consists of a collection of letters and numbers in a textual numbers.
          - Example: "This is a string!"
          - Example: "125 days since last accident."
#### <i>Integer (int)</i> 
##### - This is a whole number with no decimal points.
          - Example: 25
#### <i>Float (float)</i> 
##### - This is a number with x number of decimal places.
          - Example: 5.255
          - Example: 2.5
#### <i>Boolean (bool)</i> 
##### - This is a True or False statement.
          - Example: True
          - Example: False
### <ins>Data Structures</ins>
#### Also like Python, Pandas includes a variety of data structures, including dome of its own. Listed below are some commonly used data structures:
#### <i>List</i> 
##### - This consists of an assorted catalog of items with the SAME data type. The items in a list can be changed later in the program.
          - Example: ['Apple', 'Banana', 'Orange']
          - Example: [5, 7, 85]
#### <i>Tuple</i> 
##### - This is the same as a list, except the values in the tuple CAN'T be changed later in the program.
          - Example: ('apple', 'banana', 'orange')
#### <i>Dictionary</i> 
##### - This is a list of values identified by a key value. These are used when creating Dataframes (see below).
          - Example: {'Apples': 55, 'Bananas': 30, 'Oranges': 20}
#### <i>Series</i> 
##### - This is a one-dimensional data structure that is formed in the shape of a vertical list or column.
          - Example: 'Apple'
                     'Banana'
                     'Orange'
#### <i>DataFrame</i> 
##### - This is a two-dimensional data structure that is formed in the shape of a basic table. These can include indexes to reference specific items (shown below in the brackets). These are the most common data structure used in Pandas.
          - Example: 'Store'  'Apples' 'Bananas' 'Oranges'
                [0]  'Orem'   55       30        20
                [1]  'Provo'  30       55        20
                [2]  'Lindon' 20       30        55
### <ins>Data Manipulation Techniques</ins>
#### Pandas offers hundreds of different techniques to analyze and manipulate data. In this section, I'll give a breif overview of some of the techniques used in the Example project with some code samples. TO FOLLOW ALONG, SIMPLY COPY THE CODE SAMPLES INTO A JUPYTER NOTEBOOK.
#### <i>Change Data Types</i>
##### - At times, you want to convert a column's data type to save RAM, create a calculation, or use a field as a dimension in a Data Visualization. To change a column's data type, complete the following steps:
#### If you haven't installed Pandas yet:
      pip install pandas
#### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Create dictionary for data to add to the dataframe
##### 2. Create the dataframe
##### 3. Call the dataframe column as set it to a new value by using the "astype" method 
##### CODE SAMPLE: 
   
      import pandas as pd

      # Create dictionary for data to add to the dataframe
      data = {'Store': ['Orem', 'Provo', 'Lindon'], 'Item': ['Apple', 'Banana', 'Orange'], 'Price': [2, 3, 4]}

      # create the dataframe
      df = pd.DataFrame(data=data)

      # change the Price column's data type
      df['Price'] = df['Price'].astype(float)

      # preview new dataframe
      df
#### <i>Join Dataframes</i>
##### - Just like in a database, joining tables (or in this case, dataframes) is a great way to get related data from multiple sources. To join two dataframes, complete the following steps:
#### If you haven't installed Pandas yet:
        pip install pandas
#### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Create dictionaries for data to add to the dataframes.
##### 2. Create the dataframes.
##### 3. Join dataframes by calling the "merge" method.
##### SYNTAX: df.merge([second dataframe], how='[type of join]', left_on='[primary key]', right_on='[foreign key]'
##### CODE SAMPLE:
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
#### <i>Union Dataframes</i>
##### - Just like in SQL, you can union two queries or tables to combine the results, whether or not they match a key. To union two dataframes, complete the following steps:
#### If you haven't installed Pandas yet:
        pip install pandas
#### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Create dictionaries for data to add to the dataframes.
##### 2. Create the dataframes.
##### 3. Union the dataframes by calling the "concat" method.
##### SYNTAX: pd.concat([list of dataframes])
##### CODE SAMPLE
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
#### <i>Query a Dataframe</i>
##### - The most commonly used tool in data analysis is querying. This involves writing out a statement to specify the columns to view, row conditions, and the sorting order. To query a dataframe, complete the following steps:
#### If you haven't installed Pandas yet:
        pip install pandas
#### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Create the dictionary to hold the data.
##### 2. Create the dataframe.
##### 3. Query the dataframe by calling the "loc" method
##### SYNTAX: df.loc([row condition], [columns to show])
##### CODE SAMPLE:
     import pandas as pd

     # create the dictionary to hold the data
     data = {'Store':['Orem', 'Orem', 'Orem', 'Provo', 'Provo', 'Lindon'], 'Item':['Apple','Banana','Orange','Apple','Banana','Orange'], 'Price':[4.0, 5.25, 6.0, 7.25, 8.0, 1.25]}

     # create the dataframe
     df = pd.DataFrame(data=data)

     # query the dataframe
     df.loc[df['Store'] == 'Provo', :]
#### <i>Append Rows to a Dataframe</i>
##### - Dataframes are anything but static, thus allowing you to alter them whenever you like. To add new rows to a dataframe, complete the following steps:
#### If you haven't installed Pandas yet:
        pip install pandas
#### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Create the dictionary to hold the data.
##### 2. Create the dataframe.
##### 3. Add new rows to the dataframe by calling the "append" method.
##### SYNTAX: df.append({'[column1]':[value], '[column2]':[value], '[column3]':[value]}, ignore_index=True)
##### CODE SAMPLE:
     import pandas as pd

     # create the dictionary to hold the data
     data = {'Store':['Orem', 'Provo', 'Lindon'], 'Item':['Apple', 'Banana', 'Orange'], 'Price':[0.55, 0.95, 1.05]}

     # create the dataframe
     df = pd.DataFrame(data=data)

     # add new row to the dataframe
     df.append({'Store':'Orem', 'Item':'Grapes', 'Price': 2.25}, ignore_index=True)
#### <i>Unpivot Columns in a Dataframe</i>
##### - Sometimes, dataframes contain a large number of columns that can get in the way of an efficient query. To solve this problem, we can unpivot the column names and values into only two columns. To unpivotmultiple columns in a dataframe, complete the following steps:
#### If you haven't installed Pandas yet:
        pip install pandas
##### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Create the dictionary to hold the data.
##### 2. Create the dataframe.
##### 3. Unpivot the columns and aggregate the values by calling the "melt" method.
##### SYNTAX: pd.melt([dataframe], id_vars='[list of columns to NOT unpivot]', var_name='[name of new column to hold column names]', 
       value_name='[name of new column to hold column values]', value_vars='[list of columns to unpivot]'
##### CODE SAMPLE:
     import pandas as pd

     # create the dictionary to hold the data
     data = {'Character':['Mario', 'Luigi', 'Wario', 'Waluigi', 'Toad'], 'Strength':[70, 60, 40, 45, 15], 'Speed':[55, 70, 25, 60, 80], 'Health':
            [95, 80, 65, 70, 40]}

     # create the dataframe
     df = pd.DataFrame(data=data)

     # unpivot the columns
     pd.melt(df, id_vars=['Character'], var_name='Ability', value_name='Rating', value_vars=['Strength', 'Speed', 'Health'])
#### <i>Normalize JSON Files</i>
##### - JavaScript Object Notation (JSON) is a type of file that contains data in a "nested" format. This means that it acts similar to a File Explorer, where items are identified by a header (known as a "path") to keep things organized. Pandas allows users to convert JSON files to dataframes using the "json_normalize" function. To convert a JSON file to a dataframe, complete the following steps:
#### If you haven't installed Pandas yet:
        pip install pandas
#### If you have installed Pandas, copy and paste the code sample below into a Jupyter Notebook.
##### 1. Import the JSON file/data.
##### 2. Call the "json_normalize" method.
##### 3. Output the new dataframe.
##### SYNTAX: pd.json_normalize([file or variable name], record_path=['[name of path header, [name of nested path header]')
##### CODE SAMPLE:
       import pandas as pd

       # import the JSON file/data
       data = {
              "destination_addresses": [
                "Philadelphia, PA, USA"
              ],
              "origin_addresses": [
                "New York, NY, USA"
              ],
              "rows": [{
                "elements": [{
                  "distance": {
                    "text": "94.6 mi",
                    "value": 152193
                  },
                  "duration": {
                    "text": "1 hour 44 mins",
                    "value": 6227
                  },
                  "status": "OK"
                }]
              }],
              "status": "OK"
            }

      # convert the JSON data to dataframe
      df = pd.json_normalize(data, record_path=['rows', ['elements']])

      # output the new dataframe
      df
