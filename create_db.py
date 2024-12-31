
import sqlite3

def create_and_populate_database():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            length REAL,
            weight REAL,
            velocity REAL,
            color TEXT
        )
    """)

    cursor.executemany("""
        INSERT INTO cars (length, weight, velocity, color)
        VALUES (?, ?, ?, ?)
    """, [
        (4.2, 1200, 120, 'red'),
        (4.3, 1400, 130, 'blue'),
        (4.4, 1600, 140, 'green'),
        (4.5, 1800, 150, 'black'),
        (4.6, 2000, 160, 'white'),
        (4.7, 2200, 170, 'yellow'),
    ])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_database()
    print("Database created successfully!")
