``` 
select version();
```
| version |
|:--------|
| PostgreSQL 17.2 (Debian 17.2-1.pgdg120+1) on x86\_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit |
> ``` status
> SELECT 1
> ```

``` 
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    product VARCHAR(50) NOT NULL,
    amount INT NOT NULL
);

```
> ``` status
> CREATE TABLE
> ```

``` 
INSERT INTO Orders (order_id, customer_id, product, amount) VALUES
(1, 101, 'Laptop', 50000),
(2, 102, 'Mouse', 1000),
(3, 101, 'Keyboard', 2000),
(4, 103, 'Monitor', 15000),
(5, 102, 'Headphones', 3000),
(6, 101, 'Mouse', 1000),
(7, 103, 'Laptop', 50000),
(8, 104, 'Keyboard', 2000),
(9, 102, 'Monitor', 15000),
(10, 101, 'Headphones', 3000);

```
> ``` status
> INSERT 0 10
> ```

``` 
--Question 5: Find all orders for products whose names start with 'L' or 'M', but only if the order amount is above the overall average order amount.
select order_id,product from orders where  (product LIKE 'L%' or product LIKE 'M%') and amount >  (select avg(amount) from orders  )
```
| order\_id | product |
|---------:|:--------|
| 1 | Laptop |
| 4 | Monitor |
| 7 | Laptop |
| 9 | Monitor |
> ``` status
> SELECT 4
> ```

``` 
--Find all orders placed by customers who have never bought a 'Mouse'
select customer_id , product from orders where customer_id not in (select customer_id from orders where product = 'Mouse')
```
| customer\_id | product |
|------------:|:--------|
| 103 | Monitor |
| 103 | Laptop |
| 104 | Keyboard |
> ``` status
> SELECT 3
> ```

``` 
--Question 4: Find all individual orders that have an amount equal to the highest (maximum) single order amount in the entire table.
select order_id from orders where amount = (select max(amount) from orders); 
```
| order\_id |
|---------:|
| 1 |
| 7 |
> ``` status
> SELECT 2
> ```

``` 
-- Find all individual orders where the amount is strictly greater than the average amount of all orders in the entire table
select customer_id,order_id ,amount from orders where amount > (select avg(amount ) from Orders ); 
```
| customer\_id | order\_id | amount |
|------------:|---------:|-------:|
| 101 | 1 | 50000 |
| 103 | 4 | 15000 |
| 103 | 7 | 50000 |
| 102 | 9 | 15000 |
> ``` status
> SELECT 4
> ```

``` 
--Question 2: Find all orders for products that have ever been purchased by customer_id = 104. (Use a subquery with IN)
select customer_id , product from orders where product in (select product from Orders where customer_id = '104');
```
| customer\_id | product |
|------------:|:--------|
| 101 | Keyboard |
| 104 | Keyboard |
> ``` status
> SELECT 2
> ```

``` 
-- Find the total amount spent by each customer_id.
select customer_id, SUM(amount) from Orders group by customer_id ; 
```
| customer\_id | sum |
|------------:|----:|
| 101 | 56000 |
| 103 | 65000 |
| 104 | 2000 |
| 102 | 19000 |
> ``` status
> SELECT 4
> ```

``` 
-- Find the number of orders placed by each customer_id
select customer_id,count(order_id) 
  from Orders group by customer_id ; 
```
| customer\_id | count |
|------------:|------:|
| 101 | 4 |
| 103 | 2 |
| 104 | 1 |
| 102 | 3 |
> ``` status
> SELECT 4
> ```

``` 
--Find the average amount spent on each type of product
select product,AVG(amount) from Orders group by product; 
```
| product | avg |
|:--------|----:|
| Mouse | 1000.0000000000000000 |
| Keyboard | 2000.0000000000000000 |
| Monitor | 15000.000000000000 |
| Laptop | 50000.000000000000 |
| Headphones | 3000.0000000000000000 |
> ``` status
> SELECT 5
> ```

``` 
--Find the highest (maximum) amount spent by each customer_i
select customer_id, max(amount) from Orders group by customer_id ;
```
| customer\_id | max |
|------------:|----:|
| 101 | 50000 |
| 103 | 50000 |
| 104 | 2000 |
| 102 | 15000 |
> ``` status
> SELECT 4
> ```

``` 
--Find the customer_id values who have spent a total sum of more than 5,000, using a HAVING clause
select customer_id,sum(amount) from Orders group by customer_id having sum(amount) >50000
```
| customer\_id | sum |
|------------:|----:|
| 101 | 56000 |
| 103 | 65000 |
> ``` status
> SELECT 2
> ```

``` 
--Find the total amount spent by each customer_id, and sort the results from highest total spend to lowest.
select customer_id, SUM(amount)
from Orders 
group by customer_id
order by sum(amount) DESC;
```
| customer\_id | sum |
|------------:|----:|
| 103 | 65000 |
| 101 | 56000 |
| 102 | 19000 |
| 104 | 2000 |
> ``` status
> SELECT 4
> ```

``` 
--: Find the total number of orders for each product, but exclude the product 'Laptop' from the results completely.
select product,count(*) from orders where product != 'Laptop' group by product ;

```
| product | count |
|:--------|------:|
| Mouse | 2 |
| Keyboard | 2 |
| Monitor | 2 |
| Headphones | 2 |
> ``` status
> SELECT 4
> ```

``` 
--Find the average amount spent by each customer_id, but only show customers who have an average spend greater than 2,000
select customer_id, avg(amount) from Orders group by customer_id having avg(amount) > 2000 ; 
```
| customer\_id | avg |
|------------:|----:|
| 101 | 14000.000000000000 |
| 103 | 32500.000000000000 |
| 102 | 6333.3333333333333333 |
> ``` status
> SELECT 3
> ```

``` 
--Find the total amount spent on each product, but only include individual orders where the amount is greater than or equal to 2,000.
select product,sum(amount) from Orders where amount >  2000 group by product ; 
```
| product | sum |
|:--------|----:|
| Monitor | 30000 |
| Laptop | 100000 |
| Headphones | 6000 |
> ``` status
> SELECT 3
> ```

``` 
--For every customer_id, find the highest (maximum) single order amount. Exclude 'Mouse' from the products, and sort the final output by customer_id in descending order.
select customer_id,max(amount) from Orders where product != 'Mouse' group by customer_id order by customer_id desc; 
```
| customer\_id | max |
|------------:|----:|
| 104 | 2000 |
| 103 | 50000 |
| 102 | 15000 |
| 101 | 50000 |
> ``` status
> SELECT 4
> ```

[fiddle](https://dbfiddle.uk/PyOLuqs1)
