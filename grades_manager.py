def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}
def add_student(student_grades = None):
    if student_grades is None:
        student_grades = {}
    name = input("Enter student name: ").strip().title()
    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ").strip()
        if entry.lower() == 'exit':
            break
        subject, grade = entry.split()