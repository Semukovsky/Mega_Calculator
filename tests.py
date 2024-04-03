import unittest

from main import calc


class TestCalculator(unittest.TestCase):
    def test_plus(self):
        result_of_func = calc("пять плюс четыре")
        expected_value = "девять"
        self.assertEquals(result_of_func, expected_value)

    def test_decimal_plus_1(self):
        result_of_func = calc("пять и три сотых плюс четыре")
        expected_value = "девять и три сотых"
        self.assertEquals(result_of_func, expected_value)

    def test_decimal_plus_2(self):
        result_of_func = calc("пять и три сотых плюс четыре и пять сотых")
        expected_value = "девять и восемь сотых"
        self.assertEquals(result_of_func, expected_value)

    def test_minus(self):
        result_of_func = calc("пять минус четыре")
        expected_value = "один"
        self.assertEquals(result_of_func, expected_value)

    def test_multiplication(self):
        result_of_func = calc("пять умножить четыре")
        expected_value = "двадцать"
        self.assertEquals(result_of_func, expected_value)

    def test_devision(self):
        result_of_func = calc("пять разделить на один")
        expected_value = "пять и ноль десятых"
        self.assertEquals(result_of_func, expected_value)

    def test_prochent(self):
        result_of_func = calc("пять процент на два")
        expected_value = "один"
        self.assertEquals(result_of_func, expected_value)

    def test_not_operation(self):
        result_of_func = calc("пять - четыре")
        expected_value = "[x] Отсутствует операция. Попробуй еще раз...\n"
        self.assertEquals(result_of_func, expected_value)

    def test_failed_in_calc(self):
        result_of_func = calc("пять умножить -")
        expected_value = "[x] Ошибка в числе. Попробуй еще раз...\n"
        self.assertEquals(result_of_func, expected_value)

    def test_empty_in_calc(self):
        result_of_func = calc("")
        expected_value = "[x] Отсутствует выражение. Попробуй еще раз...\n"
        self.assertEquals(result_of_func, expected_value)

    def test_zero_devision(self):
        result_of_func = calc("пять разделить на ноль")
        expected_value = "[x] Деление на ноль. Попробуй еще раз...\n"
        self.assertEquals(result_of_func, expected_value)

    def test_zero_prochent(self):
        result_of_func = calc("пять процент на ноль")
        expected_value = "[x] Деление на ноль. Попробуй еще раз...\n"
        self.assertEquals(result_of_func, expected_value)

    def test_decimal(self):
        result_of_func = calc("сорок один и тридцать одна сотая разделить на семнадцать")
        expected_value = "два и сорок три сотых"
        self.assertEquals(result_of_func, expected_value)

    def test_first_minus(self):
        result_of_func = calc("минус пять плюс пять")
        expected_value = "ноль"
        self.assertEquals(result_of_func, expected_value)

    def test_first_second_minus(self):
        result_of_func = calc("минус пять минус пять")
        expected_value = "минус десять"
        self.assertEquals(result_of_func, expected_value)

    def test_first_second_third_minus(self):
        result_of_func = calc("минус пять минус минус пять")
        expected_value = "ноль"
        self.assertEquals(result_of_func, expected_value)

    def razmeshenie(self):
        result_of_func = calc("размещение из трех по два")
        expected_value = "шесть и ноль десятых"
        self.assertEquals(result_of_func, expected_value)

    def sochetanie(self):
        result_of_func = calc("сочетание из трех по два")
        expected_value = "три и ноль десятых"
        self.assertEquals(result_of_func, expected_value)

    def perestanovka(self):
        result_of_func = calc("перестановка по трех")
        expected_value = "шесть"
        self.assertEquals(result_of_func, expected_value)


if __name__ == "__main__":
    unittest.main()
