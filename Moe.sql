--Calculate the unit price of the last ten orders

SELECT *
,CAST (amount_usd/quantity AS DECIMAL (12,2)) AS UNIT_PRICE
FROM tutorial.orders
WHERE amount_usd >0
ORDER BY UNIT_PRICE DESC
LIMIT 10


-- Return a table showing order ids where the order quantity is greater than 500. Include the order id, order quantity and account name and sort by order quantity in ascending order.

SELECT id, account_id, quantity, amount_usd
FROM tutorial.orders
--ORDER BY quantity ASC
WHERE quantity >= 500
ORDER BY quantity ASC


-- Use the accounts table to find the account name, primary_contact, and sales_rep_id for Apple, Oracle, and IBM

SELECT name, primary_contact, sales_rep_id, region_id
FROM tutorial.accounts
WHERE name IN ('Apple', 'Oracle', 'IBM')



--Return a table that provides the region for each sales_reps along with their associated accounts. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to the account name.
--- tutorial.sales_reps)

SELECT a.name AS account_name, CONCAT(s.first_name,' ', s.last_name) AS sales_rep_name, r.name AS region_name
FROM tutorial.accounts AS a
JOIN tutorial.sales_reps AS s
ON a.sales_rep_id = s.id
JOIN tutorial.regions AS r
ON s.region_id = r.id
ORDER BY a.name
LIMIT 100


-- How many sales reps are in each region?
SELECT COUNT(s.first_name), r.name as region_name
FROM tutorial.sales_reps AS s
JOIN tutorial.regions AS r
ON s.region_id = r.id
GROUP BY region_name


-- Provide a table that shows the total amount that has been spent by each company and the total quantity of orders, sort by total quantities in descending order.

SELECT a.name AS account_name, SUM(o.amount_usd) AS total_amount, SUM(o.quantity) AS total_quantity
FROM tutorial.orders AS o
JOIN tutorial.accounts AS a
ON a.id = o.account_id
GROUP BY a.name
ORDER BY SUM(o.quantity) DESC
LIMIT 100


--Use the accounts table to find all the companies whose names start with 'J'.
SELECT *
FROM tutorial.accounts
WHERE name LIKE 'J%'
LIMIT 100