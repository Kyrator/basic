# TODO здесь писать код
list_student = [["Иванов Иван", "ВТБИ-01-17", 1, 2, 3, 4, 3],
                ["Квасов Михаил", "МИПИ-01-17", 1, 4, 3, 4, 3],
                ["Березкин Роман", "ВТББ-02-18", 2, 3, 3, 4, 2],
                ["Зернов Олег", "ИМНО-01-17", 3, 4, 3, 4, 3],
                ["Хотин Леонид", "ВТБИ-01-17", 3, 4, 3, 1, 3],
                ["Куренев Иван", "ИМНО-02-18", 4, 4, 3, 1, 3],
                ["Сырысев Александр", "ВТБB-01-17", 2, 4, 3, 4, 3],
                ["Петров Иван", "ВТБИ-01-17", 3, 2, 3, 4, 3],
                ["Петухов Женя", "МИПИ-01-17", 3, 4, 5, 4, 3],
                ["Фролов Алексей", "ИМНО-01-17", 5, 5, 5, 5, 5]]


class Student:
    def __init__(self, surname_name: str, group_number: str, rating: list[int]):
        self.surname_name = surname_name
        self.group_number = group_number
        self.rating = rating
        self.medium = sum(self.rating) / len(self.rating)


list_student_class = [Student(i_student[0], i_student[1], i_student[2:]) for i_student in list_student]


def sort_key(s):
    return s.medium


print("+{:-^22}+{:-^12}+{:-^11}+".format('-', '-', '-'))
print("|{: ^22}|{: ^12}|{: ^9}|".format('Фамилия Имя', "Группа", "Средний бал"))
print("+{:-^22}+{:-^12}+{:-^11}+".format('-', '-', '-'))
for i_student in sorted(list_student_class, key=sort_key):
    print("|{: ^22}|{: ^12}|{: ^11}|".format(i_student.surname_name, i_student.group_number, i_student.medium))
print("+{:-^22}+{:-^12}+{:-^11}+".format('-', '-', '-'))
