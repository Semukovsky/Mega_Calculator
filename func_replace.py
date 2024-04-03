from func_pymorphy import get_accs


def string_to_number(lst_with_words: list[str]) -> int | None:
    """Строка в число"""
    dct = {
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8,
        "девять": 9,
        "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
        "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20, "тридцать": 30,
        "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
        "сто": 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот": 600, "семьсот": 700,
        "восемьсот": 800, "девятьсот": 900
    }
    current_value = 0
    if lst_with_words[0] == 'минус':
        lst_with_words = lst_with_words[1:]
        flag = True
    else:
        flag = False
    for word in lst_with_words:
        value = dct.get(word, None)
        if value is None:
            print("Некорректное слово в числе:", word)
            return

        if value >= 100:
            if current_value == 0:
                current_value = value
            else:
                current_value *= value
        else:
            current_value += value

    return int(current_value) if not flag else -int(current_value)


def int_number_to_string(number: int) -> str:
    r_1 = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    r_2 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
           'семнадцать', 'восемнадцать', 'девятнадцать']
    r_3 = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    r_4 = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    if '-' in str(number):
        number = abs(number)
        flag = True
    else:
        flag = False
    if number == 0:
        res = 'ноль'
    elif 10 <= number % 100 <= 19:
        res = f"{r_4[number // 100]} {r_2[number % 10]}"
    else:
        res = f"{r_4[number // 100]} {r_3[(number // 10) % 10]} {r_1[number % 10]}"
    if flag:
        return 'минус ' + ' '.join(res.split())
    return ' '.join(res.split())


def number_to_string(number: float) -> str:
    """Число в строку"""
    decimal_places = {
        1: "десятых",
        2: "сотых",
        3: "тысячные",
    }
    if '.' in str(number):
        integer, decimal = str(number).split('.')
        l = len(decimal)
        integer, decimal = int(integer), int(decimal)
        integer = int_number_to_string(integer)
        decimal = int_number_to_string(decimal)
        res = f"{integer} и {decimal} {decimal_places[l]}"
        return res
    else:
        return int_number_to_string(int(number))
