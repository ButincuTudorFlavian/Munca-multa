class Student:
    def __init__(self, id, name, attendance, grade):
        self._id = id
        self._name = name
        self._attendance = attendance
        self._grade = grade

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    @property
    def get_attendance(self):
        return self._attendance

    @property
    def get_grade(self)->int:
        return self._grade

    @get_grade.setter
    def set_grade(self, value):
        self._grade = value

    def __str__(self):
        return f"{self.get_id}, {self.get_name}, {self.get_attendance}, {self.get_grade}"
