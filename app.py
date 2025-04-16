from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="student_db"
)
cursor = db.cursor()

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None  # Initialize error variable
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        try:
            # Verify database connection
            if not db.is_connected():
                db.reconnect()
                
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            
            if user:
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid username or password"  # Set error message
        except mysql.connector.Error as err:
            error = f"Database error: {err}"
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('login.html', error=error)

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return render_template('dashboard.html', students=students)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Add Student Route
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    try:
        # Get department data for dropdowns
        cursor.execute("SELECT * FROM department")
        departments = cursor.fetchall()

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

        return render_template('add_student.html', departments=departments)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Department Routes

# View departments
@app.route('/department')
def department():
    try:
        cursor.execute("SELECT * FROM department")
        departments = cursor.fetchall()
        return render_template('department.html', departments=departments)
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Add a new department
@app.route('/add_department', methods=['POST'])
def add_department():
    try:
        data = request.get_json()
        course_name = data['course_name']
        mentor_name = data['mentor_name']

        cursor.execute(
            "INSERT INTO department (course_name, mentor_name) VALUES (%s, %s)",
            (course_name, mentor_name)
        )
        db.commit()
        return jsonify({"success": True, "message": "Department added successfully"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

# Delete department
@app.route('/delete_department/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    try:
        cursor.execute("DELETE FROM department WHERE id = %s", (department_id,))
        db.commit()
        return jsonify({"success": True, "message": "Department deleted successfully"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

# Edit Student Route
@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'POST':
        reg_number = request.form['reg_number']
        name = request.form['name']
        phone_number = request.form['phone_number']
        course_name = request.form['course_name']
        mentor = request.form['mentor']

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
@app.route('/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        db.commit()
        return jsonify({"success": True, "message": "Student deleted successfully"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

# Profile Route
@app.route('/profile')
def profile():
    try:
        cursor.execute("SELECT id, username, password FROM users")
        users = cursor.fetchall()
        return render_template('profile.html', users=users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/marks')
def marks():
    return render_template('marks.html')

@app.route('/upload_marks', methods=['GET', 'POST'])
def upload_marks():
    try:
        cursor.execute("SELECT reg_number FROM students")
        students = cursor.fetchall()
        reg_numbers = [student[0] for student in students]  # Extract register numbers

        print("Registration Numbers: ", reg_numbers)  # Debugging print

        return render_template('upload.html', reg_numbers=reg_numbers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to fetch student details by reg number
@app.route('/get_student_info/<reg_number>', methods=['GET'])
def get_student_info(reg_number):
    cursor.execute("SELECT name, phone_number, course_name, mentor FROM students WHERE reg_number = %s", (reg_number,))
    student = cursor.fetchone()
    if student:
        return jsonify({"success": True, "student": {
            "name": student[0],
            "phone_number": student[1],
            "course_name": student[2],
            "mentor": student[3]
        }})
    return jsonify({"success": False, "message": "Student not found"}), 404

@app.route('/check_marks/<reg_number>/<semester>', methods=['GET'])
def check_marks(reg_number, semester):
    try:
        cursor.execute("SELECT * FROM marks WHERE reg_number = %s AND semester = %s", 
                      (reg_number, semester))
        exists = cursor.fetchone() is not None
        return jsonify({"exists": exists})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to submit marks
@app.route('/submit_marks', methods=['POST'])
def submit_marks():
    try:
        data = request.get_json()
        reg_number = data.get('reg_number')
        semester = data.get('semester')
        marks_data = data.get('marks')  # Array of subjects and marks

        # Check if marks already exist for that student and semester
        cursor.execute("SELECT * FROM marks WHERE reg_number = %s AND semester = %s", (reg_number, semester))
        existing = cursor.fetchone()
        if existing:
            return jsonify({"success": False, "message": "Marks already updated for the selected Semester"})

        # Insert new marks
        for entry in marks_data:
            subject = entry.get('subject')
            mark = entry.get('mark')
            
            # Remove isdigit() check since mark is already converted to int in JavaScript
            if not isinstance(mark, int):
                return jsonify({"success": False, "message": "Marks must be numeric"})
                
            if mark < 0 or mark > 100:
                return jsonify({"success": False, "message": "Marks must be between 0 and 100"})
                
            cursor.execute("INSERT INTO marks (reg_number, semester, subject, mark) VALUES (%s, %s, %s, %s)",
                          (reg_number, semester, subject, mark))

        db.commit()
        return jsonify({"success": True, "message": "Marks submitted successfully"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    
@app.route('/view_marks')
def view_marks_page():
    try:
        cursor.execute("SELECT reg_number FROM students")
        students = cursor.fetchall()
        reg_numbers = [student[0] for student in students]
        return render_template('view_marks.html', reg_numbers=reg_numbers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_marks/<reg_number>/<semester>')
def get_marks(reg_number, semester):
    try:
        cursor.execute("SELECT subject, mark FROM marks WHERE reg_number = %s AND semester = %s", 
                      (reg_number, semester))
        marks = cursor.fetchall()
        if marks:
            return jsonify({
                "success": True,
                "marks": [{"subject": mark[0], "mark": mark[1]} for mark in marks]
            })
        return jsonify({"success": False, "message": "No marks found"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
