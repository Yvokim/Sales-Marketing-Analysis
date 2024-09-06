CREATE DATABASE shoppy_db;
USE shoppy_db;


CREATE TABLE products(
product_id INT PRIMARY KEY,
product_name VARCHAR(255),
category VARCHAR(255),
price DECIMAL(10,2)

);

CREATE TABLE customers(
	customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    location VARCHAR(255),
    region VARCHAR(255),
    age INT
);

CREATE TABLE sales(
	transaction_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    region VARCHAR(255),
    date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);













