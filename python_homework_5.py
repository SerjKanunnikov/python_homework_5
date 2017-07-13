import operator

students = [{"name": "Mark", "surname": "Parks", "gender": "male", "exp": True, "marks": [7, 6, 6, 8, 7], "exam_mark": 5},
            {"name": "Adela", "surname": "Reynolds", "gender": "female", "exp": False, "marks": [5, 1, 3, 8, 8], "exam_mark": 5},
            {"name": "Jeanine", "surname": "Wilcox", "gender": "female", "exp": True, "marks": [8, 7, 9, 8, 6], "exam_mark": 2},
            {"name": "Gib", "surname": "Salmon", "gender": "male", "exp": False, "marks": [8, 6, 7, 8, 8], "exam_mark": 9},
            {"name": "Johnathan", "surname": "Bean", "gender": "male", "exp": True, "marks": [6, 5, 6, 7, 1], "exam_mark": 10},
            {"name": "Tricia", "surname": "Reynolds", "gender": "female", "exp": True, "marks": [8, 6, 7, 8, 8], "exam_mark": 9}]


def best_student():
    for student in students:
        average_mark_homework = sum(student["marks"]) / len(student["marks"])  # вычисление средней оценки за д/з
        integral_student_mark = 0.6 * average_mark_homework + 0.6 * student["exam_mark"]  # вычисление интегральной оценки
        integral_marks = {"name": student["name"],  # словарь с интегральными оценками всех студентов
                          "surname": student["surname"],
                          "integral_mark": integral_student_mark}
        #print(integral_marks)
        best_mark = max((integral_marks["integral_mark"]) for mark in integral_marks)  # поиск лучшей оценки среди интегральных
        best_students = {"name": student["name"], "surname": student["surname"], "mark": best_mark}
    print(best_students)
    print("Best student is {0} {1} with a {2} mark".format(best_students["name"], best_students["surname"], best_students["mark"]))



def average_mark_group_homework():
    group_sum = 0
    for student in students:
        group_sum += sum(student["marks"])
    group_average = group_sum / len(students)
    print("Average group mark for homework: ", group_average)


def average_mark_group_exam():
    group_sum = 0
    for student in students:
        group_sum += student["exam_mark"]
    group_average = group_sum / len(students)
    print("Average group mark for exam: ", group_average)


def average_mark_male_students_homework():
    male_mark_sum = 0
    male_students = 0
    for student in students:
        if student["gender"] == "male":
            for mark in student["marks"]:
                male_mark_sum += mark
                male_students += 1
    average_mark = male_mark_sum / male_students
    print("Average mark of male students for homework — ", average_mark)


def average_mark_male_students_exam():
    male_mark_sum = 0
    male_students = 0
    for student in students:
        if student["gender"] == "male":
            male_mark_sum += student["exam_mark"]
            male_students += 1
    average_mark = male_mark_sum / male_students
    print("Average mark of male students for exam — ", average_mark)


def average_mark_female_students_homework():
    female_mark_sum = 0
    female_students = 0
    for student in students:
        if student["gender"] == "female":
            for mark in student["marks"]:
                female_mark_sum += mark
                female_students += 1
    average_mark = female_mark_sum / female_students
    print("Average mark of female students for homework — ", average_mark)


def average_mark_female_students_exam():
    female_mark_sum = 0
    female_students = 0
    for student in students:
        if student["gender"] == "female":
            female_mark_sum += student["exam_mark"]
            female_students += 1
    average_mark = female_mark_sum / female_students
    print("Average mark of female students for exam — ", average_mark)


def average_mark_experienced_students_homework():
    mark_sum = 0
    experienced_students = 0
    for student in students:
        if student["exp"] == True:
            for mark in student["marks"]:
                mark_sum += mark
                experienced_students += 1
    average_mark = mark_sum / experienced_students
    print("Average mark of experienced students for homework — ", average_mark)


def average_mark_experienced_students_exam():
    mark_sum = 0
    experienced_students = 0
    for student in students:
        if student["exp"] == True:
            mark_sum += student["exam_mark"]
            experienced_students += 1
    average_mark = mark_sum / experienced_students
    print("Average mark of experienced students for exam — ", average_mark)


def average_mark_inexperienced_students_homework():
    mark_sum = 0
    inexperienced_students = 0
    for student in students:
        if student["exp"] == False:
            for mark in student["marks"]:
                mark_sum += mark
                inexperienced_students += 1
    average_mark = mark_sum / inexperienced_students
    print("Average mark of inexperienced students for homework — ", average_mark)


def average_mark_inexperienced_students_exam():
    mark_sum = 0
    inexperienced_students = 0
    for student in students:
        if student["exp"] == False:
            mark_sum += student["exam_mark"]
            inexperienced_students += 1
    average_mark = mark_sum / inexperienced_students
    print("Average mark of inexperienced students for exam — ", average_mark)


best_student()
# average_mark_group_homework()
# average_mark_group_exam()
# average_mark_male_students_homework()
# average_mark_male_students_exam()
# average_mark_female_students_homework()
# average_mark_female_students_exam()
# average_mark_experienced_students_homework()
# average_mark_experienced_students_exam()
# average_mark_inexperienced_students_homework()
# average_mark_inexperienced_students_exam()
