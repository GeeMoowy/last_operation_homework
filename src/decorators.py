from pathlib import Path

PATH_DIR = Path(__file__).parent.parent


def log(filename=None):
    """Внешняя функция, которая принимает аргумент filename для декоратора, для создания log-файла"""

    def wrapper(func):
        """Декоратор, принимает функцию для декорирования"""

        def inner(*args, **kwargs):
            """Функция обертка, которая принимает аргументы декорируемой функции"""
            try:
                res = func(*args, **kwargs)
                if filename:  # Проверка на наличие атрибута у filename
                    path_to_file = Path(PATH_DIR, "logs", filename)
                    with open(path_to_file, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} OK\n")  # Записываем данные в файл
                else:
                    print(f"{func.__name__} OK\n")  # Выводим данные в консоль
                return res
            except Exception as e:
                if filename:  # Проверка на наличие атрибута у filename
                    path_to_file = Path(PATH_DIR, "logs", filename)
                    with open(path_to_file, "a", encoding="utf-8") as file:
                        file.write(
                            f"{func.__name__} error: {e}. Inputs {args}, {kwargs} \n"
                        )  # Записываем данные в файл
                else:
                    print(f"{func.__name__} error: {e}. Inputs {args}, {kwargs} \n")  # Выводим данные в консоль

        return inner

    return wrapper
