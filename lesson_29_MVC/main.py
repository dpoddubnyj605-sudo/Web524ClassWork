from MVC_01_model import MarksModel
from MVC_02_view import MarksView
from MVC_03_controller import MarksController

if __name__ == '__main__':
    # model = MarksModel()
    # controller = MarksController(model)
    # view = MarksView(controller)
    view = MarksView(MarksController(MarksModel()))

    view.display_default_action()
    view.display_marks_auth('guest')
    view.display_marks_auth()
    view.display_only_marks_list()
    view.display_only_courses_list()
    view.display_all_data_list()
    print()

    view.display_add_mark('HTML', 10, 'marks_file.json', 'admin')
    view.display_add_mark('CSS', 11, 'marks_file.json', 'admin')
    view.display_add_mark('JavaScript', '12', 'marks_file.json', 'admin')
    view.display_add_mark('Python', 12, 'marks_file.json', 'admin')
    print()

    view.display_marks_auth()

    print()
    view.display_marks_auth('user_owner')
    view.display_only_marks_list('user_owner')
    view.display_all_data_list('user_owner')
    view.display_all_data_list()



