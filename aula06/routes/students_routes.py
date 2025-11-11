from flask import Blueprint, render_template, request, redirect
from database.connection import insert_student, calculate_average, get_all_notes, get_note_by_id, edit_note, delete_note

studants_routes = Blueprint('students', __name__)

@studants_routes.route('/students')
def list_students():
    list_all_notes = get_all_notes()
    return render_template('students.html', students=list_all_notes)


@studants_routes.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_students.html')
    else:
        name = request.form['name']
        note1 = request.form['note1']
        note2 = request.form['note2']
        note3 = request.form['note3']
        average = calculate_average(note1, note2, note3)
        insert_student(name, note1, note2, note3, average)
        return redirect('/students')


@studants_routes.route('/students/edit-student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'GET':
        student_note = get_note_by_id(student_id)
        return render_template('edit_students.html', student=student_note)
    elif request.method == 'POST':
        name = request.form['name']
        note1 = request.form['note1']
        note2 = request.form['note2']
        note3 = request.form['note3']
        average = calculate_average(note1, note2, note3)
        edit_note(student_id, name, note1, note2, note3, average)
        return redirect('/students')


@studants_routes.route('/students/delete-student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    delete_note(student_id)
    return redirect('/students')
