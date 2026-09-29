from database import get_connection


def create_room():
    print("\n===== CREATE ROOM =====")

    room_number = input("Enter room number: ").strip()

    if not room_number:
        print("Room number cannot be empty.")
        return

    print("\nRoom Types:")
    print("1. Single")
    print("2. Double")
    print("3. Triple")

    choice = input("Select room type: ").strip()

    if choice == "1":
        room_type = "Single"
        capacity = 1

    elif choice == "2":
        room_type = "Double"
        capacity = 2

    elif choice == "3":
        room_type = "Triple"
        capacity = 3

    else:
        print("Invalid room type.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO rooms
            (room_number, room_type, capacity, occupied)
            VALUES (?, ?, ?, 0)
            """,
            (room_number, room_type, capacity)
        )

        conn.commit()

        print("\nRoom created successfully!")
        print("Room Number:", room_number)
        print("Room Type:", room_type)
        print("Capacity:", capacity)

    except Exception as error:
        print("\nCould not create room.")
        print("Error:", error)

    finally:
        conn.close()


def search_room():
    print("\n===== SEARCH ROOM =====")

    room_number = input("Enter room number: ").strip()

    if not room_number:
        print("Room number cannot be empty.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT room_id, room_number, room_type,
               capacity, occupied
        FROM rooms
        WHERE room_number = ?
        """,
        (room_number,)
    )

    room = cursor.fetchone()

    conn.close()

    if room:
        available = room[3] - room[4]

        print("\n----- ROOM DETAILS -----")
        print("Room ID       :", room[0])
        print("Room Number   :", room[1])
        print("Room Type     :", room[2])
        print("Capacity      :", room[3])
        print("Occupied Beds :", room[4])
        print("Available Beds:", available)

    else:
        print("\nRoom not found.")


def display_all_rooms():
    print("\n===== ALL ROOMS =====")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT room_id, room_number, room_type,
               capacity, occupied
        FROM rooms
        ORDER BY room_id
        """
    )

    rooms = cursor.fetchall()

    conn.close()

    if not rooms:
        print("No rooms available.")
        return

    print("\nID | Room | Type | Capacity | Occupied | Available")
    print("-" * 60)

    for room in rooms:
        available = room[3] - room[4]

        print(
            f"{room[0]} | "
            f"{room[1]} | "
            f"{room[2]} | "
            f"{room[3]} | "
            f"{room[4]} | "
            f"{available}"
        )


def allocate_bed():
    print("\n===== BED ALLOCATION =====")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    # Check student
    cursor.execute(
        """
        SELECT name, room_id, bed_number, status
        FROM students
        WHERE student_id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    if student[3] != "Active":
        print("Student is not active.")
        conn.close()
        return

    if student[1] is not None:
        print("Student already has a room.")
        print("Room ID:", student[1])
        print("Bed Number:", student[2])
        conn.close()
        return

    room_number = input("Enter room number: ").strip()

    if not room_number:
        print("Room number cannot be empty.")
        conn.close()
        return

    # Check room
    cursor.execute(
        """
        SELECT room_id, room_number, capacity, occupied
        FROM rooms
        WHERE room_number = ?
        """,
        (room_number,)
    )

    room = cursor.fetchone()

    if not room:
        print("Room not found.")
        conn.close()
        return

    room_id = room[0]
    capacity = room[2]
    occupied = room[3]

    # Check room capacity
    if occupied >= capacity:
        print("Room is full. No bed is available.")
        conn.close()
        return

    # Allocate next available bed
    bed_number = occupied + 1

    cursor.execute(
        """
        UPDATE students
        SET room_id = ?,
            bed_number = ?
        WHERE student_id = ?
        """,
        (room_id, bed_number, student_id)
    )

    cursor.execute(
        """
        UPDATE rooms
        SET occupied = occupied + 1
        WHERE room_id = ?
        """,
        (room_id,)
    )

    conn.commit()
    conn.close()

    print("\nBed allocated successfully!")
    print("Student ID :", student_id)
    print("Student    :", student[0])
    print("Room Number:", room_number)
    print("Bed Number :", bed_number)


def check_occupancy():
    print("\n===== ROOM OCCUPANCY =====")

    display_all_rooms()
