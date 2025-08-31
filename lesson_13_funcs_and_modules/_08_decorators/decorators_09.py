from functools import wraps


def authorise_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user[1] == 'admin':
            return func(user, *args, **kwargs)
        else:
            print(f'Acces denied for: {user[0]}!')

    return wrapper


@authorise_admin
def view_secret_data(user):
    print(f'Secret data for {user[0]}, status {user[1]}')


if __name__ == '__main__':
    view_secret_data(['Alice', 'admin'])
    view_secret_data(['Bob', 'manager'])
