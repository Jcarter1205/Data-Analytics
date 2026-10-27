
USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT ProductID, ProductName, UnitPrice
FROM Products;


-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;


-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0
  AND UnitsOnOrder >= 1;


-- 4. Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry.

-- Products identifies each item's category using CategoryID.
SELECT ProductID, ProductName, CategoryID
FROM Products;

-- The Categories table contains the list of categories.
SELECT *
FROM Categories;

-- List all seafood products.
SELECT Products.ProductID, Products.ProductName
FROM Products
JOIN Categories
  ON Products.CategoryID = Categories.CategoryID
WHERE Categories.CategoryName = 'Seafood';


-- 5. Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.

-- Products identifies each supplier using SupplierID.
SELECT ProductID, ProductName, SupplierID
FROM Products;

-- Find the supplier identifier for Tokyo Traders.
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

-- Find all products supplied by Tokyo Traders.
SELECT Products.ProductID, Products.ProductName
FROM Products
WHERE Products.SupplierID = (
    SELECT SupplierID
    FROM Suppliers
    WHERE CompanyName = 'Tokyo Traders'
);


-- 6. How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question.

-- Count the employees.
SELECT COUNT(*) AS EmployeeCount
FROM Employees;

-- Find employees whose job title contains "manager".
SELECT EmployeeID, FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%manager%';


-- 7. Save your changes to 1B_query_practice.sql and use Git Bash to add, commit, and push to DataAnalytics/week-03.
