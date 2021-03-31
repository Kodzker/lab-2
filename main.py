# translation from google.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# The code was written by Timofey Bochkor, Einstein and others...

if __name__ != '__main__':
    print("This is a program, not a library!")
    exit()

from library import *

print('')

array = get_students()  # получить массив студентов.
#echo_students(array)
print('')

array = sort_students(array)  # сортировка массива студентов
echo_students(array)
print('')

print('best:')
echo_best_students(array)  # вывод учиников у которых есть 4 и 5.
