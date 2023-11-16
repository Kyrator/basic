# TODO здесь писать код
import random


class Child:
    status_calm = {0: "Спокойный",
                   1: "Активный"}

    status_hungry = {0: "Не хочется",
                     1: "Хочу есть"}

    def __init__(self, name, age):
        self.name = name
        self.age_child = age
        self.status_calm = random.randint(0, 1)
        self.status_hungry = random.randint(0, 1)

    def get_status_calm(self):
        return Child.status_calm[self.status_calm]

    @property
    def get_status_hungry(self):
        return Child.status_hungry[self.status_hungry]

    def set_status_calm(self):
        self.status_calm = 0

    def set_status_hungry(self):
        self.status_hungry = 0


class Parent:

    def __init__(self, name: str, age: int, list_child: list):
        self.i_child = None
        self.name = name
        self.age = age
        self.list_child = []
        for name, age in list_child:
            try:
                if age + 16 < self.age:
                    self.list_child.append(Child(name, age))
                else:
                    raise ValueError
            except ValueError:
                print("{} не может быть Вашим ребенком. Отнесите туда откуда его взяли.\n".format(name))

    def print_info(self):
        print("Я {} мне {} лет.".format(self.name, self.age))
        print("У меня есть дети: ")
        for i_child in self.list_child:
            print("\t{} \t\t{} \t\t{} \t\t\t\t{}"
                  .format(i_child.name, i_child.age_child,
                          i_child.get_status_calm(), i_child.get_status_hungry))
        print()

    def calm_child(self):
        for i_child in self.list_child:
            if i_child.get_status_calm() == "Активный":
                i_child.set_status_calm()
                print("{} успокоен".format(i_child.name))

    def feed_child(self):
        for i_child in self.list_child:
            if i_child.get_status_hungry == "Хочу есть":
                i_child.set_status_hungry()
                print("{} покормлен".format(i_child.name))


families = (
    ("Homer Simpson", 35, (("Liza Simpson", 11), ("Barth Simpson", 12), ("Meggy Simpson", 2), ("Capitan Amerika", 89))),
    ("Peter Griffin", 32, (("Meg Griffin", 15), ("Chris Griffin", 12), ("Stewie Griffin", 5))))

families_list = [Parent(name, age, children) for name, age, children in families]

for i_family in families_list:
    i_family.print_info()
    print()

for i_family in families_list:
    i_family.calm_child()
    print()

for i_family in families_list:
    i_family.feed_child()
    print()

for i_family in families_list:
    i_family.print_info()
    print()
