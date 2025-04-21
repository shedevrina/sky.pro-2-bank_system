from functools import wraps
from typing import Union


def log(filename=0):
    """Декоратор, Если filename задан, логи записываются в указанный файл. Если filename не задан, логи выводятся в консоль.
Вывод -> my_function ok
Вывод -> my_function error: тип ошибки. Inputs: (1, 2), {}

Логирование должно включать:
Имя функции и результат выполнения при успешной операции.
Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
"""
    if not isinstance(filename, Union[int, str]):
        print("Указано не верное имя файла")
        raise TypeError("Ошибка данных")
    else:
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if filename:
                    try:
                        result = func(*args, **kwargs)
                        with open(filename, 'a') as file:
                            file.write(f'{func.__name__}: {result}\n')
                            file.close()

                    except Exception as e:
                        with open(filename, 'a') as file:
                            file.write(f'{func.__name__} error: Inputs: arguments {args}.\n')
                            file.close()
                        raise ValueError("Данные не складываются")
                else:
                    try:
                        result = func(*args, **kwargs)
                        print("my_function ok")

                    except Exception as e:
                        print(f'{func.__name__} error: Inputs: {tuple(x for x in args)}')
                        raise ValueError("Данные не складываются")
                    return result

            return wrapper
        return decorator

