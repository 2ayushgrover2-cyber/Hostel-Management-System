from database import get_connection


def add_student():
    print("\n===== STUDENT REGISTRATION =====")

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    gender = input("Enter gender: ").strip()
    course = input("Enter course: ").strip()
    phone = input("Enter phone number: ").strip()

    if not gender or not course or not phone:
        print("All fields are required.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, age, gender, course, phone)
        VALUES (?, ?, ?, ?, ?)
    """, (name, age, gender, course, phone))

    student_id = cursor.lastrowid

    conn.commit()
    conn.close()

    print("\nStudent registered successfully!")
    print("Student ID:", student_id)


def search_student():
    print("\n===== SEARCH STUDENT =====")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, age, gender, course,
               phone, room_id, bed_number, status
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    if student:
        print("\n----- Student Details -----")
        print("Student ID :", student[0])
        print("Name       :", student[1])
        print("Age        :", student[2])
        print("Gender     :", student[3])
        print("Course     :", student[4])
        print("Phone      :", student[5])
        print("Room ID    :", student[6])
        print("Bed Number :", student[7])
        print("Status     :", student[8])
    else:
        print("Student not found.")


def update_student():
    print("\n===== UPDATE STUDENT =====")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    print("\nLeave a field blank to keep the existing value.")

    name = input("Enter new name: ").strip()
    phone = input("Enter new phone: ").strip()
    course = input("Enter new course: ").strip()

    if name:
        cursor.execute(
            "UPDATE students SET name = ? WHERE student_id = ?",
            (name, student_id)
        )

    if phone:
        cursor.execute(
            "UPDATE students SET phone = ? WHERE student_id = ?",
            (phone, student_id)
        )

    if course:
        cursor.execute(
            "UPDATE students SET course = ? WHERE student_id = ?",
            (course, student_id)
        )

    conn.commit()
    conn.close()

    print("Student record updated successfully.")


def checkout_student():
    print("\n===== STUDENT CHECKOUT =====")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid student ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT room_id, bed_number, status
        FROM students
        WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    if student[2] != "Active":
        print("Student is already checked out.")
        conn.close()
        return

    room_id = student[0]

    cursor.execute("""
        UPDATE students
        SET status = 'Checked Out',
            room_id = NULL,
            bed_number = NULL
        WHERE student_id = ?
    """, (student_id,))

    if room_id:
        cursor.execute("""
            UPDATE rooms
            SET occupied = CASE
                WHEN occupied > 0 THEN occupied - 1
                ELSE 0
            END
            WHERE room_id = ?
        """, (room_id,))

    conn.commit()
    conn.close()

    print("Student checked out successfully.")
