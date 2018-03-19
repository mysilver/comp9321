class Teacher:
    def __init__(self, name, course, students={}):
        super().__init__()
        self.name = name
        self.course = course
        self.students = students


class Student:
    def __init__(self, id, first_name, last_name, gender='MALE'):
        super().__init__()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

