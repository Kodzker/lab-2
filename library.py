# translation from google.

class Student:
    first_name = ""  # Прізвище і ініціали.
    number_group = 0  # Номер групи.
    list_number = []  # 4 Успішність. оцінка якої нема я так поняв.

    def __init__(self, number_group, first_name, list_number):
        self.list_number = list_number
        self.number_group = number_group
        self.first_name = first_name


def get_data(link: str = "data_in.txt") -> list:
    # получаю массив элементов из базы:
    with open(link) as f:
        read_data = f.read().replace(' ', '-').replace('\n', ' ').split()

    # print(read_data)

    # создаю массив слов из массива элементов:
    array = []

    for i in read_data:
        array.append(i.replace('-', ' ').split())

    # print(array)

    return array


def seredhiy_bal(student: Student) -> float:
    sum = 0
    length = len(student.list_number)

    for j in range(length):
        sum += student.list_number[j]

    return sum / length


def get_students() -> list:
    array = []

    for i in get_data():
        array.append(Student(int(i[0]), i[1], [int(i[2]), int(i[3]), int(i[4]),
            int(i[5])]))

    return array


def echo_students(array: list) -> None:
    for i in array:
        print(i.number_group, i.first_name, i.list_number, seredhiy_bal(i))


def echo_best_students(array: list) -> list:
    flag = True  # I will say that I have not found a better student. - translation from google.

    for i in array:
        if 4 in i.list_number or 5 in i.list_number:
            echo_students([i])

            flag = False  # I will say that I have found the best student. - translation from google.

    if flag:
        print("there are no such students")  # - translation from google.


def sort_students(array: list) -> list:
    flag = True

    while flag:
        flag = False

        length = len(array)

        for i in range(length):
            if i + 1 < length and seredhiy_bal(array[i]) > seredhiy_bal(array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]

                flag = True

    return array
