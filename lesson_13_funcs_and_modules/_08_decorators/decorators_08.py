from functools import wraps
from datetime import datetime


def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        with open(r'logs\actions.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f'{datetime.now()} >> User: {username}, action: {func.__name__}\n')
        return func(username, *args, **kwargs)

    return wrapper


@log_action
def login(username):
    print(f'{username} вошел в систему.')


@log_action
def update_profile(username, profile_data):
    print(f'{username} обновил профиль с данными: {profile_data}')


if __name__ == '__main__':
    login('Alice')
    update_profile("Alice", [25, 'Москва'])
