from flask import Flask, render_template,request, redirect, url_for
import mysql.connector
app = Flask(__name__)

# Login Page
@app.route('/')
def login():
    return render_template('login.html')

# Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="student_db"
)
cursor = db.cursor()


# Dashboard Route
@app.route('/dashboard')
def dashboard():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('dashboard.html', students=students)

# Add Student Route
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        reg_number = request.form['reg_number']
        name = request.form['name']
        phone_number = request.form['phone_number']
        course_name = request.form['course_name']
        mentor = request.form['mentor']

        cursor.execute(
            "INSERT INTO students (reg_number, name, phone_number, course_name, mentor) VALUES (%s, %s, %s, %s, %s)",
            (reg_number, name, phone_number, course_name, mentor)
        )
        db.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_student.html')

# Edit Student Route
@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'POST':
        reg_number = request.form['reg_number']
        name = request.form['name']
        phone_number = request.form['phone_number']
        course_name = request.form['course_name']
        mentor = request.form['mentor']
        profile_pic = request.files['profile_pic']


        cursor.execute(
            "UPDATE students SET reg_number=%s, name=%s, phone_number=%s, course_name=%s, mentor=%s WHERE id=%s",
            (reg_number, name, phone_number, course_name, mentor, student_id)
        )
        db.commit()
        return redirect(url_for('dashboard'))

    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    return render_template('edit_student.html', student=student)
# Delete Student Route
@app.route('/delete_student/<int:student_id>')

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    db.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
