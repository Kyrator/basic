# TODO здесь писать код
import random


class Fighter:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.health = 100

# TODO: методы класса должны быть в классе; например, дать в нос, все еще жив
# внешний код должен организовать "битву"
    def hit(self, fighter):
        fighter.health -= 20
        print(f"Ударил {self.name}, {fighter.name} потерял 20 ед. здоровья.")
        print(f" У {self.name}а осталось {self.health}. У {fighter.name}а осталось {fighter.health}.\n")


fighter_1 = Fighter("Васян", 1)
fighter_2 = Fighter("Колян", 2)
fight = [fighter_1, fighter_2]

while True:
    if fighter_1.health * fighter_2.health:
        choose_warrior = random.randint(0, 1)
        if choose_warrior:
            fighter_1.hit(fighter_2)
        else:
            fighter_2.hit(fighter_1)
    else:
        win = fighter_1.name if fighter_1.health > 0 else fighter_2.name
        print("Битва закончилась. Победил {} ".format(win))
        break


