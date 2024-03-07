from data import students

def add_student(name, id):
    student = {
        "name": name,
        "id": id
    }
    students.append(student)

def remove_student(id):
    for i, student in enumerate(students):
        if student["id"] == id:
            del students[i]
            return

def edit_student(id, name):
    for student in students:
        if student["id"] == id:
            student["name"] = name
            return

def print_students():
    for student in students:
        print(student)