# module_2_2.py Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = input('Введите число:')
second = input('Введите еще одно число:')
third = input('Введите еще одно число:')
if first == second == third:
    a = '3'
elif first == second:
    a = '2'
elif first == third:
    a = '2'
elif second == third:
    a = '2'
else:
    a = '0'
print(f'Kоличество равных: {a}')
