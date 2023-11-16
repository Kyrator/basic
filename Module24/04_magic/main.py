# TODO здесь писать код
class Water:
    name = "Вода"

    def __add__(self, other):
        if other.name == "Воздух":
            return Storm()
        elif other.name == "Огонь":
            return Steam()
        elif other.name == "Земля":
            return Dirt()
        elif other.name == "Холод":
            return Ice()
        else:
            return None


class Air:
    name = "Воздух"

    def __add__(self, other):
        if other.name == "Огонь":
            return Light()
        elif other.name == "Земля":
            return Dust()
        else:
            return None


class Fire:
    name = "Огонь"

    def __add__(self, other):
        if other.name == "Земля":
            return Lava()
        else:
            return None


class Earth:
    name = "Земля"

    def __add__(self, other):
        if other.name == "Земля":
            return Lava()
        else:
            return None


class Cold:
    name = "Холод"

    def __add__(self, other):
        if other.name == "Земля":
            return Lava()
        else:
            return None


class Storm:
    name = "Шторм"
    answer = 'Вода + Воздух = Шторм'


class Steam:
    name = "Пар"
    answer = 'Вода + Огонь = Пар'


class Dirt:
    name = "Грязь"
    answer = 'Вода + Земля = Грязь'


class Light:
    name = "Молния"
    answer = 'Воздух + Огонь = Молния'


class Dust:
    name = "Пыль"
    answer = 'Воздух + Земля = Пыль'


class Lava:
    name = "Лава"
    answer = 'Огонь + Земля = Лава'


class Ice:
    name = "Лед"
    answer = 'Вода + Холод = Лед'


combinations = [Water(), Air(), Fire(), Earth(), Cold()]

for i_elem in combinations:
    for j_elem in combinations:
        new_elem = i_elem + j_elem
        if new_elem:
            print(new_elem.answer)
        else:
            print(new_elem)
