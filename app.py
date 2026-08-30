from flask import Flask, render_template, request
from database import init_db, save_result

app = Flask(__name__)
init_db()

def calculate_result(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    percentage = round(total / 3, 2)
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"
    return total, percentage, grade

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll_no = request.form['roll_no']
    marks1 = int(request.form['marks1'])
    marks2 = int(request.form['marks2'])
    marks3 = int(request.form['marks3'])

    total, percentage, grade = calculate_result(marks1, marks2, marks3)
    save_result(name, roll_no, marks1, marks2, marks3, total, percentage, grade)

    return render_template('result.html', name=name, roll_no=roll_no,
                            total=total, percentage=percentage, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
