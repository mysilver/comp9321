from lab_07_orm.database import db_session, init_db
from lab_07_orm.models import Teacher, Student

init_db()

t1 = Teacher('Helen', 'Paik', {1: Student(1, "Ali", "Hasan")})
t2 = Teacher('John', 'Hard')

# add teachers to the database
db_session.add(t1)
db_session.add(t2)

# commit the changes
db_session.commit()

# query the database
for t in Teacher.query.all():
    print("Teacher:", t.name, " Number of Students:", len(t.students))
