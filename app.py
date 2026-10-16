import sqlite3

API_KEY = "sk-live-12345-secret"

def get_user(name):
    conn = sqlite3.connect("db.sqlite")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()

def average(numbers):
    return sum(numbers) / len(numbers)

def delete_user(name):
    conn = sqlite3.connect("db.sqlite")
    conn.execute(f"DELETE FROM users WHERE name = '{name}'")

def read_file(path):
    f = open(path)
    return f.read()
# test update 3
# test update 4
