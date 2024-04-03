from func_replace import string_to_number, number_to_string
from func_pymorphy import get_normal_form
from combinators import razmeshenie, sochetanie, perestanovka

operations = {  # операции
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "разделить": "/",
    "процент": "%",
    "размещение": razmeshenie,
    "сочетание": sochetanie,
    "перестановка": perestanovka,
}
dct_places = {  # основы для десят. дробей
    "десятый": 10,
    "сотый": 100,
    "тысячная": 1000,
}


def get_res(number_1: int, operation: str, number_2: int = None) -> int:  # принимает числа и операцию
    if operation in ["размещение", "сочетание"]:  # если операция размещ. или сочет.
        res_of_expression = operations[operation](number_1, number_2)
    elif operation == "перестановка":  # если переставнока
        res_of_expression = operations[operation](number_1)
    else:  # иначе это обычная матем. операция
        expression = f"{number_1}{operations[operation]}{number_2}"
        res_of_expression = eval(expression)
    return round(res_of_expression, 3)  # округляет и возвращает


def calc(string: str) -> str:  # сама функция
    lst = [get_normal_form(word) for word in string.lower().split()]  # приводим выраж в нижний и разбиваем по словам в НФ
    if not lst:  # если нет выражен
        return "[x] Отсутствует выражение. Попробуй еще раз...\n"
    if lst[0] in ["размещение", "сочетание"]:  # если на первом место стоит размещ | сочетани
        operation = lst[0]
        lst = lst[2:]
        index = lst.index("по")
        first_number = lst[:index]
        second_number = lst[index + 1:]
    elif lst[0] == "перестановка":  # если перестановка
        operation = lst[0]
        index = lst.index("по")
        lst = lst[2:]
        first_number = lst[:index]
        first_number = string_to_number(first_number)
        result = get_res(first_number, operation)  # тк перестановка считается только по одному числу, то здесь мы сразу возваращет ответ
        return number_to_string(result)  # приводим к строке и возвращ
    else:
        operation = [i for i in lst if i in operations]  # идем по операциям и находим какие стоят у нас
        l = len(operation)  # смотрим сколько их
        if l == 0:
            return '[x] Отсутствует операция. Попробуй еще раз...\n'
        elif l == 1:  # если одна, то все нормально, идем считать
            operation = operation[0]
            index = lst.index(operation)
            first_number = lst[:index]
            second_number = lst[index + 1:]
        elif l == 2:  # если две, то где есть минус
            if lst[0] == 'минус':  # проверяем что у первго стоит минус
                operation = operation[1]
                index = lst[1:].index(operation)
                first_number = lst[:index + 1]
                second_number = lst[index + 2:]
            else:  # проверяем что у второго стоит минус
                operation = operation[0]
                index = lst.index(operation)
                first_number = lst[:index]
                second_number = lst[index + 1:]
        elif l == 3:  # если 3 операции, значит и в начале и у второго числа стоит минус
            operation = operation[1]
            index = lst[1:].index(operation)
            first_number = lst[:index + 1]
            second_number = lst[index + 2:]
        else:  # значит что то напутали с операциями
            return '[x] Предел операций. Попробуй еще раз...\n'
    try:
        if second_number[0] == 'на':
            second_number = second_number[1:]

        if "и" in first_number:  # проверяет что первое число дробное
            index_of_and = first_number.index("и")
            integer, decimal = first_number[:index_of_and], first_number[index_of_and + 1:]
            integer = string_to_number(integer)
            decimal_place = dct_places.get(decimal[-1])
            decimal = string_to_number(decimal[:-1])
            decimal = decimal / decimal_place
            first_number = integer + decimal  # преобразует число
        else:  # если целое
            first_number = string_to_number(first_number)
        if "и" in second_number:  # проверяет что второе число дробное
            index_of_and = second_number.index("и")
            integer, decimal = second_number[:index_of_and], second_number[index_of_and + 1:]
            integer = string_to_number(integer)
            decimal_place = dct_places.get(decimal[-1])
            decimal = string_to_number(decimal[:-1])
            decimal = decimal / decimal_place
            second_number = integer + decimal  # преобразует число
        else:  # если целое
            second_number = string_to_number(second_number)
        result = get_res(first_number, operation, second_number)  # считается результат
        # print(f"[x] {first_number=}, {second_number=}, {result=}")
        result = number_to_string(result)  # преобразуется в строку
        return result  # возвращается
    except ZeroDivisionError:
        return '[x] Деление на ноль. Попробуй еще раз...\n'
    except TypeError:
        return "[x] Ошибка в числе. Попробуй еще раз...\n"
    except Exception as e:
        print(e)
        return '[x] Попробуй еще раз...\n'


result_of_func = calc("девятнадцать и восемьдесят две сотых разделить на девяносто девять")
print(result_of_func)
