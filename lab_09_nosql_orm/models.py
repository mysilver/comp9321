from mongoengine import StringField, IntField, Document, EmbeddedDocument, ListField, EmbeddedDocumentField


class Student(EmbeddedDocument):
    id = IntField(required=True, primary_key=True)
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    gender = StringField(required=True, max_length=50)

    def __init__(self, id, first_name, last_name, gender='MALE', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


class Teacher(Document):
    id = IntField(required=True, primary_key=True)
    name = StringField(required=True, max_length=50)
    course = StringField(required=True, max_length=50)
    students = ListField(EmbeddedDocumentField(Student))

    def __init__(self, id, name, course, students=[], *args, **values):
        super().__init__(*args, **values)
        self.id = id
        self.name = name
        self.course = course
        self.students = students
