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
        if ',' in entry:
            subject, grade = entry.split(',')
            subjects[subject.strip().title()] = float(grade.strip())
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades
def get_students(student_grades, keys):
    result = {}
    search = {name.lower(): name for name in student_grades.keys()}
    for key in keys:
        clean_key = key.strip().lower()
        if clean_key in search:
            original_name = search[clean_key]
            result[original_name] = student_grades[original_name]
        else:
            print(f"{key.strip().title()} not found!")
    return result
def avg_by_student(student_grades, keys = None):
    if keys is not None:
        dict = get_students(student_grades, keys)
    else:
        dict = student_grades
    for student, subjects in dict.items():
        if subjects:
            average = sum(subjects.values()) / len(subjects)
            print(f"{student}: {round(average, 1)}")
