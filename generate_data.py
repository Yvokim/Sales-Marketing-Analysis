# Generate product categories and names
import pandas
import pandas as pd
import random
import faker
from datetime import datetime, timedelta

categories = ['Electronics', 'Clothing', 'Home Goods', 'Books', 'Toys']
product_names = {

    'Electronics': ['SmartPhone', 'Laptop', 'Headphones', 'Smartwatch', 'Tablet'],
    'Clothing': ['T-shirt', 'Jeans', 'Jacket', 'Sneakers', 'Hat'],
    'Home Goods': ['Lamp', 'Sofa', 'Coffee Table', 'Curtains', 'Dishware'],
    'Books': ['Novel', 'Biography', 'Cookbook', 'Textbook', 'Comics'],
    'Toys': ['Action Figure', 'Puzzle', 'Board Game', 'Doll', 'Lego Set']

}
# Generate Products Data

products = []
product_id = 1

for category, names in product_names.items():
    for name in names:
        price = round(random.uniform(10, 500), 2)  # Random prices btn $10 and $500
        products.append([product_id, name, category, price])
        product_id += 1

# Convert to Data Frame
products_df = pd.DataFrame(products, columns=['product_id', 'product_name', 'category', 'price'])

# Display the products DataFrame
print(products_df)

# Generate Random customer data

fake = faker.Faker()  # Initialize Faker to generate random customer data

# Generate customer data

regions = ['North', 'South', 'East', 'West', 'Central']

customers = []
customer_id = 1

for _ in range(100):  # Generate 100 customers
    name = fake.name()
    location = fake.city()
    age = random.randint(18, 70)  # Random age btn 18 and 70
    region = random.choice(regions)  # Assign random region
    customers.append([customer_id, name, location, age, region])
    customer_id += 1

# Convert to a dataframe

customers_df = pandas.DataFrame(customers, columns=['customer_id', 'customer_name', 'location', 'age', 'region'])

# Display the customers
print(customers_df)

# GENERATE SALES DATA

sales = []
transaction_id = 1
start_date = datetime(2023, 1, 1)

for _ in range(500):  # Generate 500 customers
    customer_id = random.randint(1, 100)  # Random customer
    product_id = random.randint(1, len(products_df))  # Random product
    quantity = random.randint(1, 5)  # Qty btn 1 and 5
    date = start_date + timedelta(days=random.randint(0, 365))  # Random date
    sales.append([transaction_id, customer_id, product_id, quantity, date])
    transaction_id += 1

# Convert to  DataFrame
sales_df = pd.DataFrame(sales, columns=['transaction_id', 'customer_id', 'product_id', 'quantity', 'date'])

sales_df = sales_df.merge(customers_df[['customer_id', 'region']], on='customer_id', how='left')
# Display

print(sales_df)

# SAVE THE DATA TO CSV FILES

products_df.to_csv('products.csv', index=False)
customers_df.to_csv('customers.csv', index=False)
sales_df.to_csv('sales.csv', index=False)
