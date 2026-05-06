# premiere ligne
def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b


def est_pair(n):
    return n % 2 == 0


def factorielle(n):
    if n < 0:
        raise ValueError("n doit etre positif")
    if n == 0:
        return 1
    return n * factorielle(n - 1)


def inverser_chaine(s):
    return s[::-1]


def est_palindrome(s):
    return s == s[::-1]


def maximum(liste):
    if not liste:
        raise ValueError("Liste vide")
    return max(liste)


def compter_voyelles(s):
    return sum(1 for c in s.lower() if c in "aeiou")
