from repository import StudentTextFIleRepo
from services import StudentService

class UI:
    def __init__(self, student_service: StudentService):
        self._student_service = student_service
        self.running = True

    @staticmethod
    def run():
        try:
            student_repo = StudentTextFIleRepo()
            student_service = StudentService(student_repo)
            return UI(student_service)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def print_menu():
        print("Welcome to Exam Manager")
        print("   1. Add a Student")
        print("   2. Display all students")
        print("   3. Give a bonus")
        print("   4. Display students based on criteria")
        print("   x. Exit")

    def user_run(self):
        if self._student_service is None:
            print("Student Service not initialized")
            return

        while self.running:
            self.print_menu()
            option = input("Enter your choice: ")
            if option == "1":
                try:
                    self.add_student()
                except Exception as e:
                    print(e)
            elif option == "2":
                try:
                    self.display_all_students()
                except Exception as e:
                    print(e)
            elif option == "3":
                try:
                    self.give_bonus()
                except Exception as e:
                    print(e)
            elif option == "4":
                try:
                    self.display_criteria()
                except Exception as e:
                    print(e)
            elif option == "x":
                self.running = False
            else:
                print("Invalid option")

    def display_all_students(self):
        student_list = self._student_service.display_all_students_decreasing()
        for student in student_list:
            print(student)

    def add_student(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        attendance = input("Enter student attendance: ")
        grade = input("Enter student grade: ")
        self._student_service.add_student(id, name, attendance, grade)
        print("Student added successfully")

    def give_bonus(self):
        number_p = input("Enter a number of attendances: ")
        bonus = int(input("Enter bonus value: "))
        self._student_service.give_bonus(number_p, bonus)
        print("Bonus added successfully")

    def display_criteria(self):
        input_string = input("Enter string to find in name: ")
        students_criteria = self._student_service.search_criteria(input_string)
        for student in students_criteria:
            print(student)

if __name__ == "__main__":
    ui = UI.run()
    if ui is not None:
        ui.user_run()