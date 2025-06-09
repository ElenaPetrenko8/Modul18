import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']

students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']

students_marks = {}

for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]
        students_marks[student][class_] = marks


def print_all_grades():
    """Вывод всех оценок всех учеников"""
    for student in students:
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()


def print_student_grades(student):
    """Вывод всех оценок конкретного ученика"""
    if student in students_marks:
        print(f'Все оценки ученика {student}:')
        for class_ in classes:
            print(f'{class_} - {students_marks[student][class_]}')
    else:
        print('ОШИБКА: такого ученика нет в списке')


def print_student_averages(student: object) -> None:
    """Вывод среднего балла по предметам для конкретного ученика"""
    if student in students_marks:
        print(f'Средние баллы ученика {student}:')
        for class_ in classes:
            marks = students_marks[student][class_]
            avg = sum(marks) / len(marks)
            print(f'{class_} - {avg:.1f}')
    else:
        print('ОШИБКА: такого ученика нет в списке')


def add_student():
    """Добавление нового ученика"""
    name = input('Введите имя нового ученика: ')
    if name not in students:
        students.append(name)
        students.sort()
        students_marks[name] = {}
        for class_ in classes:
            students_marks[name][class_] = []
        print(f'Ученик {name} добавлен')
    else:
        print('ОШИБКА: такой ученик уже существует')


def remove_student():
    """Удаление ученика"""
    name = input('Введите имя ученика для удаления: ')
    if name in students:
        students.remove(name)
        del students_marks[name]
        print(f'Ученик {name} удален')
    else:
        print('ОШИБКА: такого ученика нет в списке')


def add_subject():
    """Добавление нового предмета"""
    subject = input('Введите название нового предмета: ')
    if subject not in classes:
        classes.append(subject)
        for student in students:
            students_marks[student][subject] = []
        print(f'Предмет {subject} добавлен')
    else:
        print('ОШИБКА: такой предмет уже существует')


def remove_subject():
    """Удаление предмета"""
    subject = input('Введите название предмета для удаления: ')
    if subject in classes:
        classes.remove(subject)
        for student in students:
            del students_marks[student][subject]
        print(f'Предмет {subject} удален')
    else:
        print('ОШИБКА: такого предмета нет в списке')


def edit_grade():
    """Редактирование оценки"""
    student = input('Введите имя ученика: ')
    if student not in students_marks:
        print('ОШИБКА: такого ученика нет в списке')
        return

    class_ = input('Введите предмет: ')
    if class_ not in students_marks[student]:
        print('ОШИБКА: такого предмета нет у ученика')
        return

    print(f'Текущие оценки: {students_marks[student][class_]}')
    try:
        index = int(input('Введите номер оценки для редактирования (начиная с 0): '))
        if 0 <= index < len(students_marks[student][class_]):
            new_grade = int(input('Введите новую оценку (1-5): '))
            if 1 <= new_grade <= 5:
                students_marks[student][class_][index] = new_grade
                print('Оценка изменена')
            else:
                print('ОШИБКА: оценка должна быть от 1 до 5')
        else:
            print('ОШИБКА: неверный номер оценки')
    except ValueError:
        print('ОШИБКА: введите число')


print('''
Список команд:
1. Добавить оценку ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Вывести все оценки определенного ученика
5. Вывести средний балл по предметам для определенного ученика
6. Добавить нового ученика
7. Удалить ученика
8. Добавить новый предмет
9. Удалить предмет
10. Редактировать оценку
11. Выход из программы
''')

while True:
    try:
        command = int(input('Введите команду: '))

        if command == 1:
            print('1. Добавить оценку ученика по предмету')
            student = input('Введите имя ученика: ')
            class_ = input('Введите предмет: ')
            if student in students_marks and class_ in students_marks[student]:
                mark = int(input('Введите оценку (1-5): '))
                if 1 <= mark <= 5:
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                else:
                    print('ОШИБКА: оценка должна быть от 1 до 5')
            else:
                print('ОШИБКА: неверное имя ученика или название предмета')

        elif command == 2:
            print('2. Вывести средний балл по всем предметам по каждому ученику')
            for student in students:
                print(student)
                for class_ in classes:
                    marks = students_marks[student][class_]
                    if marks:
                        avg = sum(marks) / len(marks)
                        print(f'{class_} - {avg:.1f}')
                    else:
                        print(f'{class_} - нет оценок')
                print()

        elif command == 3:
            print('3. Вывести все оценки по всем ученикам')
            print_all_grades()

        elif command == 4:
            print('4. Вывести все оценки определенного ученика')
            student = input('Введите имя ученика: ')
            print_student_grades(student)

        elif command == 5:
            print('5. Вывести средний балл по предметам для определенного ученика')
            student = input('Введите имя ученика: ')
            print_student_averages(student)

        elif command == 6:
            print('6. Добавить нового ученика')
            add_student()

        elif command == 7:
            print('7. Удалить ученика')
            remove_student()

        elif command == 8:
            print('8. Добавить новый предмет')
            add_subject()

        elif command == 9:
            print('9. Удалить предмет')
            remove_subject()

        elif command == 10:
            print('10. Редактировать оценку')
            edit_grade()

        elif command == 11:
            print('11. Выход из программы')
            break

        else:
            print('ОШИБКА: неверная команда')

    except ValueError:
        print('ОШИБКА: введите число от 1 до 11')