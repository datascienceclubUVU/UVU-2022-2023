# SQL for Beginners
## <ins>Introduction</ins>
#### Interested in learning more about the world of databases? Look no further than SQL! This tutorial will be your guide to learn the basic SQL statements. Enjoy!


## <ins>Definitions</ins>
#### A <i>column</i>, also called an "attribute" or "field", describes an aspect of a data point. For example, height, weight, and age may all be columns.
#### A <i>row</i>, also called a record, is a collection of columns that represent a single data point. For example, one row may represent one hospital patient and may have attributes like age, weight, and height.
#### A <i>table</i> is a collection of rows and columns. This is the most basic unit found in a database and will be the foundation of this tutorial.
#### A <i>query</i> is a specific selection of columns from a table that can include filters to limit the rows retrieved. A google search is an example of a query.

## <ins>The 5 Basic SQL Statements</ins>
#### Since this is a tutorial for beginners, I’m going to show you how to write a query if you wanted to extract data from one table.
#### There are five components to a basic query:
   - _SELECT_ **(mandatory)**
   - _FROM_ **(mandatory)**
   - _WHERE_ (optional)
   - _GROUP BY_ (optional)
   - _ORDER BY_ (optional)
#### The structure is as follows:
`SELECT [column1], [column2]`<br>
`FROM [table_name]`

<br></br>
#### Let’s bring back my example as a reference:
#### _SELECT ID, Name, Age, Weight_lbs, Height_cm_
#### _FROM patient_info_
#### _WHERE Age > 20 AND Weight_lbs > 100_
#### _ORDER BY ID;_
<br></br>
#### **1. SELECT (Mandatory)**
#### - SELECT determines which columns you want to pull from a given table. For example, if I wanted to pull Name then my code would look like:
#### - A neat trick is if you want to pull all columns, you can use an asterisk — see below:
#### -         _SELECT *_
<br></br>
#### **2. FROM (Mandatory)**
#### - FROM determines which table you want to pull the information from. For example, if you wanted to pull the Name of the patient, you would want to pull the data FROM the table called patient_info (see above). The code would look something like this:
##### _SELECT_ _Name_
##### _FROM_ _patient_info_
#### - And there’s your first functional query! Let's go through the 3 additional optional steps.
<br></br>
#### **3. WHERE (optional)**
#### - What if you wanted to select the Names of patients who are older than 23? This is when WHERE comes in. WHERE is a statement used to filter your table, the same way you would use the filter tool in Excel!
#### - The code to get the Names of patients who are older than 23 is to the left. A visual representation is shown to the right:
IMAGE GOES HERE
#### - If you want the Names of patients that satisfy two clauses, you can use AND. Eg. Find the Names of patients who are older than 23 and weigh more than 130 lbs.
##### _SELECT Name_
##### _FROM patient_info_
##### _WHERE Age > 23 AND Weight_lbs > 130_
#### - If you want the Names of patients that satisfy one of two clauses, you can use OR. Eg. Find the Names of patients who are younger than 22 or older than 23.
##### _SELECT Name_
##### _FROM patient_info_
##### _WHERE Age < 22 OR Age > 23_
<br></br>
#### **4. GROUP BY (optional)**
#### - GROUP BY does what it says — it groups rows that have the same values into summary rows. It is typically used with aggregate functions like COUNT, MIN, MAX, SUM, AVG.
#### Let's use the example below:
IMAGE GOES HERE
#### If we wanted to get the number of hospital visits for each patient, we could use the code below and get the following result:
IMAGE GOES HERE
<br></br>
#### **5. ORDER BY (optional)**
#### - ORDER BY allows you to sort your results based on a particular attribute or a number of attributes in ascending or descending order. Let’s show an example.
##### _SELECT *_
##### _FROM patient_info_
##### _ORDER BY Age ASC_
#### - ‘ORDER BY Age asc’ means that your result set will order the rows by age in ascending order (see the left table in the image above). If you want to order it in descending order (right table in the image above), you would replace asc with desc.

###### *This article was taken from Medium.com. This work is not being used in any commercial or official publication.
