from pathlib import Path


PATH_DIR = Path(__file__).parent.parent


def log(filename):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                if filename:
                    path_to_file = Path(PATH_DIR, "logs", filename)
                    with open(path_to_file, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} OK\n")
                else:
                    print(f"{func.__name__} OK\n")
                return res
            except Exception as e:
                if filename:
                    path_to_file = Path(PATH_DIR, "logs", filename)
                    with open(path_to_file, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs {args}, {kwargs} \n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs {args}, {kwargs} \n")
        return inner
    return wrapper
