class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять
        # стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):

    def __init__(self, name):
        super().__init__(name)

        """магическая сила - равна значению НАЧАЛЬНОГО 
        показателя силы умноженному на 3 (self.__power * 3)"""

        self.__magic = (self.get_power() * 3)

    def attack(self, target):
        """Может атаковать врага, но атакует
        только в половину силы self.__power"""
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):
        """Он получает на 20% больше урона
        (1.2 * damage)"""
        self.set_hp(self.get_hp() - (1.2 * damage))
        super().take_damage(damage)

    def give_a_health(self, target):
        """Исцеление - увеличивает здоровье цели на
        величину равную своей магической силе"""
        target.set_hp(target.get_hp() + self.__magic)

    def make_a_move(self, friends, enemies):
        """    - выбор действия - получает на вход всех
                союзников и всех врагов и на основе своей стратегии
                выполняет ОДНО из действий (атака,
                исцеление) на выбранную им цель
        """
        print(self.name, end=' ')
        target_of_health = friends[0]
        min_health = target_of_health.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_health = friend
                min_health = target_of_health.get_hp()

        if min_health < 240:
            self.give_a_health(target_of_health)
            print("Исцеляю", target_of_health.name, "на", self.get_power())

        else:
            if not enemies:
                return
            enemy = 0
            target_of_attack = enemies[0]
            min_health = target_of_attack.get_hp()
            for i_enemy in range(len(enemies)):
                if 0 < enemies[i_enemy].get_hp() < min_health:
                    enemy = i_enemy
                    min_health = target_of_attack.get_hp()
            print("Атакую ближнего -", enemies[enemy].name)
            self.attack(enemies[enemy])
        print('\n')
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return ('Name: {0} | HP: {1} | isLife {2} | Power {3}'
                .format(self.name, self.get_hp(), self.is_alive(), self.get_power()))


class Tank(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.is_shield = False

    def attack(self, target):
        """Атака - атакует, но т.к. доспехи очень
        тяжелые - наносит половину урона (self.__power)
        """
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):
        """Получение урона - весь входящий урон делится
        на показатель защиты (damage/self.defense) и
        только потом отнимается от здоровья
        """
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)

    def up_shield(self):
        """Поднять щит - если щит не поднят -
        поднимает щит. Это увеличивает показатель
        брони в 2 раза, но уменьшает показатель
        силы в 2 раза."""
        self.defense *= 2

    def down_shield(self):
        """Опустить щит - если щит поднят - опускает
        щит. Это уменьшает показатель брони в 2 раза,
        но увеличивает показатель силы в 2 раза
        """
        self.defense /= 2

    def make_a_move(self, friends, enemies):

        """Выбор действия - получает на вход всех
        союзников и всех врагов и на основе своей
        стратегии выполняет ОДНО из действий (атака,
        поднять щит/опустить щит) на выбранную им цель
        """

        print(self.name, end=' ')
        if self.get_hp() < 150 and not self.is_shield:
            print("Подымаю щит")
            self.up_shield()
        elif self.get_hp() > 340 and self.is_shield:
            print("Опускаю щит")
            self.down_shield()
        else:
            if not enemies:
                return
            enemy = 0
            target_of_attack = enemies[0]
            min_health = target_of_attack.get_hp()
            for i_enemy in range(len(enemies)):
                if 0 < enemies[i_enemy].get_hp() < min_health:
                    enemy = i_enemy
                    min_health = target_of_attack.get_hp()
            print("Атакую ближнего -", enemies[enemy].name)
            self.attack(enemies[enemy])
        print('\n')
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return ('Name: {0} | HP: {1} | isLife {2} | Power {3} | Defence {4}'
                .format(self.name, self.get_hp(), self.is_alive(), self.get_power(), self.defense))


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        """Атака - наносит урон равный
        показателю силы (self.__power)
        умноженному на коэффициент усиления урона
        (self.power_multiply)
        """
        target.take_damage(self.get_power() * self.power_multiply)
        # self.power_down()

    def power_down(self):
        """После нанесения урона -
        вызывается метод ослабления power_down."""
        # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
        self.power_multiply /= 2

    def power_up(self):
        """Усиление (power_up) - увеличивает
        коэффициента усиления урона в 2 раза"""
        self.power_multiply *= 2

    def take_damage(self, damage):
        """Получение урона - получает урон равный
        входящему урона умноженному на половину
        коэффициента усиления урона - damage *
        (self.power_multiply / 2)
        """
        self.set_hp(self.get_hp() - (damage * (self.get_power() * (self.power_multiply / 2))))
        super().take_damage(damage)

    def make_a_move(self, friends, enemies):

        """Выбор действия - получает на вход всех
        союзников и всех врагов и на основе своей
        стратегии выполняет ОДНО из действий (атака,
        усиление, ослабление) на выбранную им цель
        """

        print(self.name, end=' ')
        if self.get_hp() < 140 and self.power_multiply < self.get_power()/2:
            self.power_up()
            print("Повышаю атаку -", self.power_multiply)
        # elif self.get_hp() < 140 and self.power_multiply > 0.5:
        #     self.power_down()
        #     print("Повышаю атаку -", self.power_multiply)
        else:
            if not enemies:
                return
            enemy = 0
            target_of_attack = enemies[0]
            max_power = target_of_attack.get_power()
            for i_enemy in range(len(enemies)):
                if enemies[i_enemy].get_power() < max_power and enemies[i_enemy].get_hp() > 0:
                    enemy = i_enemy
                    max_power = target_of_attack.get_power()
                else:
                    enemy = 0
            print("Атакую ближнего -", enemies[enemy].name)
            self.attack(enemies[enemy])
            self.power_down()

        print('\n')
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return ('Name: {0} | HP: {1} | isLife {2} | Power {3} | Multy {4}'
                .format(self.name, self.get_hp(), self.is_alive(), self.get_power(), self.power_multiply))









