from database import create_tables

from student import (
    add_student,
    search_student,
    update_student,
    checkout_student
)

from staff import (
    add_staff,
    search_staff,
    display_all_staff
)

from room import (
    create_room,
    search_room,
    display_all_rooms,
    allocate_bed,
    check_occupancy
)

from payment import (
    add_payment,
    payment_history,
    check_fee_status
)

from dashboard import show_dashboard
from report import generate_report


def student_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("       STUDENT MANAGEMENT")
        print("=" * 40)

        print("1. Register Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Student Checkout")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            checkout_student()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def staff_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("        STAFF MANAGEMENT")
        print("=" * 40)

        print("1. Add Staff")
        print("2. Search Staff")
        print("3. Display All Staff")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_staff()

        elif choice == "2":
            search_staff()

        elif choice == "3":
            display_all_staff()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def room_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("         ROOM MANAGEMENT")
        print("=" * 40)

        print("1. Create Room")
        print("2. Search Room")
        print("3. Display All Rooms")
        print("4. Allocate Bed")
        print("5. Check Occupancy")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_room()

        elif choice == "2":
            search_room()

        elif choice == "3":
            display_all_rooms()

        elif choice == "4":
            allocate_bed()

        elif choice == "5":
            check_occupancy()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def payment_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("        PAYMENT MANAGEMENT")
        print("=" * 40)

        print("1. Add Payment")
        print("2. Payment History")
        print("3. Check Fee Status")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_payment()

        elif choice == "2":
            payment_history()

        elif choice == "3":
            check_fee_status()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def main():

    # Create database tables
    create_tables()

    print("\n")
    print("=" * 55)
    print("       WELCOME TO HOSTEL MANAGEMENT SYSTEM")
    print("=" * 55)

    while True:

        print("\n")
        print("--------------- MAIN MENU ---------------")

        print("1. Student Management")
        print("2. Staff Management")
        print("3. Room Management")
        print("4. Payment Management")
        print("5. Dashboard")
        print("6. Generate Hostel Report")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            staff_menu()

        elif choice == "3":
            room_menu()

        elif choice == "4":
            payment_menu()

        elif choice == "5":
            show_dashboard()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            print("\nThank you for using Hostel Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
