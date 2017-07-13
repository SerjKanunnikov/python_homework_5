
students = [{"name": "Mark", "surname": "Parks", "gender": "male", "exp": True, "marks": [7, 6, 6, 8, 7], "exam_mark": 5},
            {"name": "Adela", "surname": "Reynolds", "gender": "female", "exp": False, "marks": [5, 1, 3, 8, 8], "exam_mark": 5},
            {"name": "Jeanine", "surname": "Wilcox", "gender": "female", "exp": True, "marks": [8, 7, 9, 8, 6], "exam_mark": 2},
            {"name": "Gib", "surname": "Salmon", "gender": "male", "exp": False, "marks": [8, 6, 7, 8, 8], "exam_mark": 9},
            {"name": "Johnathan", "surname": "Bean", "gender": "male", "exp": True, "marks": [6, 5, 6, 7, 1], "exam_mark": 10},
            {"name": "Tricia", "surname": "Reynolds", "gender": "female", "exp": True, "marks": [8, 6, 7, 8, 8], "exam_mark": 9}]


def best_student():
    best_students = []
    for student in students:
        average_mark_homework = sum(student["marks"]) / len(student["marks"])
        integral_student_mark = 0.6 * average_mark_homework + 0.6 * student["exam_mark"]  
        integral_marks = {"name": student["name"],
                              "surname": student["surname"],
                              "integral_mark": integral_student_mark}
        print(integral_marks)
    best_mark = max((integral_marks["integral_mark"]) for mark in integral_marks)
    print("Лучший студент: {0} {1} с интегральной оценкой {2}".format(student["name"], student["surname"], best_mark))



def average_mark_group_homework():
    group_sum = 0
    for student in students:
        group_sum += sum(student["marks"])
    group_average = group_sum / len(students)
    print("Средняя оценка группы за домашние задания: ", group_average)


def average_mark_group_exam():
    group_sum = 0
    for student in students:
        group_sum += student["exam_mark"]
    group_average = group_sum / len(students)
    print("Средняя оценка группы за экзамен:", group_average)


def average_mark_male_students_homework():
    male_mark_sum = 0
    male_students = 0
    for student in students:
        if student["gender"] == "male":
            for mark in student["marks"]:
                male_mark_sum += mark
                male_students += 1
    average_mark = male_mark_sum / male_students
    print("Средняя оценка мужчин за экзамен:", average_mark)


def average_mark_male_students_exam():
    male_mark_sum = 0
    male_students = 0
    for student in students:
        if student["gender"] == "male":
            male_mark_sum += student["exam_mark"]
            male_students += 1
    average_mark = male_mark_sum / male_students
    print("Средняя оценка мужчин за экзамен:", average_mark)


def average_mark_female_students_homework():
    female_mark_sum = 0
    female_students = 0
    for student in students:
        if student["gender"] == "female":
            for mark in student["marks"]:
                female_mark_sum += mark
                female_students += 1
    average_mark = female_mark_sum / female_students
    print("Средняя оценка женщин за домашнюю работу:", average_mark)


def average_mark_female_students_exam():
    female_mark_sum = 0
    female_students = 0
    for student in students:
        if student["gender"] == "female":
            female_mark_sum += student["exam_mark"]
            female_students += 1
    average_mark = female_mark_sum / female_students
    print("Средняя оценка женщин за экзамен:", average_mark)


def average_mark_experienced_students_homework():
    mark_sum = 0
    experienced_students = 0
    for student in students:
        if student["exp"] == True:
            for mark in student["marks"]:
                mark_sum += mark
                experienced_students += 1
    average_mark = mark_sum / experienced_students
    print("Средняя оценка студентов с опытом за домашнюю работу:", average_mark)


def average_mark_experienced_students_exam():
    mark_sum = 0
    experienced_students = 0
    for student in students:
        if student["exp"] == True:
            mark_sum += student["exam_mark"]
            experienced_students += 1
    average_mark = mark_sum / experienced_students
    print("Средняя оценка студентов с опытом за экзамен:", average_mark)


def average_mark_inexperienced_students_homework():
    mark_sum = 0
    inexperienced_students = 0
    for student in students:
        if student["exp"] == False:
            for mark in student["marks"]:
                mark_sum += mark
                inexperienced_students += 1
    average_mark = mark_sum / inexperienced_students
    print("Средняя оценка студентов без опыта за домашнюю работу:", average_mark)


def average_mark_inexperienced_students_exam():
    mark_sum = 0
    inexperienced_students = 0
    for student in students:
        if student["exp"] == False:
            mark_sum += student["exam_mark"]
            inexperienced_students += 1
    average_mark = mark_sum / inexperienced_students
    print("Средняя оценка студентов без опыта за экзамен:", average_mark)


def command():
    while True:
        command_pick = input("Введите команду: \n"
                             "1. Средняя оценка за домашние задания по группе\n"
                             "2. Средняя оценка за экзамен по группе\n"
                             "3. Средняя оценка за домашние задания у мужчин\n"
                             "4. Средняя оценка за экзамен у мужчин\n"
                             "5. Средняя оценка за домашние задания у женщин\n"
                             "6. Средняя оценка за экзамен у женщин\n"
                             "7. Средняя оценка за домашние задания у студентов с опытом\n"
                             "8. Средняя оценка за экзамен у студентов с опытом\n"
                             "9. Средняя оценка за домашние задания у студентов без опыта\n"
                             "10. Средняя оценка за экзамен у студентов без опыта\n"
                             "11. Лучший студент\n")
        if command_pick == "1":
            average_mark_group_homework()
        elif command_pick == "2":
            average_mark_group_exam()
        elif command_pick == "3":
            average_mark_male_students_homework()
        elif command_pick == "4":
            average_mark_male_students_exam()
        elif command_pick == "5":
            average_mark_female_students_homework()
        elif command_pick == "6":
            average_mark_female_students_exam()
        elif command_pick == "7":
            average_mark_experienced_students_homework()
        elif command_pick == "8":
            average_mark_experienced_students_exam()
        elif command_pick == "9":
            average_mark_inexperienced_students_homework()
        elif command_pick == "10":
            average_mark_inexperienced_students_exam()
        elif command_pick == "11":
            best_student()
        else:
            print("Введите команду от 1 до 11\n")

command()
