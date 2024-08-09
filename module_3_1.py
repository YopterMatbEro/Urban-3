def count_calls():
    global calls
    calls += 1
    return


def string_info(string='Тестовая строка'):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string: str, list_: list):
    count_calls()
    return True if string.lower() in [word.lower() for word in list_] else False


calls = 0
list_to_search = ['TEst', 'теСт', 'ТЕСТОвая стрОКА', 'тестОваЯ', 'сТрОКа', 'теСТОвая сТрОЧКА', 'стРОчКа', 'teST stRING',
                  'StrING', 'Str']

info = string_info('Параллелепипед')
print(info)
info = string_info('Ретроспектива')
print(info, '\n')

contain = is_contains('TesT', list_to_search)
print(contain)
contain = is_contains('ТЕСТОВАЯ СТРОКА', list_to_search)
print(contain)
contain = is_contains('ТеСтостерон', list_to_search)
print(contain, '\n')

print(calls)
