# Zapisz każdą z poniższych funkcji w postaci list/dict/set 
# comprehension. Nie należy używać żadnych zmiennych tymczasowych
# ani dodatkowych linii, każda funkcja ma zostać wyrażona
# w postaci:

# def FUNKCJA(ARGUMENTY):
#     return COMPREHENSION

def even_numbers_from_list(data):
    """Zwraca podlistę "data" zawierającą wyłącznie parzyste liczby"""
    result = []
    for point in data:
        if point % 2 == 0:
            result.append(point)
    return result


def words_analyze(words):
    """Zwraca listę trójek, gdzie i'ta trójka to (i, i'te słowo, długość i'tego słowa)"""
    result = []
    i = 0
    for word in words:
        result.append((i, word, len(word)))
        i += 1
    return result


def count_words_starting_with_given_letter(text, letter):
    """Zwraca słownik gdzie kluczami są wszystkie słowa występujące w tekście 
    rozpoczynające się na zadaną literę, a wartością ile razy wystąpiy"""
    result = {}
    for word in text.split():
        if word[0] == letter:
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1
    return result


def comprehensions_even_numbers_from_list():
    pass


def comprehensions_words_analyze():
    pass


def comprehensions_count_words_starting_with_given_letter():
    pass