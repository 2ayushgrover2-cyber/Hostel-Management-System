from database import get_connection
from datetime import date


def add_payment():
    print("\n===== ADD PAYMENT =====")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    # Check if student exists
    cursor.execute(
        """
        SELECT student_id, name, status
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

    if student[2] != "Active":
        print("Student is not active.")
        conn.close()
        return

    try:
        amount = float(input("Enter payment amount: "))

        if amount <= 0:
            print("Payment amount must be greater than 0.")
            conn.close()
            return

    except ValueError:
        print("Please enter a valid amount.")
        conn.close()
        return

    payment_date = str(date.today())

    cursor.execute(
        """
        INSERT INTO payments
        (student_id, amount, payment_date, status)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, amount, payment_date, "Paid")
    )

    conn.commit()
    payment_id = cursor.lastrowid

    conn.close()

    print("\nPayment added successfully!")
    print("Payment ID :", payment_id)
    print("Student ID :", student_id)
    print("Student    :", student[1])
    print("Amount     :", amount)
    print("Date       :", payment_date)
    print("Status     : Paid")


def payment_history():
    print("\n===== PAYMENT HISTORY =====")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT payment_id,
               student_id,
               amount,
               payment_date,
               status
        FROM payments
        WHERE student_id = ?
        ORDER BY payment_id
        """,
        (student_id,)
    )

    payments = cursor.fetchall()

    conn.close()

    if not payments:
        print("\nNo payment records found.")
        return

    print("\nPayment ID | Student ID | Amount | Date | Status")
    print("-" * 60)

    for payment in payments:
        print(
            f"{payment[0]} | "
            f"{payment[1]} | "
            f"{payment[2]} | "
            f"{payment[3]} | "
            f"{payment[4]}"
        )


def check_fee_status():
    print("\n===== FEE STATUS =====")

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
        SELECT student_id, name, status
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

    # Calculate total payment
    cursor.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM payments
        WHERE student_id = ?
        """,
        (student_id,)
    )

    total_paid = cursor.fetchone()[0]

    conn.close()

    print("\n----- FEE STATUS -----")
    print("Student ID  :", student[0])
    print("Student Name:", student[1])
    print("Status      :", student[2])
    print("Total Paid  :", total_paid)

    if total_paid > 0:
        print("Fee Status  : Payment Recorded")
    else:
        print("Fee Status  : No Payment Recorded")
