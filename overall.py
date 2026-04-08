dict_students = {
    "student1":{"assignment1":80,"assignment2":90,"assignment3":100},
    "student2":{"assignment1":70,"assignment2":75,"assignment3":85},
    "student3":{"assignment1":95,"assignment2":85,"assignment3":90}
}

def calc_average(student_assignments):
    average = 0
    for assignment_score_key in student_assignments:
        average += student_assignments.get(assignment_score_key)
    average /= len(student_assignments)
    average = round(average)
    return average

def student_averages(dict_students):
    avg_students = {}
    for clave in dict_students:
        avg_students[clave] = calc_average(dict_students.get(clave))
    print(avg_students)

def assignment_averages(dict_students):
    avg_assignments = {}
    for student in dict_students:
        for assignment in dict_students[student]:
            if assignment in avg_assignments:
                avg_assignments[assignment] += dict_students.get(student)[assignment]
            else:
                avg_assignments[assignment] = dict_students.get(student)[assignment]
    for key in avg_assignments:
        avg_assignments[key] /= len(dict_students)
        avg_assignments[key] = round(avg_assignments[key])
    print(avg_assignments)

student_averages(dict_students)
assignment_averages(dict_students)