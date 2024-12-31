
from fastapi import FastAPI, Depends
from fastapi.responses import Response
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("cars.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/search_cars")
def search_cars(length: float = None, weight: float = None, velocity: float = None, color: str = None):
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    if length:
        query += " AND length = ?"
        params.append(length)
    if weight:
        query += " AND weight = ?"
        params.append(weight)
    if velocity:
        query += " AND velocity = ?"
        params.append(velocity)
    if color:
        query += " AND color = ?"
        params.append(color)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return {"cars": [dict(row) for row in results]}

@app.get("/all_cars")
def all_cars():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars")
    results = cursor.fetchall()
    conn.close()
    return {"cars": [dict(row) for row in results]}
