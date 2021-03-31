# translation from google.

# This is a student template:
class Student:
    first_name = ""  # Surname and initials.

    number_group = 0  # Student group number.

    list_number = []  # Student grades. an array of 4 ratings
    # (in the range 0 - 5).

    def __init__(self, number_group, first_name, list_number):
        self.number_group = int(number_group)

        array = []
        for i in list_number:
            if (int(i) > 5):
                i=5
            array.append(int(i))
        self.list_number = array

        self.first_name = first_name


# I read an array of students from the database:
def get_data(link: str = "data_in.txt") -> list:

    # I get an array of elements from the database:
    with open(link) as f:
        read_data = f.read().replace(' ', ',').replace('\n', ' ').split()

    # debug:
    #print(read_data)

    # I create an array of words from an array of elements:
    array = []

    for i in read_data:
        array.append(i.replace(',', ' ').split())

    # debug:
    #print(array)

    return array


# I learn the student's average score: GPA
def average_score(student: Student) -> float:

    total = 0  # sum. Python already has a sum function!
    length = len(student.list_number)

    for j in range(length):
        total += student.list_number[j]

    return total / length


# I create an array of students:
def get_students() -> list:
    array = []

    for i in get_data():
        array.append(Student(i[0], i[1], [i[2], i[3], i[4], i[5]]))

    return array


# I display an array of students:
def echo_students(array: list) -> None:
    for i in array:
        print(i.number_group, i.first_name, i.list_number, average_score(i))


# I display excellent students on the screen:
def echo_best_students(array: list) -> list:
    flag = True  # I will say that I have not found a better student. - translation from google.

    for i in array:
        if 4 in i.list_number or 5 in i.list_number:
            echo_students([i])

            flag = False  # I will say that I have found the best student. - translation from google.

    if flag:
        print("there are no such students")  # - translation from google.


# I sort students by grade point average:
def sort_students(array: list) -> list:
    flag = True

    # I sort until the array is sorted:
    while flag:
        # I will say that the array is already sorted:
        flag = False

        length = len(array)

        # Sort by bubble method:
        for i in range(length):
            if i + 1 < length and average_score(array[i]) > average_score(array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]

                # I will say that the array is still sorted:
                flag = True

    return array
