from flask import Flask
from flask import jsonify
from flask_restful import reqparse

app = Flask(__name__)
database = []


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Statistics:
    min = None
    max = None
    average = 0
    num_of_students = 0


def statistics():
    """
    This function gets through the all student objects in the database
    and calculates min, max, average, and total number of students.
    :return: Statistics
    """
    stats = Statistics()
    stats.num_of_students = len(database)

    if stats.num_of_students == 0:
        return stats

    stats.max = database[0].grade
    stats.min = database[0].grade
    sum = 0
    for student in database:
        sum += student.grade
        if student.grade < stats.min:
            stats.min = student.grade
        if student.grade > stats.max:
            stats.max = student.grade

    stats.average = sum / stats.num_of_students
    return stats


@app.route("/students", methods=['POST'])
def add_student():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('grade', type=int)
    args = parser.parse_args()

    name = args.get("name")
    grade = args.get("grade")

    database.append(Student(name, grade))
    return jsonify(studentName= name),200


@app.route("/students", methods=['GET'])
def get_students():
    response = jsonify([st.__dict__ for st in database])
    response.headers._list.append(('Access-Control-Allow-Origin', '*'))
    return response


@app.route("/students/<name>", methods=['GET'])
def get_student(name):
    for st in database:
        if st.name == name:
            return jsonify(st.__dict__)

    return jsonify(name=False), 404


@app.route("/students/<name>", methods=['DELETE'])
def delete_student(name):
    for st in database:
        if st.name == name:
            database.remove(st)
            return jsonify(studentName=name), 200
    return jsonify(studentName=False), 200


@app.route("/students/<name>", methods=['POST'])
def update_student(name):
    parser = reqparse.RequestParser()
    parser.add_argument('grade', type=int)
    args = parser.parse_args()
    grade = args.get("grade")

    for st in database:
        if st.name == name:
            database.remove(st)
            database.append(Student(name, grade))
            return jsonify(studentName=name, studentGrade=grade), 201

    return jsonify(studentName=False), 404


@app.route("/statistics", methods=['GET'])
def get_statistics():
    return jsonify(statistics().__dict__)


if __name__ == "__main__":
    app.run()
