# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# # STEP 1
# # Replace None with your code
# df_boston = """SELECT firstName, lastName, jobTitle
#        FROM employees
#        WHERE officeCode IN (
#            SELECT officeCode 
#            FROM offices 
#            WHERE city = 'Boston'
#        );"""

# result = pd.read_sql(df_boston, conn)
# print(result)
# # STEP 2
# # Replace None with your code
# df_zero_emp = """SELECT *
#        FROM offices
#        WHERE officeCode NOT IN (
#            SELECT officeCode 
#            FROM employees
#        );"""

# result2 = pd.read_sql(df_zero_emp, conn)
# print(result2)

# # STEP 3
# # Replace None with your code
# df_employee =  """SELECT e.firstName, e.lastName, o.city, o.state
#        FROM employees e
#        LEFT JOIN offices o USING (officeCode)
#        ORDER BY e.firstName, e.lastName;"""

# result3 = pd.read_sql(df_employee, conn)
# print(result3)

# STEP 4
# Replace None with your code
# df_contacts = """SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
#        FROM customers
#        WHERE customerNumber NOT IN (
#            SELECT customerNumber 
#            FROM orders
#        )
#        ORDER BY contactLastName;"""

# result4 = pd.read_sql(df_contacts, conn)
# print(result4)

# STEP 5
# Replace None with your code
# df_payment = """SELECT contactFirstName, contactLastName, amount, paymentDate
#        FROM customers
#        JOIN payments USING (customerNumber)
#        ORDER BY CAST(amount AS FLOAT) DESC;"""

# result5 = pd.read_sql(df_payment, conn)
# print(result5)

# STEP 6
# Replace None with your code
# df_credit = """SELECT e.employeeNumber, e.firstName, e.lastName, 
#               COUNT(c.customerNumber) AS numCustomers
#        FROM employees e
#        JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
#        GROUP BY e.employeeNumber, e.firstName, e.lastName
#        HAVING AVG(CAST(c.creditLimit AS FLOAT)) > 90000
#        ORDER BY numCustomers DESC;"""

# result6 = pd.read_sql(df_credit, conn)
# print(result6)

# STEP 7
# Replace None with your code
# df_product_sold = """SELECT p.productName, 
#               COUNT(od.orderNumber) AS numorders,
#               SUM(od.quantityOrdered) AS totalunits
#        FROM products p
#        JOIN orderdetails od USING (productCode)
#        GROUP BY p.productName
#        ORDER BY totalunits DESC;"""

# result7 = pd.read_sql(df_product_sold, conn)
# print(result7)

# STEP 8
# Replace None with your code
# df_total_customers =  """SELECT p.productName, p.productCode,
#               COUNT(DISTINCT o.customerNumber) AS numpurchasers
#        FROM products p
#        JOIN orderdetails od USING (productCode)
#        JOIN orders o USING (orderNumber)
#        GROUP BY p.productName, p.productCode
#        ORDER BY numpurchasers DESC;"""

# result8 = pd.read_sql(df_total_customers, conn)
# print(result8)

# STEP 9
# # Replace None with your code
# df_customers = """SELECT o.officeCode, o.city,
#               COUNT(c.customerNumber) AS n_customers
#        FROM offices o
#        JOIN employees e USING (officeCode)
#        JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
#        GROUP BY o.officeCode, o.city;"""

# result9 = pd.read_sql(df_customers, conn)
# print(result9)

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
       );"""

result10 = pd.read_sql(df_under_20, conn)
print(result10)
conn.close()