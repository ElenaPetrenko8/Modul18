import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

for student in students:
    students_marks[student] = {}
    # цикл по предметам
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks

for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести все оценки определенного ученика
        5. Вывести средний балл по каждому предмету для определенного ученика
        6. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')

        student = input('Введите имя ученика: ')

        class_ = input('Введите предмет: ')

        mark = int(input('Введите оценку: '))

        if student in students_marks.keys() and class_ in students_marks[student].keys():

            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')

        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')

        for student in students:
            print(student)

            for class_ in classes:

                marks_sum = sum(students_marks[student][class_])

                marks_count = len(students_marks[student][class_])

                print(f'{class_} - {marks_sum / marks_count:.1f}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')

        for student in students:
            print(student)

            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Вывести все оценки определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Все оценки для ученика {student}:')
            for class_ in classes:
                print(f'{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: такого ученика нет в списке')
    elif command == 5:
        print('5. Вывести средний балл по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Средние баллы для ученика {student}:')
            for class_ in classes:
                marks = students_marks[student][class_]
                avg = sum(marks) / len(marks)
                print(f'{class_} - {avg:.1f}')
        else:
            print('ОШИБКА: такого ученика нет в списке')
    elif command == 6:
        print('6. Выход из программы')
        break

print(f'Список студентов: {students}')

name = input('Введите имя студента, которого нужно удалить: ')

if name in students:

    students.remove(name)
    print('Студент удален из списка.')
else:
    print('Данного студента в списке нет.')

print(f'Список студентов: {students}')


students.sort()
print(f'Сортировка в порядке возрастания: {students}')

students.sort(reverse=True)
print(f'Сортировка в порядке убывания: {students}')


students_name = input('Введите имя клиента: ')


if students_name in students:
    print('Студент есть в списке')
else:
    print('Студента нет в списке. Вносим его в список.')
    students.append(students_name)
print(f'Список студентов: {students}')


print('Редактируем запись в списке оценок:')
student = input('Введите имя студента: ')
if student in students_marks:
    class_ = input('Введите предмет: ')
    if class_ in students_marks[student]:
        print(f'Текущие оценки: {students_marks[student][class_]}')
        new_mark = int(input('Введите новую оценку для добавления: '))
        students_marks[student][class_].append(new_mark)
        print(f'Обновленные оценки: {students_marks[student][class_]}')
    else:
        print('ОШИБКА: такого предмета нет у ученика')
else:
    print('ОШИБКА: такого ученика нет в списке')