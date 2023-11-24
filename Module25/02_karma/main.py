# TODO здесь писать код
import random


class Life:
    def __init__(self, name):
        self.day = 0
        self.name = name
        self.exeptions_karma = [
            "KillError",
            "DrunkError",
            "CarCrashError",
            "GluttonyError",
            "DepressionError"
        ]
        self.karma = 0

    @property
    def one_day(self) -> str:
        self.day += 1
        try:
            if random.randint(1, 10) != 10:
                to_day_karma = random.randint(1, 7)
                self.karma += to_day_karma
                return f"{man.name} earned {to_day_karma} score karma\n"
            raise ValueError
        except ValueError:
            karma_error = random.choice(self.exeptions_karma)
            with open("karma.log", "a") as karma:
                karma.write(karma_error + "\n")
            return f"{man.name} earned {karma_error} \n"


man = Life(name="Egor")

while True:
    print(f"To day is {man.day}")
    print(man.one_day)
    if man.karma >= 500:
        print(f"{man.name} earned {man.karma} ")
        break
