from string import Template

# my_template = Template("$user_login имеет права: $user_access, в приложении $app_name")
#
# my_string1 = my_template.substitute(user_login="Admin",
#                                     user_access='superuser',
#                                     app_name="E-Shop")
#
# my_string2 = my_template.substitute(user_login="User1787",
#                                     user_access='read-only',
#                                     app_name="E-Shop")
#
# print(my_string1)
# print(my_string2)

my_template = Template("$user_login имеет права: $user_access, в приложении $user_app_name")
users_list = []

for i in range(3):
    user_login = input("Логин: ")
    user_access = input("Права: ")
    user_app_name = input('Приложение: ')
    user_info = my_template.substitute(user_login=user_login,
                                       user_access=user_access,
                                       user_app_name=user_app_name)
    users_list.append(user_info)


for user in users_list:
    print(user)
