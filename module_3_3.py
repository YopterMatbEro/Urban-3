def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1 часть
print_params()
print_params(2)

print_params(2, 'другая строка')
print_params(b='новая строка')
print_params(b='новая строка', c=False)
print_params(4, b='новая строка', c=False)

print_params(24, 222, 333)

print_params(b=25)
print_params(c=[1, 2, 3])
print()

# 2 часть
values_list = [0, 'string', [1, True]]
values_dict = {'a': 0, 'b': 'string', 'c': [1, True]}

print_params(*values_list)
print_params(**values_dict)
print()

# 3 часть
values_list_2 = [15, True]

print_params(*values_list_2, 42)
try:
    print_params(*values_list_2, b='новая строка', c=False)
except Exception as e:
    print(e)
