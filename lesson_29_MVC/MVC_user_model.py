class UserRoles:
    admin = 'is_superuser'
    staff = 'is_staff'
    user = 'user'


class User:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.__role = UserRoles.user

    def get_role(self):
        return self.__role

    def set_role(self, new_role, user_obj):
        if self.__role == UserRoles.admin:
            user_obj.__role = new_role
            print(f'Уровень доступа изменен на: {new_role}')
        else:
            print(f'Доступ запрещен, изменять роли может только Admin')

    def create_superuser(self):
        self.__role = UserRoles.admin


if __name__ == '__main__':
    userAdmin = User('Admin', 'Adminov')
    userAdmin.create_superuser()

    userGuest = User('Ivan', 'Ivanov')
    userGuest.set_role('is_staff', userGuest)
    userAdmin.set_role('is_staff', userGuest)
