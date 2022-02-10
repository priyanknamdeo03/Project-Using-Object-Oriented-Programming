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
 

class Student():
    def __init__(self) -> None:
        self.student_data = []
        self.student_fields = ['roll', 'name', 'age', 'email', 'phone']
        self.student_database = 'students.csv'


    def display_menu(self) -> None:
        print("--------------------------------------")
        print(" Welcome to Student Management System")
        print("---------------------------------------")
        print("1. Add New Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Quit")
    
    
    def add_student(self) -> None:
        print("-------------------------")
        print("Add Student Information")
        print("-------------------------")
       
        for field in self.student_fields:
            value = input("Enter " + field + ": ")
            self.student_data.append(value)
    
        with open(self.student_database, "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([self.student_data])
    
        print("Data saved successfully")
        input("Press any key to continue")
        return
    
    
    def view_students(self) -> None:
        print("--- Student Records ---")
    
        with open(self.student_database, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for fields in self.student_fields:
                print(fields, end='\t |')
            print("\n-----------------------------------------------------------------")
    
            for row in reader:
                for item in row:
                    print(item, end="\t |")
                print("\n")
    
        input("Press any key to continue")
    
    
    def search_student(self) -> None:
        print("--- Search Student ---")
        roll = input("Enter roll no. to search: ")

        with open(self.student_database, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        print("----- Student Found -----")
                        print("Roll: ", row[0])
                        print("Name: ", row[1])
                        print("Age: ", row[2])
                        print("Email: ", row[3])
                        print("Phone: ", row[4])
                        break
            else:
                print("Roll No. not found in our database")
        input("Press any key to continue")
    
    
    def update_student(self) -> None:
        updated_data = []
        print("--- Update Student ---")
        roll = input("Enter roll no. to update: ")
        index_student = None
        
        with open(self.student_database, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            counter = 0

            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        index_student = counter
                        print("Student Found: at index ",index_student)
                        self.student_data = []
                        for field in self.student_fields:
                            value = input("Enter " + field + ": ")
                            self.student_data.append(value)
                        updated_data.append(self.student_data)
                    else:
                        updated_data.append(row)
                    counter += 1
 
 
        # Check if the record is found or not
        if index_student is not None:
            with open(self.student_database, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
        else:
            print("Roll No. not found in our database")
    
        input("Press any key to continue")
 

    def delete_student(self) -> None:    
        updated_data = []
        print("--- Delete Student ---")
        roll = input("Enter roll no. to delete: ")
        student_found = False

        with open(self.student_database, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            counter = 0

            for row in reader:
                if len(row) > 0:
                    if roll != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True
    
        if student_found is True:
            with open(self.student_database, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
            print("Roll no. ", roll, "deleted successfully")
        else:
            print("Roll No. not found in our database")
    
        input("Press any key to continue")

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


