from MVC_01_model import MarksModel


def check_access_role(user_role, available_roles):
    if user_role not in available_roles:
        return 'Forbidden'
    return True


class MarksController:
    IS_SUPERUSER = 'is_superuser'
    IS_STAFF = 'is_staff'
    USER_OWNER = 'user_owner'
    GUEST = 'guest'

    def __init__(self, model: MarksModel):
        self.model = model

    def get_default_action(self):
        return 'Добро пожаловать на главную страницу'

    def get_marks_auth(self, user_role=GUEST, available_roles=(IS_SUPERUSER, IS_STAFF, USER_OWNER)):
        if user_role not in available_roles:
            return 'Forbidden'
        if self.model.student_marks:
            return self.model.student_marks
        return None

    #
    # def get_marks_auth(self, user_role=GUEST, available_roles=(IS_SUPERUSER, IS_STAFF, USER_OWNER)):
    #     user_check_result = check_access_role(user_role, available_roles)
    #     if user_check_result is True:
    #         if self.model.student_marks:
    #             return self.model.student_marks
    #         return None
    #     return user_check_result

    def get_only_courses_list(self):
        courses = []
        data = self.model.student_marks
        if data:
            for element in data:
                courses.append(element['course'])
            return courses
        return None

    def get_only_marks_list(self, user_role=GUEST, available_roles=(IS_SUPERUSER, IS_STAFF, USER_OWNER)):
        if user_role not in available_roles:
            return 'Forbidden!'
        marks = []
        data = self.model.student_marks
        if data:
            for element in data:
                marks.append(element['mark'])
            return marks
        return None

    def get_all_data_list(self, user_role=GUEST):
        available_roles = (MarksController.IS_SUPERUSER, MarksController.IS_STAFF, MarksController.USER_OWNER)
        user_check_result = check_access_role(user_role, available_roles)
        if user_check_result:
            if self.model.student_marks:
                return self.get_only_courses_list(), self.get_only_marks_list(user_role)
            return None
        return user_check_result

    def add_mark(self, course, mark, filename, user_role=GUEST):
        available_roles = (MarksController.IS_SUPERUSER, MarksController.IS_STAFF)
        user_check_result = check_access_role(user_role, available_roles)
        if user_check_result:
            if isinstance(mark, int):
                self.model.add_mark(course, mark, filename)
                return True
            return False
        return user_check_result
