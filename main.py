# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = """SELECT firstName, lastName
       FROM employees
       WHERE officeCode IN (
           SELECT officeCode 
           FROM offices 
           WHERE city = 'Boston'
       );"""

df_boston = pd.read_sql(df_boston, conn)
print(df_boston)
# STEP 2
# Replace None with your code
df_zero_emp = """SELECT *
       FROM offices
       WHERE officeCode NOT IN (
           SELECT officeCode 
           FROM employees
       );"""

df_zero_emp = pd.read_sql(df_zero_emp, conn)
print(df_zero_emp)

# STEP 3
# Replace None with your code
df_employee =  """SELECT e.firstName, e.lastName, o.city, o.state
       FROM employees e
       LEFT JOIN offices o USING (officeCode)
       ORDER BY e.firstName, e.lastName;"""

df_employee = pd.read_sql(df_employee, conn)
print(df_employee)

# STEP 4
# Replace None with your code
df_contacts = """SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
       FROM customers
       WHERE customerNumber NOT IN (
           SELECT customerNumber 
           FROM orders
       )
       ORDER BY contactLastName;"""

df_contacts = pd.read_sql(df_contacts, conn)
print(df_contacts)

# STEP 5
# Replace None with your code
df_payment = """SELECT contactFirstName, contactLastName, amount, paymentDate
       FROM customers
       JOIN payments USING (customerNumber)
       ORDER BY CAST(amount AS FLOAT) DESC;"""

df_payment = pd.read_sql(df_payment, conn)
print(df_payment)

# STEP 6
# Replace None with your code
df_credit = """SELECT e.employeeNumber, e.firstName, e.lastName, 
              COUNT(c.customerNumber) AS numCustomers
       FROM employees e
       JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
       GROUP BY e.employeeNumber, e.firstName, e.lastName
       HAVING AVG(CAST(c.creditLimit AS FLOAT)) > 90000
       ORDER BY numCustomers DESC;"""

df_credit = pd.read_sql(df_credit, conn)
print(df_credit)

# STEP 7
# Replace None with your code
df_product_sold = """SELECT p.productName, 
              COUNT(od.orderNumber) AS numorders,
              SUM(od.quantityOrdered) AS totalunits
       FROM products p
       JOIN orderdetails od USING (productCode)
       GROUP BY p.productName
       ORDER BY totalunits DESC;"""

df_product_sold = pd.read_sql(df_product_sold, conn)
print(df_product_sold)

# STEP 8
# Replace None with your code
df_total_customers =  """SELECT p.productName, p.productCode,
              COUNT(DISTINCT o.customerNumber) AS numpurchasers
       FROM products p
       JOIN orderdetails od USING (productCode)
       JOIN orders o USING (orderNumber)
       GROUP BY p.productName, p.productCode
       ORDER BY numpurchasers DESC;"""

df_total_customers = pd.read_sql(df_total_customers, conn)
print(df_total_customers)

# STEP 9
# Replace None with your code
df_customers = """SELECT o.officeCode, o.city,
              COUNT(c.customerNumber) AS n_customers
       FROM offices o
       JOIN employees e USING (officeCode)
       JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
       GROUP BY o.officeCode, o.city;"""

df_customers = pd.read_sql(df_customers, conn)
print(df_customers)

# STEP 10
# Replace None with your code
df_under_20 = """SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, 
              o.city, o.officeCode
       FROM employees e
       JOIN offices o USING (officeCode)
       JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
       JOIN orders ord USING (customerNumber)
       JOIN orderdetails od USING (orderNumber)
       WHERE od.productCode IN (
           SELECT productCode
           FROM orderdetails
           JOIN orders USING (orderNumber)
           GROUP BY productCode
           HAVING COUNT(DISTINCT customerNumber) < 20
       )
       ORDER BY e.lastName;"""
df_under_20 = pd.read_sql(df_under_20, conn)
print(df_under_20)

conn.close()