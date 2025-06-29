try:
    raise Exception
except Exception:
    print(f'Хммм... Что-то пошло не так!')
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')

try:
    raise ValueError
except Exception:
    print(f'Хммм... Что-то пошло не так!')
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')

try:
    raise ValueError
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')
except Exception:
    print(f'Хммм... Что-то пошло не так!')

try:
    raise Exception
except ValueError as ve:
    print(f'Получено нужное исключение {type(ve).__name__}')
except Exception:
    print(f'Хммм... Что-то пошло не так!')
