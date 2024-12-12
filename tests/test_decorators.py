from src.decorators import log


def test_log(capsys):
    @log(filename=None)
    def my_func(x, y):
        return x + y
    my_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_func OK\n\n"


def test_log_err(capsys):
    @log(filename=None)
    def my_func(x, y):
        return x + y
    my_func("1", 2)
    captured = capsys.readouterr()
    assert captured.out == "my_func error: can only concatenate str (not \"int\") to str. Inputs ('1', 2), {} \n\n"


def test_log_positive():
    @log(filename="my_log")
    def my_func(x, y):
        return x + y
    captured = my_func(1, 2)
    assert captured == 3
