from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Statistics:
    min = None
    max = None
    average = 0
    num_of_students = 0


fields = {
    "min": fields.Float,
    "max": fields.Float,
    "average": fields.Float,
    "num_of_students": fields.Integer
}


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


class Converter(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('grade', type=int)
        args = parser.parse_args()

        name = args.get("name")
        grade = args.get("grade")

        database.append(Student(name, grade))
        return {'message': 'Added Successfully'}, 200

    @marshal_with(fields=fields)
    def get(self):
        return statistics()


app = Flask(__name__)
api = Api(app)
database = []
api.add_resource(Converter, '/statistics', endpoint="statistics", methods=['GET'])
api.add_resource(Converter, '/student', endpoint="student", methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
