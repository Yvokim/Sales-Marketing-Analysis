import pandas as pd
from sqlalchemy import create_engine

# pymysql :PyMySQL: This is a database driver or connector
# that allows SQLAlchemy (and other libraries)
# to communicate with MySQL databases.

# SQLAlchemy: This is the ORM (Object-Relational Mapping) framework that provides tools for working with databases in
# Python. It allows you to define database schema using Python classes and perform database operations through
# high-level abstractions.

#  MySQL's connection details

engine = create_engine('mysql+pymysql://malibubliss:malibubliss%40123@localhost/shoppy_db')

# load data from CSV files
products_df = pd.read_csv('products.csv')
customers_df = pd.read_csv('customers.csv')
sales_df = pd.read_csv('sales.csv')

# Insert data into tables
products_df.to_sql('products', con=engine, if_exists='replace', index=False)
customers_df.to_sql('customers', con=engine, if_exists='replace', index=False)
sales_df.to_sql('sales', con=engine, if_exists='replace', index=False)

print('Data has been inserted successfully.')
