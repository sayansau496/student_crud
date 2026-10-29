"""
Student Management System - Simple CRUD project
Python + Flask + MySQL + HTML

Sayan Sir's Tutorials (CoE Kolkata)

CRUD  =  Create, Read, Update, Delete
    Create -> INSERT  (add_student)
    Read   -> SELECT  (index)
    Update -> UPDATE  (edit_student)
    Delete -> DELETE  (delete_student)
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "change-this-secret-key"   # needed for flash() messages

# ---------------------------------------------------------------
# STEP 1: Change the password below to YOUR MySQL root password
# ---------------------------------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "school_db",
}

STREAMS = ["Science", "Commerce", "Humanities"]


def get_connection():
    """Open a new connection to the MySQL database."""
    return mysql.connector.connect(**DB_CONFIG)


def read_form(form):
    """Read and check the data typed in the HTML form.
    Returns (data, error_message). error_message is None if all is OK."""
    roll_no = form.get("roll_no", "").strip()
    name = form.get("name", "").strip()
    section = form.get("section", "").strip().upper()
    stream = form.get("stream", "").strip()
    marks = form.get("marks", "").strip()

    if not (roll_no and name and section and stream and marks):
        return None, "Please fill in all the fields."
    if not (roll_no.isdigit() and marks.isdigit()):
        return None, "Roll number and marks must be numbers."
    if int(marks) > 100:
        return None, "Marks must be between 0 and 100."
    if stream not in STREAMS:
        return None, "Please choose a valid stream."
    if len(section) != 1 or not section.isalpha():
        return None, "Section must be a single letter (A, B, C ...)."

    return (int(roll_no), name, section, stream, int(marks)), None


# ---------------------------- READ ----------------------------
@app.route("/")
def index():
    search = request.args.get("q", "").strip()

    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    if search:
        like = "%" + search + "%"
        cur.execute(
            "SELECT * FROM students WHERE name LIKE %s OR roll_no LIKE %s ORDER BY roll_no",
            (like, like),
        )
    else:
        cur.execute("SELECT * FROM students ORDER BY roll_no")
    students = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", students=students, search=search)


# --------------------------- CREATE ---------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        data, error = read_form(request.form)
        if error:
            flash(error, "error")
            return render_template("form.html", title="Add Student",
                                   student=request.form, streams=STREAMS)

        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO students (roll_no, name, section, stream, marks) "
                "VALUES (%s, %s, %s, %s, %s)",
                data,
            )
            conn.commit()
            flash("Student added successfully!", "success")
            return redirect(url_for("index"))
        except mysql.connector.IntegrityError:
            flash("This roll number already exists.", "error")
            return render_template("form.html", title="Add Student",
                                   student=request.form, streams=STREAMS)
        finally:
            cur.close()
            conn.close()

    return render_template("form.html", title="Add Student",
                           student=None, streams=STREAMS)


# --------------------------- UPDATE ---------------------------
@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        data, error = read_form(request.form)
        if error:
            flash(error, "error")
            cur.close()
            conn.close()
            return render_template("form.html", title="Edit Student",
                                   student=request.form, streams=STREAMS)
        try:
            cur.execute(
                "UPDATE students SET roll_no=%s, name=%s, section=%s, "
                "stream=%s, marks=%s WHERE id=%s",
                data + (student_id,),
            )
            conn.commit()
            flash("Student updated successfully!", "success")
            return redirect(url_for("index"))
        except mysql.connector.IntegrityError:
            flash("This roll number already exists.", "error")
            return render_template("form.html", title="Edit Student",
                                   student=request.form, streams=STREAMS)
        finally:
            cur.close()
            conn.close()

    # GET request: show the form filled with the old values
    cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cur.fetchone()
    cur.close()
    conn.close()

    if student is None:
        flash("Student not found.", "error")
        return redirect(url_for("index"))

    return render_template("form.html", title="Edit Student",
                           student=student, streams=STREAMS)


# --------------------------- DELETE ---------------------------
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()
    flash("Student deleted.", "success")
    return redirect(url_for("index"))


# ------------------ friendly message if MySQL fails ------------------
@app.errorhandler(mysql.connector.Error)
def database_error(err):
    return (
        "<h2>Database error</h2>"
        "<p>%s</p>"
        "<p>Check that MySQL is running, the password in app.py is correct, "
        "and that you have run schema.sql.</p>" % err,
        500,
    )


if __name__ == "__main__":
    app.run(debug=True)
