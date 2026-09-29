import sqlite3

DATABASE_NAME = "hostel_management.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            course TEXT NOT NULL,
            phone TEXT NOT NULL,
            room_id INTEGER,
            bed_number INTEGER,
            status TEXT DEFAULT 'Active'
        )
    """)

    # Staff table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    # Rooms table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT UNIQUE NOT NULL,
            room_type TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            occupied INTEGER DEFAULT 0
        )
    """)

    # Payments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TEXT NOT NULL,
            status TEXT DEFAULT 'Paid',
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """)

    conn.commit()
    conn.close()


def execute_query(query, parameters=()):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, parameters)
        conn.commit()

        last_id = cursor.lastrowid

        return last_id

    except sqlite3.Error as error:
        print("Database Error:", error)
        return None

    finally:
        conn.close()


def fetch_one(query, parameters=()):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, parameters)
        return cursor.fetchone()

    except sqlite3.Error as error:
        print("Database Error:", error)
        return None

    finally:
        conn.close()


def fetch_all(query, parameters=()):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, parameters)
        return cursor.fetchall()

    except sqlite3.Error as error:
        print("Database Error:", error)
        return []

    finally:
        conn.close()
