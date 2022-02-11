# Student Management System
"""
Fields :- ['roll', 'name', 'age', 'email', 'phone']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
"""
 
import csv
import json

class Student():
    def __init__(self) -> None:
        self.student_data = []
        self.student_fields = ['roll', 'name', 'age', 'email', 'phone']

    # ------------------------------------------------------------------

    def display_menu(self) -> None:
        print("\n--------------------------------------")
        print(" Welcome to Student Management System")
        print("---------------------------------------")
        print("1. Add New Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Quit")
    
    # ------------------------------------------------------------------
    
    def add_student(self) -> None:
        print("-------------------------")
        print("Add Student Information")
        print("-------------------------")
        data = {}

        for field in self.student_fields:
            value = input("Enter " + field + ": ")
            data[field] = value
        self.student_data.append(data)

        with open(f'students.json', "w", encoding="utf-8") as file:
            json.dump(self.student_data, file, indent=4)

        print("Data saved successfully")
        input("Press any key to continue ")
        return
    
    # ------------------------------------------------------------------
    
    def view_students(self) -> None:
        print("\n--- Student Records ---")

        with open(f'students.json', "r", encoding="utf-8") as file:
            data = json.load(file)

            for add_details in data:
                print("Roll No : ", add_details['roll'])
                print("Name : ", add_details['name'])
                print("Age : ", add_details['age'])
                print("Phone : ", add_details['phone'])
                print("-------------------------------\n")
    
        input("Press any key to continue ")
    
    # ------------------------------------------------------------------
    
    def search_student(self) -> None:
        print("\n--- Search Student ---")
        roll = input("Enter roll no. to search: ")

        with open(f'students.json', "r", encoding="utf-8") as file:
            data = json.load(file)

            for show_details in data:
                if show_details['roll'] == roll:
                    print("\n--- Student Records ---")
                    print("\nRoll No : ", show_details['roll'])
                    print("Name : ", show_details['name'])
                    print("Age : ", show_details['age'])
                    print("Phone : ", show_details['phone'])
                    print("-------------------------------\n")
                    break
            else:
                print("\nRoll No. not found in our database...........\n")

        input("Press any key to continue ")
    
    # ------------------------------------------------------------------
    
    def update_student(self) -> None:
        print("\n--- Update Student ---")
        roll = input("Enter roll no. to update: ")
        file_updated = False

        with open(f'students.json', "r+", encoding="utf-8") as file:
            data = json.load(file)

            for row_detail in data:
                if row_detail['roll'] == roll:
                    
                    for field in self.student_fields:
                        value = input("Enter " + field + ": ")
                        row_detail[field] = value
                    print("\nUpdate Successful.................\n")
                    # global file_updated
                    file_updated = True
                    break
            else:
                print("\nRoll No. not found in our database...........\n")
        
        if file_updated:
            with open(f'students.json', "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
    
        input("Press any key to continue ")
    
    # ------------------------------------------------------------------

    def delete_student(self) -> None:    
        print("\n--- Delete Student ---")
        roll = input("Enter roll no. to delete: ")
        file_deleted = False

        with open(f'students.json', "r+", encoding="utf-8") as file:
            data = json.load(file)
            
            for row_detail in range(len(data)):
                if data[row_detail]['roll'] == roll:
                    del data[row_detail]
                    print("\Record Deletion Successful.............\n")
                    file_deleted = True
                    break
            else:
                print("\nRoll No. not found in our database...........\n")
        
        with open(f'students.json', "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
        input("Press any key to continue ")

# ----------------------------------------------------------------------


def main() -> None:
    student = Student()

    while True:
        student.display_menu()
    
        choice = input("Enter your choice: ")
        if choice == '1':
            student.add_student()
        elif choice == '2':
            student.view_students()
        elif choice == '3':
            student.search_student()
        elif choice == '4':
            student.update_student()
        elif choice == '5':
            student.delete_student()
        else:
            break
    
    print("-------------------------------")
    print(" Thank you for using our system")
    print("-------------------------------")

# ----------------------------------------------------------------------


if __name__ == '__main__':
    main()


