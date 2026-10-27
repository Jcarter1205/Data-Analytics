-- 4a. The products table holds the items Northwind sells.
-- 4b. The categories table holds the types of items Northwind sells.
-- 5. Retrieve all columns from the employees table.
SELECT *
FROM northwind.employees;
-- 5a. The Northwind employee whose name makes it look like she is a bird is Margaret Peacock.
-- 6. Retrieve all columns from the products table.
SELECT *
FROM northwind.products;
-- 6a. The products query returns 77 records in the standard Northwind database.
-- To retrieve only 10 rows, I can change the query row limit using the toolbar.
-- 6b. The LIMIT 10 clause restricts the query to 10 rows.
-- Source: MySQL 8.0 Reference Manual, SELECT Statement:
-- https://dev.mysql.com/doc/refman/8.0/en/select.html
-- 7. Retrieve all columns from the categories table.
SELECT *
FROM northwind.categories;
-- 7c. The CategoryID for Seafood is 8 in the standard Northwind database.
-- 8. Retrieve the first 50 orders with the required columns.
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM northwind.orders
LIMIT 50;