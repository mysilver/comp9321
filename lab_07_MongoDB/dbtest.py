from mongoengine import connect

from lab_07_MongoDB.models import Teacher, Student

from mongoengine import connect
from lab_07_MongoDB.models import Teacher, Student


def save_information():
    t1 = Teacher(1, 'Helen', 'Paik', [Student(1, "Tom", " Ainsley")])
    t2 = Teacher(2, 'John', 'Hardy')
    connect('teacher')  # add teachers to the database
    t1.save()
    t2.save()


def get_all_teachers():
    connect('teacher')
    for t in Teacher.objects:
        print(t.id, t.name)


def get_one_teacher():
    connect('teacher')
    for t in Teacher.objects(id=1):
        print(t.id, t.name)


def update_teacher_info():
    connect('teacher')
    Teacher.objects(id=2).update(name='George')


def delete_teacher_info():
    connect('teacher')
    Teacher.objects(id=2).Delete()


if __name__ == '__main__':
    save_information()
    get_all_teachers()
    delete_teacher_info()


