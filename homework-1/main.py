"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

#подключене к БД

conn  = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="453453"
)
cursor = conn.cursor()


#Заполнение таблицы

with open('north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO customers (customer_id, company_name, contact_name) "
            "VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

# Заполнение таблицы employees
with open('north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO employees (first_name, last_name, title, birth_date, notes) "
            "VALUES (%s, %s, %s, %s, %s)",
            (row[1], row[2], row[3], row[4], row[5])
        )


# Заполнение таблицы orders

# открываем файл и читаем данные
with open('north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропуск заголовка
    for row in reader:
        cursor.execute(
            "INSERT INTO orders (order_id, customer_id,employee_id,order_date,ship_city) "
            "VALUES (%s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4]) # исправляем индексы столбцов и пропускаем order_id
        )


# Сохранение изменений и закрытие соединения
conn.commit()
cursor.close()
conn.close()