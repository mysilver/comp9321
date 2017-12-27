from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer)

from lab_08_authentication.auth import login_required, SECRET_KEY


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


class GenerateToken(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        username = args.get("username")
        password = args.get("password")

        s = Serializer(SECRET_KEY, expires_in=600)
        token = s.dumps(username)

        if username == 'admin' and password == 'admin':
            return token.decode()

        abort(400)


class CourseHandler(Resource):
    @staticmethod
    @login_required
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('grade', type=int)
        args = parser.parse_args()

        name = args.get("name")
        grade = args.get("grade")

        database.append(Student(name, grade))
        return {'message': 'Added Successfully'}, 200, {}

    @staticmethod
    @marshal_with(fields=fields)
    @login_required
    def get():
        return statistics(), 200, {}


app = Flask(__name__)
api = Api(app)
database = []
api.add_resource(CourseHandler, '/statistics', endpoint="statistics", methods=['GET'])
api.add_resource(CourseHandler, '/student', endpoint="student", methods=['POST'])
api.add_resource(GenerateToken, '/auth', endpoint="auth", methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
