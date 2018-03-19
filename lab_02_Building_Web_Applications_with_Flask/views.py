import datetime

from flask import request, render_template, Flask, redirect, url_for, make_response, session
from lab_02_Building_Web_Applications_with_Flask.models import Teacher, Student
from lab_02_Building_Web_Applications_with_Flask.serialize import deserialize, serialize

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    teacher = retrieve_teacher()
    if teacher is None:
        return redirect(url_for("register"))

    return redirect(url_for("show_students"))


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form.get("name")
        course = request.form.get("course")
        teacher = Teacher(name, course)

        session["_teacher"] = serialize(teacher)
        return redirect(url_for("index"))


@app.route('/students', methods=["GET"])
def show_students():
    teacher = retrieve_teacher()
    if teacher is None:
        return redirect("register")
    else:
        return render_template("students.html", students=teacher.students.values())


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        id = request.form.get("id")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        gender = request.form.get("gender")

        teacher = retrieve_teacher()
        teacher.students[id] = Student(id, firstname, lastname, gender)
        session['_teacher'] = serialize(teacher)

        return redirect(url_for("show_students"))


@app.route('/delete/<id>', methods=["GET", "POST", "DELETE"])
def delete(id):
    teacher = retrieve_teacher()
    teacher.students.pop(id)
    session['_teacher'] = serialize(teacher)

    return redirect(url_for("show_students"))


@app.route('/edit/<id>', methods=["POST", "GET"])
def edit(id):
    teacher = retrieve_teacher()
    student = teacher.students.pop(id)

    if request.method == 'GET':
        return render_template("edit.html", student=student)
    else:
        student.first_name = request.form.get("firstname")
        student.last_name = request.form.get("lastname")
        student.gender = request.form.get("gender")

        teacher.students[id] = student
        session['_teacher'] = serialize(teacher)
        return redirect(url_for("show_students"))


@app.route('/save')
def save():
    serialized_teacher = session.get("_teacher")
    resp = make_response(render_template("save.html"))
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


if __name__ == "__main__":
   app.secret_key = 'SPECIFY_YOUR_OWN_SECRET_KEY'
   app.config['SESSION_TYPE'] = 'filesystem'
   app.run()