-- SQL-команды для создания таблиц
CREATE TABLE customers (
  customer_id VARCHAR(50) NOT NULL,
  company_name VARCHAR(100) NOT NULL,
  contact_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  title VARCHAR(100),
  birth_date DATE,
  notes TEXT
);


CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL,
    employee_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(50) NOT NULL
);