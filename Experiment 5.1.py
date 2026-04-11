import csv

def student_system():
    students = {}

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Export to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")

            students[roll] = {'Name': name, 'Marks': marks}
            print("Record saved!")

        elif choice == '2':
            roll = input("Enter Roll Number to search: ")

            if roll in students:
                print(f"Found: {students[roll]}")
            else:
                print("Student not found.")

        elif choice == '3':
            if not students:
                print("No records found.")
            else:
                for roll, info in students.items():
                    print(f"Roll: {roll} | Name: {info['Name']} | Marks: {info['Marks']}")

        elif choice == '4':
            with open('students.csv', 'w', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(['Roll No', 'Name', 'Marks'])

                for roll, info in students.items():
                    writer.writerow([roll, info['Name'], info['Marks']])

            print("Data exported to students.csv")

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

student_system()