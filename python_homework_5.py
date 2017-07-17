
students = [{"name": "Mark", "surname": "Parks", "gender": "male", "exp": True, "marks": [7, 6, 6, 8, 7], "exam_mark": 5},
            {"name": "Adela", "surname": "Reynolds", "gender": "female", "exp": False, "marks": [5, 1, 3, 8, 8], "exam_mark": 5},
            {"name": "Jeanine", "surname": "Wilcox", "gender": "female", "exp": True, "marks": [8, 7, 9, 8, 6], "exam_mark": 2},
            {"name": "Gib", "surname": "Salmon", "gender": "male", "exp": False, "marks": [8, 6, 7, 8, 8], "exam_mark": 9},
            {"name": "Johnathan", "surname": "Bean", "gender": "male", "exp": True, "marks": [6, 5, 6, 7, 1], "exam_mark": 7},
            {"name": "Tricia", "surname": "Reynolds", "gender": "female", "exp": True, "marks": [8, 6, 7, 8, 8], "exam_mark": 9}]


def best_student():
    integral_marks = []  # Список студентов и их интегральных оценов
    max_integral_mark = 0  # Максимальная интегральная оценка
    best_students = []  # Список студентов, чья интегральная оценка равна максимальной
    for student in students:
        average_mark_homework = sum(student["marks"]) / len(student["marks"])  # Средняя оценка студента за домашнюю работу
        integral_student_mark = 0.6 * average_mark_homework + 0.4 * student["exam_mark"]  # Интегральная оценка студента
        integral_marks.append({"name": student["name"],
                               "surname": student["surname"],
                               "integral_mark": integral_student_mark})  # Пополнение списка интегральных оценок
        max_integral_mark = max(mark["integral_mark"] for mark in integral_marks)  # Поиск максимальной интегральной оценки
    for student in integral_marks:
        if student["integral_mark"] == max_integral_mark:  # Сравнение интегральной оценки студента с максимальной
            best_students.append({"name": student["name"],
                                  "surname": student["surname"],
                                  "integral_mark": integral_student_mark})  # Пополнение списка лучших студентов
    if len(best_students) == 1:  # Вывод одного лучшего студента
        print("Лучший студент: {0} {1} с баллом {2}".format(student["name"], student["surname"], round(student["integral_mark"]), 3))
    if len(best_students) > 1:  # Вывод нескольких оучших студентов
        print("Лучшие студенты: ", end='')
        for student in best_students:
            print("{} {}".format(student["name"], student["surname"]), end=", ")
        print("с интегральным баллом {}".format(round(student["integral_mark"]), 3))


def average_mark_group_homework():
    group_sum = 0
    for student in students:
        group_sum += sum(student["marks"])
    group_average = group_sum / len(students) / len(student["marks"])
    print("Средняя оценка группы за домашние задания: ", round(group_average, 1))


def average_mark_group_exam():
    group_sum = 0
    for student in students:
        group_sum += student["exam_mark"]
    group_average = group_sum / len(students)
    print("Средняя оценка группы за экзамен:", round(group_average, 1))


def average_mark_for_homework_by_gender():
    gender = input("Выберите пол стдентов (М/Ж): \n")
    mark_sum = 0
    if gender == "М":
        male_students = 0
        for student in students:
            if student["gender"] == "male":
                for mark in student["marks"]:
                    mark_sum += mark
                    male_students += 1
        average_mark = mark_sum / male_students
        print("Средняя оценка мужчин за экзамен: \n", round(average_mark, 1))
    elif gender == "Ж":
        mark_sum = 0
        female_students = 0
        for student in students:
            if student["gender"] == "female":
                for mark in student["marks"]:
                    mark_sum += mark
                    female_students += 1
        average_mark = mark_sum / female_students
        print("Средняя оценка женщин за домашнюю работу:", round(average_mark, 1))
    else:
        print("Правильно укажите пол: М или Ж")


def average_mark_for_exam_by_gender():
    gender = input("Выберите пол стдентов (М/Ж): \n")
    mark_sum = 0
    if gender == "М":
        male_students = 0
        for student in students:
            if student["gender"] == "male":
                mark_sum += student["exam_mark"]
                male_students += 1
        average_mark = mark_sum / male_students
        print("Средняя оценка мужчин за экзамен:", round(average_mark, 1))
    elif gender == "Ж":
        female_students = 0
        for student in students:
            if student["gender"] == "female":
                mark_sum += student["exam_mark"]
                female_students += 1
        average_mark = mark_sum / female_students
        print("Средняя оценка женщин за экзамен:", round(average_mark, 1))
    else:
        print("Правильно укажите пол: М или Ж")


def average_mark_for_homework_by_experience():
    experience = input("Вывести среднюю оценку за домашние работы у студентов: \n"
                       "1. С опытом \n"
                       "2. Без опыта \n")
    mark_sum = 0
    if experience == "1":
        experienced_students = 0
        for student in students:
            if student["exp"] == True:
                for mark in student["marks"]:
                    mark_sum += mark
                    experienced_students += 1
        average_mark = mark_sum / experienced_students
        print("Средняя оценка студентов с опытом за домашнюю работу:", round(average_mark, 1))
    elif experience == "2":
        inexperienced_students = 0
        for student in students:
            if student["exp"] == False:
                for mark in student["marks"]:
                    mark_sum += mark
                    inexperienced_students += 1
        average_mark = mark_sum / inexperienced_students
        print("Средняя оценка студентов без опыта за домашнюю работу:", round(average_mark, 1))
    else:
        print("Правильно укажите опыт студентов: 1 - студенты с опытом, 2 - студенты без опыта\n")


def average_mark_for_exam_by_experience():
    experience = input("Вывести среднюю оценку за экзамен у студентов: \n"
                       "1. С опытом \n"
                       "2. Без опыта \n")
    mark_sum = 0
    if experience == "1":
        experienced_students = 0
        for student in students:
            if student["exp"] == True:
                mark_sum += student["exam_mark"]
                experienced_students += 1
        average_mark = mark_sum / experienced_students
        print("Средняя оценка студентов с опытом за экзамен:", round(average_mark, 1))
    elif experience == "2":
        inexperienced_students = 0
        for student in students:
            if student["exp"] == False:
                mark_sum += student["exam_mark"]
                inexperienced_students += 1
        average_mark = mark_sum / inexperienced_students
        print("Средняя оценка студентов без опыта за экзамен:", round(average_mark, 1))
    else:
        print("Правильно укажите опыт студентов: 1 - студенты с опытом, 2 - студенты без опыта\n")


def command():
    while True:
        command_pick = input("Введите команду: \n"
                             "1. Средняя оценка за домашние задания по группе\n"
                             "2. Средняя оценка за экзамен по группе\n"
                             "3. Средняя оценка за домашние задания в зависимости от пола студентов\n"
                             "4. Средняя оценка за экзамен в зависимости от пола студентов\n"
                             "5. Средняя оценка за домашние задания в зависимости от опыта студентов\n"
                             "6. Средняя оценка за экзамен в зависимости от опыта студентов\n"
                             "7. Лучший студент\n")
        if command_pick == "1":
            average_mark_group_homework()
        elif command_pick == "2":
            average_mark_group_exam()
        elif command_pick == "3":
            average_mark_for_homework_by_gender()
        elif command_pick == "4":
            average_mark_for_exam_by_gender()
        elif command_pick == "5":
            average_mark_for_homework_by_experience()
        elif command_pick == "6":
            average_mark_for_exam_by_experience()
        elif command_pick == "7":
            best_student()

command()
