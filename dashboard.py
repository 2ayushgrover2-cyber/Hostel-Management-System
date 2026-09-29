from database import get_connection


def show_dashboard():
    print("\n")
    print("=" * 50)
    print("           HOSTEL DASHBOARD")
    print("=" * 50)

    conn = get_connection()
    cursor = conn.cursor()

    # Total students
    cursor.execute("""
        SELECT COUNT(*)
        FROM students
        WHERE status = 'Active'
    """)

    total_students = cursor.fetchone()[0]

    # Total staff
    cursor.execute("""
        SELECT COUNT(*)
        FROM staff
    """)

    total_staff = cursor.fetchone()[0]

    # Total rooms
    cursor.execute("""
        SELECT COUNT(*)
        FROM rooms
    """)

    total_rooms = cursor.fetchone()[0]

    # Total capacity
    cursor.execute("""
        SELECT COALESCE(SUM(capacity), 0)
        FROM rooms
    """)

    total_capacity = cursor.fetchone()[0]

    # Occupied beds
    cursor.execute("""
        SELECT COALESCE(SUM(occupied), 0)
        FROM rooms
    """)

    occupied_beds = cursor.fetchone()[0]

    # Available beds
    available_beds = total_capacity - occupied_beds

    # Total payments
    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM payments
    """)

    total_payments = cursor.fetchone()[0]

    conn.close()

    print("Total Active Students :", total_students)
    print("Total Staff           :", total_staff)
    print("Total Rooms           :", total_rooms)
    print("Total Bed Capacity    :", total_capacity)
    print("Occupied Beds         :", occupied_beds)
    print("Available Beds        :", available_beds)
    print("Total Payments        : ₹{:.2f}".format(total_payments))

    print("=" * 50)
