# TODO здесь писать код
import random


class Human:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.satiety = 50
        self.live = True

    def feed(self, step):
        self.satiety += step
        self.home.fridge -= step

    def earn(self, step):
        self.satiety -= step
        self.home.bedside_table += step

    def play(self, step):
        self.satiety -= step

    def shopping(self, step):
        self.home.fridge += step
        self.home.bedside_table -= step

    def check(self):
        if self.satiety < 0:
            self.live = False

    def algoritm_human(self):
        cubic = random.randint(1, 6)
        if self.satiety < 20:
            self.feed(cubic)
            # print("feed")
        elif self.home.fridge < 10:
            self.shopping(cubic)
            # print("shopping")
        elif self.home.bedside_table < 50 or cubic == 1:
            self.earn(cubic)
            # print("earn")
        elif cubic == 2:
            self.feed(cubic)
            # print("feed")
        else:
            self.play(cubic)
            # print("play")
        self.check()
        print("Проживающий {}, сытость = {} ".format(self.name, self.satiety))


class Home:
    def __init__(self, name):
        self.name = name
        self.bedside_table = 0
        self.fridge = 50


day = 1

home_couple_home = Home("couple_home")
human_Sergey = Human("Sergey", home_couple_home)
human_Kate = Human("Kate", home_couple_home)

# family_single = Home("single_home")
# human_Andrey = Human("Andrey", family_single)


while day < 366:
    if human_Sergey.live or human_Kate.live:
        print("День {}".format(day))
        if human_Kate.live:
            human_Kate.algoritm_human()
        if human_Sergey.live:
            human_Sergey.algoritm_human()
        print()
        day += 1
    else:
        break
