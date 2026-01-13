from domain import Student

class StudentMemRepo:
    def __init__(self):
        self._data = {}

    def display_all_students(self):
        return list(self._data.values())

class StudentTextFIleRepo(StudentMemRepo):
    def __init__(self, filename="students.txt"):
        super().__init__()
        self._filename = filename
        self.__load_file()

    def add_student(self, id, name, attendance, grade):
        """
        Adds a student to the repository and saves the changes in the file
        :param id: student id
        :param name: student name
        :param attendance: student attendance
        :param grade: student grade
        """
        self._data[id] = Student(id, name, attendance, grade)
        self.__save_file()

    def __load_file(self):
        try:
            fin = open(self._filename, "r")
        except FileNotFoundError:
            return
        self._data = {}
        for line in fin:
            line_ok = line.strip().split(", ")
            if len(line_ok) < 4:
                continue
            id = line_ok[0]
            name = line_ok[1]
            attendance = line_ok[2]
            grade = line_ok[3]
            self._data[id] = Student(id, name, attendance, grade)

        fin.close()

    def __save_file(self):
        fout = open(self._filename, "w")
        for student in self._data.values():
            fout.write(f"{student.get_id}, {student.get_name}, {student.get_attendance}, {student.get_grade}\n")
        fout.close()