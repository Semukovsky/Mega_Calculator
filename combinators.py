from math import factorial


def razmeshenie(n, k):
    return factorial(n) / factorial(n - k)


def sochetanie(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def perestanovka(n):
    return factorial(n)
