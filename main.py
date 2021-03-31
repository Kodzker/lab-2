# translation from google.

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi,', name)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')
else:
    exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from library import *

print('')

array = get_students()  # получить массив студентов.

# echo_students(array)

print('')

array = sort_students(array)  # сортировка массива студентов

echo_students(array)

print()

print('best:')
echo_best_students(array)  # вывод учиников у которых есть 4 и 5.
