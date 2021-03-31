# translation from google.

# This code contains up to 80 characters per line.
# This code does not exceed 10 lines per function.

# This is a student template:
class Student:
    list_number = []  # Student grades. an array of 4 ratings
    # (in the range 0 - 5).
    first_name = ""  # Surname and initials.
    number_group = 0  # Student group number.


    def __init__(self, number_group, first_name, list_number):
        self.number_group = int(number_group)
        self.first_name = first_name
        
        array = []
        for i in list_number:
            i = int(i)
            i = 5 if i > 5 else i
            i = 0 if i < 0 else i
            array.append(i)

        self.list_number = array


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
def GPA(student: Student) -> float:

    total = 0  # sum. Python already has a sum function!
    length = len(student.list_number)

    for j in range(length):
        total += student.list_number[j]

    return total / length


# I create an array of students:
def get_students() -> list:
    array = []

    for l in get_data():
        array.append(Student(l[0], l[1], [l[2], l[3], l[4], l[5]]))

    return array


# I display an array of students:
def echo_students(array: list) -> None:
    for i in array:
        print(i.number_group, i.first_name, i.list_number, GPA(i))


# Is this student an excellent student?
def has_excellent_grades(student: Student) -> bool:
    excellent_grades = 4,5
    
    for number in excellent_grades:
        if number in student.list_number:
            return True
    return False


# I display excellent students on the screen:
def echo_best_students(array: list) -> None:
    flag = True  # I will say that I have not found a better student.

    for i in array:
        if has_excellent_grades(i):
            echo_students([i])

            flag = False  # I will say that I have found the best student.

    if flag:
        print("there are no such students")


# I sort students by grade point average:
def sort_students(array: list) -> list:
    flag = True

    # I sort until the array is sorted:
    while flag:
        # I will say that the array is already sorted:
        flag = False

        length = len(array)

        # Sort by bubble method:
        for j in range(length):
            if j + 1 < length and GPA(array[j]) > GPA(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

                # I will say that the array is still sorted:
                flag = True

    return array
