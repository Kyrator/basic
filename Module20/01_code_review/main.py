students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# TODO исправить код

def find_interest(students_dict):
  interest_list_find = set()
  surname_string_find = ''
  for student in students_dict.values():
    interest_list_find.update(student['interests'])
    surname_string_find += student['surname']
  length_surname_find = len(surname_string_find)

  return interest_list_find, length_surname_find


print("Список пар «ID студента — возраст»:", [(id, student['age']) for id, student in students.items()])

interest_list, length_surname = find_interest(students)

print("Полный список интересов всех студентов:",interest_list)

print("Общая длина всех фамилий студентов:", length_surname)
