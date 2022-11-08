# TABLEAU 2022.1 BASICS
### Overview
#### - Tableau is a Business Intelligence tool used primarily for data visualization and reporting. In this tutorial, we will discuss the following topics:
            * Data Source Connections
            * Dimensions and Measures
            * Marks
            * Aggregate Functions
            * Filters
            * Legends
            * Tooltips
            * Tableau Shortcuts
### ~
### <i>Data Source Connections</i>
#### - Arguably the best feature of Tableau is the large array of data sources offered. The most used data sources for beginning users include the following:
            * Text Files
            * Microsoft Excel
            * Microsoft SQL Server
#### - To connect to these data sources, follow the instructions below:
    * How to Connect to Text Files:
        1. Open Tableau Desktop
        2. On the left pane of the "New Data Source" page, select "Text File" under the "To a File" header.
        3. In the "Select a File" dialog box, choose the file you want to use as your data source.
###
    * How to Connect to Microsoft Excel Files:
        1. Open Tableau Desktop
        2. On the left pane of the "New Data Source" page, select "Microsoft Excel" under the "To a File" header.
        3. In the "Select a File" dialog box, choose the Excel workbook you want to use as your data source.
### 
    * How to Connect to Microsoft SQL Server:
        1. Open Tableau Desktop
        2. On the left pane of the "New Data Source" page, select "Microsoft SQL Server" under the "To a Server" header.
        3. In the dialog box, enter the Server Name, Database Name, and select "Windows Authentication" 
           if you don't have a specified username and password.
        4. Click "Sign in".
### ~
### <i>Dimensions and Measures</i>
#### - Tableau is built on top of a query language known as Structured Query Language (SQL). Because of this, Tableau treats the data as tabular data (just like data  in Excel). Tabular data comes in the forms of categories and measurements. Tableau declares these data types as dimensions and measures.
#### - <i>DIMENSIONS</i> contain qualitative values (such as names, dates, or geographical data). You can use dimensions to categorize, segment, and reveal the details in your data. Dimensions affect the level of detail in the view.
#### - <i>MEASURES</i> contain numeric, quantitative values that you can measure. Measures can be aggregated. When you drag a measure into the view, Tableau applies an aggregation to that measure (by default).
### ~
### <i>Marks</i>
#### - Tableau offers a wide variety of data visualization features that allows the user to customize their charts. Some of these features include Colors, Size, Text Labels, Level of Detail, and Shapes.
![Tableau Marks Card](https://help.tableau.com/current/pro/desktop/en-us/Img/build_manual_shelves_marks1.png)
#### - The <i>COLORS</i> mark allows you to use a field to determine the colors used in the chart. Colors can enahance the usability of your visualization by distinguishing between different categories, and amounts (e.g., use the Sales field as the color mark to show how much money each Store made by displaying a darker color for more money, lighter color for less money.)
#### - The <i>SIZE</i> mark allows you to use a field to determine how large a particular object is in the chart. For example, if you had a bar chart comparing sales across five years, you could use the "Sales Amount" field to determine the size of the bars. The wider the bar, the more money made in the year.
#### - The <i>TEXT LABEL</i> mark allows you to create labels for each category or measure. For example, if you had a tree map comparing the Amount of Sales across State, you could use the "State Name" field as a text label to show which state has the most sales. These help the end user use the chart quickly rather than having to try to analyze the results for hours on end.
#### - The <i>DETAIL</i> mark allows you to add external fields to the visualization for use in calculations and tooltips. For example, if you were showing the top 5 cities by amount of sales, it might be useful to add the "State Name" field to the detail mark to show the State Name in the tooltip.
#### - The <i>SHAPES</i> mark is only used in specific chart types including scatter plots, box plots, and shape charts (bar charts that use shapes rather than bars). This mark is used for special cases but can be used to distinguish between categories or to create unique objects such as info buttons (the letter "i" inside a circle.)
### ~
### <i>AGGREGATE FUNCTIONS</i>
#### - As mentioned before, measures are used to create calculations between categories. To make the best use of this type of field, it is wise to choose the correct type of aggregation:
![Tableau Measures Aggregation](https://help.tableau.com/current/pro/desktop/en-us/Img/calc_agg2.png)
#### - The <i>SUM</i> aggregate simply adds up all the values in this field of the dataset (or the category depending on the level of detail). For example, SUM(Sales) will show you the total amount of the Sales field.
#### - The <i>AVERAGE</i> aggregate calculates the average of all the values in this field of the dataset (or the category depending on the level of detail). For example, AVERAGE(Sales) will show you the average amount of the Sales field.
#### - The <i>MEDIAN</i> aggregate sorts all the values in the field in ascending order (from smallest to largest) and outputs the middle value. This can be useful when there are outliers in your dataset (if most of the data in the Sales field is between 10,000 and 20,000 but you have a few values above 50,000, Median might be better to use than Average).
#### - The <i>COUNT</i> aggregate counts the number of values in the field (or the number of values in the category depending on the level of detail). For example, COUNT(Sales) will show you the number of values in the Sales field. This aggregate function can also be used with dimension fields. For example, COUNT(State Name) will show you the number of states in your dataset.
#### - The <i>COUNTD</i> aggregate counts the number of DISTINCT values in the field (or the number of distinct values in the category depending on the level of detail. For example, COUNTD(Artist Name) will show you the number of distinct artists in the Artist Name field. This function is very useful when you want to group values by category or are calculating the number of unique members within a given category or metric (such as ratings for a movie).
#### - The <i>MAXIMUM</i> aggregate outputs the largest value in the field (or the largest value in the category depending on the level of detail). For example, MAX(Sales) will show you the largest sales amount in the Sales field.
#### - The <i>MINIMUM</i> aggregate outputs the smallest value in the field (or the smallest value in the category depending on the level of detail). For example, MIN(Sales) will show you the smallest sales amount in the Sales field.
#### - There are a few other aggregates, but for the purpose of this tutorial we will skip them.
### ~
### <i>FILTERS</i>
#### - One of the most critical concepts of data visualization is user interaction and the most basic types of user interactions is the use of filters. Filters allow the end user to shrink the size of the dataset to adjust the level of detail, extract key insights by comparing different groups or categories, and view the difference between different metrics and input variables:
![Tableau Filters Card](https://help.tableau.com/current/pro/desktop/en-us/Img/filtering-drag1.png)
#### - Tableau allows you to specify default filters for the end user to interact with, as well as dynamic filters using parameters. Parameters is covered in the Intermediate tutorial, though it is good to know of their use. To create a simple filter, simply drag and drop the field you would like to use as the filter to the filters shelf (Above the Marks card).
