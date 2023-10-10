# Zapisz poniższą funkcję w postaci list/dict/set 
# comprehension. Nie należy używać żadnych zmiennych tymczasowych
# ani dodatkowych linii, każda funkcja ma zostać wyrażona
# w postaci:

# def FUNKCJA(ARGUMENTY):
#     return COMPREHENSION

def comprehensions_merge_dicts(a, b, f):
    '''
    Funkcja przyjmuje:
    - dwa słowniki a i b
    - dwuargumentową funkcję f
    Funkcja jako wynik powinna zwrócić słownik, który będzie sumą dwóch słowników.
    Sumę dwóch słowników powinniśmy rozumieć jako słownik, w którym zbiór kluczy będzie równy
    sumie zbiorów kluczy ze słowników a i b. Gdy jakiś klucz występuje w obu słownikach, to wartość ma być
    wynikiem funkcji f obliczonej na wartościach dla danego klucza w słowniku a i słowniku b
    '''
    pass


def add(a,b):
    return a + b