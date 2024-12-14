# Вводим три числа
first = int(input())
second = int(input())
third = int(input())

# Вводим условия
if first == second == third:
    print(3)  # Если все числа равны, то выводим 3
elif first == second or first == third or second == third:
    print(2)  # Если хотя бы 2 равны, то выводим 2
else:
    print(0)  # Если равных чисел нет, то выводим 0