import datetime

from flask import Blueprint
from flask import request, render_template, redirect, url_for, make_response, session, Flask

from lab_02_Blueprints.app.models import Teacher, Student
from lab_02_Blueprints.utils.serialize import deserialize, serialize

bp = Blueprint('app', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def index():
    teacher = retrieve_teacher()
    if teacher is None:
        return redirect(url_for(".register"))

    return redirect(url_for(".show_students"))


@bp.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        return render_template("app/register.html")
    else:
        name = request.form.get("name")
        course = request.form.get("course")
        teacher = Teacher(name, course)

        session["_teacher"] = serialize(teacher)
        return redirect(url_for(".index"))


@bp.route('/students', methods=["GET"])
def show_students():
    teacher = retrieve_teacher()
    if teacher is None:
        return redirect("register")
    else:
        return render_template("app/students.html", students=teacher.students.values())


@bp.route('/add', methods=["POST", "GET"])
def add():
    if request.method == 'GET':
        return render_template("app/add.html")
    else:
        id = request.form.get("id")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        gender = request.form.get("gender")

        teacher = retrieve_teacher()
        teacher.students[id] = Student(id, firstname, lastname, gender)
        session['_teacher'] = serialize(teacher)

        return redirect(url_for(".show_students"))


@bp.route('/delete/<id>', methods=["GET", "POST", "DELETE"])
def delete(id):
    teacher = retrieve_teacher()
    teacher.students.pop(id)
    session['_teacher'] = serialize(teacher)

    return redirect(url_for(".show_students"))


@bp.route('/edit/<id>', methods=["POST", "GET"])
def edit(id):
    teacher = retrieve_teacher()
    student = teacher.students.pop(id)

    if request.method == 'GET':
        return render_template("app/edit.html", student=student)
    else:
        student.first_name = request.form.get("firstname")
        student.last_name = request.form.get("lastname")
        student.gender = request.form.get("gender")

        teacher.students[id] = student
        session['_teacher'] = serialize(teacher)
        return redirect(url_for(".show_students"))


@bp.route('/save')
def save():
    serialized_teacher = session.get("_teacher")
    resp = make_response(render_template("app/save.html"))
    if serialized_teacher is not None:
        expire_date = datetime.datetime.now() + datetime.timedelta(days=90)
        resp.set_cookie("_teacher", serialized_teacher, expires=expire_date)

    return resp


def retrieve_teacher():
    serialized_teacher = session.get("_teacher")
    if serialized_teacher is None:
        serialized_teacher = request.cookies.get('_teacher')

    if serialized_teacher is not None:
        return deserialize(serialized_teacher)

    return None
