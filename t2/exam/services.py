from repository import StudentTextFIleRepo

class StudentError(Exception):
    pass

class StudentService:
    def __init__(self, student_repo: StudentTextFIleRepo):
        self._student_repo = student_repo

    def display_all_students_decreasing(self):
        student_list = self._student_repo.display_all_students()
        sort_students = sorted(student_list, key=lambda student: (- int(student.get_grade), student.get_name))
        return sort_students

    def valid_student(self, id, name, attendance, grade):
        """
        Checks if the student id is unique, it has a valid name, the attendance, and the grade
        are positive integers and returns True or false
        :param id: student id
        :param name: student name
        :param attendance: student attendance
        :param grade: student grade
        :return: True or False
        """
        for student in self._student_repo.display_all_students():
            if student.get_id == id:
                return False

        if " " not in name:
            return False

        name_1, name_2 = name.split(" ")
        if len(name_1) < 3 or len(name_2) < 3:
            return False

        if int(attendance) < 0:
            return False

        if int(grade) < 0 or int(grade) > 10:
            return False

        return True

    def add_student(self, id, name, attendance, grade):
        """
        Adds a student to the repository and saves the changes in the file
        or raises an error if the student's data is invalid
        :param id: student id
        :param name: student name
        :param attendance: student attendance
        :param grade: student grade
        """
        if self.valid_student(id, name, attendance, grade):
            self._student_repo.add_student(id, name, attendance, grade)
        else:
            raise StudentError("Invalid student data")

    def give_bonus(self, number_p, bonus):
        for student in self._student_repo.display_all_students():
            if int(student.get_attendance) >= int(number_p) and int(student.get_grade) + int(bonus) <= 10:
                student.set_grade = int(student.get_grade) + int(bonus)

    def search_criteria(self, input_string):
        search_students = []
        for student in self._student_repo.display_all_students():
            if input_string in student.get_name:
                search_students.append(student)

        sort_students = sorted(search_students, key=lambda student: student.get_name)
        return sort_students