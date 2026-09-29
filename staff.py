from database import get_connection


def add_staff():
    print("\n===== ADD STAFF =====")

    name = input("Enter staff name: ").strip()
    role = input("Enter staff role: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not role or not phone:
        print("All fields are required.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO staff (name, role, phone)
        VALUES (?, ?, ?)
    """, (name, role, phone))

    staff_id = cursor.lastrowid

    conn.commit()
    conn.close()

    print("\nStaff added successfully!")
    print("Staff ID:", staff_id)


def search_staff():
    print("\n===== SEARCH STAFF =====")

    try:
        staff_id = int(input("Enter staff ID: "))
    except ValueError:
        print("Invalid staff ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT staff_id, name, role, phone
        FROM staff
        WHERE staff_id = ?
    """, (staff_id,))

    staff = cursor.fetchone()

    conn.close()

    if staff:
        print("\n----- Staff Details -----")
        print("Staff ID :", staff[0])
        print("Name     :", staff[1])
        print("Role     :", staff[2])
        print("Phone    :", staff[3])
    else:
        print("Staff record not found.")


def display_all_staff():
    print("\n===== ALL STAFF =====")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT staff_id, name, role, phone
        FROM staff
    """)

    records = cursor.fetchall()

    conn.close()

    if not records:
        print("No staff records available.")
        return

    for record in records:
        print(
            f"ID: {record[0]} | "
            f"Name: {record[1]} | "
            f"Role: {record[2]} | "
            f"Phone: {record[3]}"
        )
