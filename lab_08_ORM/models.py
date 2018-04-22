from sqlalchemy import Column, Integer, String
from sqlalchemy import PickleType

from lab_08_ORM.database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    course = Column(String)
    students = Column(PickleType)

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
