class Student:

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.marks = {}

    def to_get_a_mark(self, mark, discipline):
        self.marks[discipline] = mark
        print(f'{self.name} {self.surname} получил оценку {mark} по курсу {self.course}, дисциплина {discipline}.')

    def display_student_marks(self):
        print(f'Студент: {self.name}, {self.surname}.\nКурс: {self.course}')
        for discipline, mark in self.marks.items():
            print(f'Дисциплина: {discipline} >> {mark}')


if __name__ == '__main__':
    students = [
        ['Иван', 'Иванов', 'Python'],
        ['Петр', 'Петров', 'QA'],
    ]

    students_objs = []
    for name, surname, course in students:
        students_objs.append(Student(name, surname, course))

    student_01, student_02 = students_objs
    student_01.to_get_a_mark(8, 'Строки')
    student_01.to_get_a_mark(9, 'Списки')
    student_01.to_get_a_mark(7, 'Словари')
    student_01.display_student_marks()
    print(student_01.marks)
    print()

    student_02.to_get_a_mark(10, 'Ручное Тестирование')
    student_02.to_get_a_mark(11, 'Основы Python')
    student_02.to_get_a_mark(9, 'Базы данных')
    student_02.display_student_marks()


