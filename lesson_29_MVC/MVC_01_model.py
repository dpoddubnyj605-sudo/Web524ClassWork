import json


class MarksModel:

    def __init__(self):
        self.__student_marks = []

    @property
    def student_marks(self):
        return self.__student_marks

    def add_mark(self, course, mark, filename):
        data = {}
        data['course'] = course
        data['mark'] = mark
        self.student_marks.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.__student_marks, fp, ensure_ascii=False, indent=4)

    def calculate_average_mark(self):
        overall_score = 0
        for mark in self.student_marks:
            overall_score += mark['mark']
        return round(overall_score / len(self.student_marks), 2)

#
# if __name__ == '__main__':
#     user_name = input('Введите ваше имя: ')
#     user_filename = fr'student_marks_files\{user_name}_mark_file.json'
#     marks_model = MarksModel()
#     print(marks_model.student_marks)
#     marks_model.add_mark('HTML', 10, user_filename)
#     marks_model.add_mark('CSS', 12, user_filename)
#     marks_model.add_mark('JavaScript', 9, user_filename)
#     marks_model.add_mark('Python', 11, user_filename)
#     print(marks_model.student_marks)
#     print(marks_model.calculate_average_mark())
