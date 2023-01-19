from libs import lib
import pytest

class TestFib:

    # Тестируем программу на корректных данных. Функция возвращает список элементов.
    def test_1(self):
        assert lib.fib(7) == [1, 1, 2, 3, 5, 8, 13]

    # Тестируем программу на некоррктных данных. Функция возвращает пустой список [].
    def test_2(self):
        # Когда мы подаем на вход программе число 0 или отрицательное - программа должна вернуть пустой список.
        assert lib.fib(0) == []