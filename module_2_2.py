# module_2_2.py Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = input('Введите число:')
second = input('Введите еще одно число:')
third = input('Введите еще одно число:')
if first == second == third:
    print('3')
elif first == second:
    print('2')
elif first == third:
    print('2')
elif second == third:
    print('2')
else:
    print("0")
