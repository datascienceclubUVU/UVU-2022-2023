# Intermediate SQL: Common Table Expressions (CTEs)
## Introduction
#### After reading the tutorial on subqueries, you may have thought to yourself, why on earth would I use these when they are impossible to comprehend? That's a great question. Luckily, the creators of SQL decided to create a much more comprehensive way of writing out multiple queries without using joins or unions: CTEs. **_Common Table Expressions (CTEs)_** are simply subqueries that are chained together though multiple uses of the WITH statement. This makes it significantly easier to read and comprehend long and complex subqueries.
## CTEs vs. Subqueries
#### Now that we have discussed why CTEs are superior to subqueries, let's take a visual example to more clearly illustrate the reason behind this:
    Example A (Subquery): SELECT customer_id, first_name, last_name, SUM(order_amt) sales_total
                          FROM customers
                          WHERE customer_id IN (SELECT DISTINCT customer_id FROM completed_sales)
                          GROUP BY customer_id, first_name, last_name
    Example A (CTE): WITH customer_sales AS (SELECT DISTINCT customer_id FROM completed_sales),
                      
                     all_customers AS (SELECT customer_id, first_name, last_name, SUM(order_amt) sales_total
                                       FROM customers
                                       GROUP BY customer_id, first_name, last_name)
                     SELECT * 
                     FROM all_customers
                     JOIN customer_sales ON all_customers.customer_id = customer_sales.customer_id
 #### As can be seen above, although the CTE is much longer, it is much easier to understand the query due to the use of aliases and joins rather than an unnamed subquery. However, there are times when subqueries may be necessary. For example, if you are trying to find customers with a particular characteristic (say their activity status), the characteristic will more than likely change over time. In these cases, it may be necessary to use a combination of both subqueries and CTES.
## CTE Best Practices
#### Just like anything in SQL, there is always a good, bad, and better way of doing things. In this context, take a look at the list below for some general rules of thumb to write effective CTEs:
    - ALWAYS write detailed aliases.
        - The reason for this is clarity. If you name all your CTEs names such as "x", "query", or "table1", 
          it will make it very difficult for your co-workers to decipher which CTE is which.
    - Be liberal with your comments.
        - Just because it's easy for you to understand the query, just remember than an outside user, such as a 
          member of your team who isn't familiar with SQL, may need to analyze the query to better analyze its results. 
          Comments enable outside users a greater ability to understand the steps and actions you took throughout the query.
    - ALWAYS be descriptive when renaming columns.
        - Similar to the first rule of thumb, when you are using aggregations or other functions within your CTEs, 
          the calculations invovled can become mixed up in the process. TO help with this, it never hurts to rename the 
          columns to something more desctiptive (rather than naming SUM(sales) "sales", name it something more descriptive such as "sales_per_customer")
## Conclusion
#### Although we didn't go into too much depth on the topic of the syntax of CTEs, it's more impotant to understand the use cases of them over subqueries. It's also very important to know when to use subqueries over CTEs or a combination of both. In any of these cases, deep business knowledge is necessary to understand the type of analysis you're trying to conduct and how to most effectively communicate how you got the result.
## Next Steps
#### To finish off the intermediate section of this learning series, let's take a look at how to make better use of the GROUP BY clause:
- [Group By Extensions](https://github.com/uvudataclub2022/UVU-2022-2023/blob/Data-Analytics/Relational%20Databases%20(SQL)/Tutorials/SQL/Group%20By%20Extensions.md)
