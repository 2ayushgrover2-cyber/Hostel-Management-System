from database import get_connection
from datetime import datetime


def generate_report():
    print("\n===== GENERATING HOSTEL REPORT =====")

    conn = get_connection()
    cursor = conn.cursor()

    # Total active students
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        WHERE status = 'Active'
        """
    )

    total_students = cursor.fetchone()[0]

    # Total staff
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM staff
        """
    )

    total_staff = cursor.fetchone()[0]

    # Total rooms
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM rooms
        """
    )

    total_rooms = cursor.fetchone()[0]

    # Total capacity
    cursor.execute(
        """
        SELECT COALESCE(SUM(capacity), 0)
        FROM rooms
        """
    )

    total_capacity = cursor.fetchone()[0]

    # Occupied beds
    cursor.execute(
        """
        SELECT COALESCE(SUM(occupied), 0)
        FROM rooms
        """
    )

    occupied_beds = cursor.fetchone()[0]

    # Total payments
    cursor.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM payments
        """
    )

    total_payments = cursor.fetchone()[0]

    # Student details
    cursor.execute(
        """
        SELECT student_id,
               name,
               age,
               gender,
               course,
               phone,
               room_id,
               bed_number,
               status
        FROM students
        ORDER BY student_id
        """
    )

    students = cursor.fetchall()

    conn.close()

    available_beds = total_capacity - occupied_beds

    report_file = "hostel_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("             HOSTEL MANAGEMENT REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(
            "Generated On: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n\n"
        )

        file.write("===== HOSTEL SUMMARY =====\n")
        file.write(f"Total Active Students : {total_students}\n")
        file.write(f"Total Staff           : {total_staff}\n")
        file.write(f"Total Rooms           : {total_rooms}\n")
        file.write(f"Total Bed Capacity    : {total_capacity}\n")
        file.write(f"Occupied Beds         : {occupied_beds}\n")
        file.write(f"Available Beds        : {available_beds}\n")
        file.write(f"Total Payments        : {total_payments}\n\n")

        file.write("=" * 60 + "\n")
        file.write("                 STUDENT DETAILS\n")
        file.write("=" * 60 + "\n\n")

        if students:

            for student in students:

                file.write(f"Student ID : {student[0]}\n")
                file.write(f"Name       : {student[1]}\n")
                file.write(f"Age        : {student[2]}\n")
                file.write(f"Gender     : {student[3]}\n")
                file.write(f"Course     : {student[4]}\n")
                file.write(f"Phone      : {student[5]}\n")
                file.write(f"Room ID    : {student[6]}\n")
                file.write(f"Bed Number : {student[7]}\n")
                file.write(f"Status     : {student[8]}\n")

                file.write("-" * 60 + "\n")

        else:
            file.write("No student records found.\n")

    print("\nReport generated successfully!")
    print("File name:", report_file)
