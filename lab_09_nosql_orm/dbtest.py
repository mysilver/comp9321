from mongoengine import connect

from lab_09_nosql_orm.models import Teacher, Student

t1 = Teacher(1, 'Helen', 'Paik', [Student(1, "Ali", "Hasan")])
t2 = Teacher(2, 'John', 'Hard')

connect('teacher')
# add teachers to the database
t1.save()
t2.save()

# Print the number of teachers in the collection
print('Collection Size:', Teacher.objects.count())
# Prints out the names of all the teachers in the database
for t in Teacher.objects:
    print(t.id, t.name)

print("Filter the collection")
# Filter The collection
for t in Teacher.objects(id=1):
    print(t.id, t.name)
