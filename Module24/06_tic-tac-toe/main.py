# TODO здесь писать код
class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = " "


class Board:
    def __init__(self):
        self.pole = [Cell(i) for i in range(1, 10)]

    def display(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.pole[0 + i * 3].symbol,
                  "|", self.pole[1 + i * 3].symbol,
                  "|", self.pole[2 + i * 3].symbol, "|")
        print("-" * 13)

    def change_cell(self, number, symbol):
        if self.pole[number - 1].symbol == " ":
            self.pole[number - 1].symbol = symbol
            return True
        return False

    def check_win(self):
        win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for comb in win_comb:
            if self.pole[comb[0]].symbol == self.pole[comb[1]].symbol == self.pole[comb[2]].symbol:
                if player1.symbol == self.pole[comb[0]].symbol:
                    print("Победитель {} !".format(player1.name))
                    self.display()
                    return True
                elif player2.symbol == self.pole[comb[0]].symbol:
                    print("Победитель {} !".format(player2.name))
                    self.display()
                    return True
                else:
                    return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self, player_1, player_2):
        self.player1 = player_1
        self.player2 = player_2
        self.board = Board()

    def one_move_player(self):
        try:
            number_cell = int(input("Введите число от 1 до 9\n"))
            if 1 <= number_cell <= 9:
                return number_cell
            else:
                print("Нужно везти число от 1 до 9")
        except ValueError:
            print("Не правильный ввод. Попробуйте еще раз.")
            return self.one_move_player()

    def start(self, player):
        self.board.display()
        print("{} ходит.".format(player.name))
        number = self.one_move_player()
        self.board.change_cell(number, player.symbol)


player1 = Player("Олег", "X")
player2 = Player("Алиса", "O")
game = Game(player1, player2)

count = 0
while True:
    if count % 2 == 0:
        game.start(player1)
    else:
        game.start(player2)
    count += 1
    if count > 4:
        if game.board.check_win():
            break
    if count == 9:
        print("Ничья")
        game.board.display()
        break
