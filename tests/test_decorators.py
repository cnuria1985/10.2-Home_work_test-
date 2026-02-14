
import pytest
from src.decorators import log


# тест на вывод сообщения об успешном выполнении функции в виртуальный файл

def test_log_file_ok(tmp_path):
    file = tmp_path / "mylog.txt"
    @log(filename=file)
    def func(a, b):
        return a + b

    func(1, 2)

    with open(file, encoding="utf-8") as f:
        assert f.read() == "func ok\n"


# тест на вывод сообщения при ошибке в виртуальный файл

def test_log_file_error(tmp_path):
    file = tmp_path / "mylog.txt"
    @log(filename=file)
    def func(a, b):
        return a + b

    func('1', 2)

    with open(file, encoding="utf-8") as f:
        assert f.read() == "func error: can only concatenate str (not \"int\") to str. Inputs: ('1', 2) {}\n"


# тест на вывод сообщения при ошибке с использованием capsys

def test_log_error(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function('1', 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: can only concatenate str (not \"int\") to str. Inputs: ('1', 2) {}\n"


# тест на вывод сообщения при успешном выполнении функции

def test_log_ok(capsys):
    @log()
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


# тест на вывод сообщения об успешном выполнении функции в файл

def test_log_file_is_ok():
    @log(filename="mylog.txt")
    def func(a, b):
        return a + b

    func(1, 2)

    with open("mylog.txt", encoding="utf-8") as f:
        assert f.read() == "func ok\n"
