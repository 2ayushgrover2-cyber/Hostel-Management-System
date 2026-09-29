# Hostel Management System

A simple Python and SQLite based command-line Hostel Management System suitable for a BTech first-year project.

## Features

- Student registration
- Automatic student ID generation
- Student search and update
- Student checkout
- Room creation
- Single, Double and Triple rooms
- Automatic bed allocation
- Room occupancy checking
- Staff management
- Payment recording
- Payment history
- Hostel dashboard
- Text report generation

## Technologies

- Python 3
- SQLite
- SQL
- Python `sqlite3`
- Python `datetime`

No external Python packages are required.

## Project Structure

```text
Hostel-Management-System/
│
├── main.py
├── database.py
├── student.py
├── room.py
├── staff.py
├── payment.py
├── dashboard.py
├── report.py
├── README.md
├── .gitignore
│
├── hostel_management.db     # created automatically after running
└── hostel_report.txt        # created when a report is generated
```

## How to Run in PyCharm

1. Open PyCharm.
2. Select **Open** and choose this project folder.
3. Make sure Python 3 is configured as the project interpreter.
4. Open `main.py`.
5. Right-click inside `main.py`.
6. Select **Run 'main'**.
7. The database is created automatically.

No `pip install` command is required.

## How to Upload to GitHub

Create a new GitHub repository, for example:

`Hostel-Management-System`

Then upload the project files.

Recommended files to upload:

- `main.py`
- `database.py`
- `student.py`
- `room.py`
- `staff.py`
- `payment.py`
- `dashboard.py`
- `report.py`
- `README.md`
- `.gitignore`

The SQLite database and generated report are ignored because they are created automatically by the application.

## Testing

Test the following:

1. Register a student.
2. Create a room.
3. Allocate a bed to the student.
4. Search the student.
5. Add a payment.
6. View payment history.
7. Add a staff member.
8. Open the dashboard.
9. Generate the hostel report.
10. Test invalid inputs.

## Project Objective

The objective is to demonstrate Python programming, modular programming, SQLite database management, SQL queries, input validation, exception handling and file handling through a practical hostel management application.

## Future Enhancements

- GUI using Tkinter
- Web interface
- Login/authentication
- Attendance management
- Visitor management
- Email/SMS notifications
- Cloud database
- Advanced charts and analytics
