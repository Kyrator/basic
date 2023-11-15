# TODO здесь писать код
import random


class Fighter:
    def __init__(self, index):
        self.index = index
        self.name = "Воин {}".format(self.index)
        self.health = 100

# TODO: методы класса должны быть в классе; например, дать в нос, все еще жив
# внешний код должен организовать "битву"


class Ring:
    status_battle = True

    def __init__(self):
        self.warriors = [Fighter(index) for index in range(1, 3)]

    def battle(self):
        choose_warrior = random.randint(0, 1)
        self.warriors[(choose_warrior + 1) % 2].health -= 20
        print("Ударил {}, {} потерял 20 ед. здоровья. Осталось {}".format(
            self.warriors[choose_warrior].name,
            self.warriors[(choose_warrior + 1) % 2].name,
            self.warriors[(choose_warrior + 1) % 2].health
        ))
        self.status_battle = self.warriors[(choose_warrior + 1) % 2].health * self.warriors[
            (choose_warrior + 1) % 2].health
        if not self.status_battle:
            win = ''
            for warrior in self.warriors:
                if warrior.health != 0:
                    win = warrior.name
            print("Выйграл {} ".format(win))


fight = Ring()
while fight.status_battle:
    fight.battle()
