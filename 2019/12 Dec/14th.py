# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Salesforce.
#
# Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid.
# The game ends either when one player creates a line of four consecutive discs of their color (horizontally,
# vertically, or diagonally), or when there are no more spots left in the grid.
#
# Design and implement Connect 4.
# | 41 | 40 | 39 | 38 | 37 | 36 | 35 |
# | 34 | 33 | 32 | 31 | 30 | 29 | 28 |
# | 27 | 26 | 25 | 24 | 23 | 22 | 21 |
# | 20 | 19 | 18 | 17 | 16 | 15 | 14 |
# | 13 | 12 | 11 | 10 | 9  | 8  | 7  |
# |  6 |  5 |  4 |  3 | 2  | 1  | 0  |


def list_contains(A, B):
    return ', '.join(map(str, A)) in ', '.join(map(str, B))


class Connect4:
    turn = "X"
    values = []

    def __init__(self, grid_x=7, grid_y=6, win=4):
        assert grid_x < 10 and grid_y < 10
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.win = win
        for i in range(self.grid_y):
            Connect4.values.append([None] * self.grid_x)
        self.run_game()

    def run_game(self):
        print(self)
        while not self.check_win(Connect4.player_input(self)):
            print(self)
            if Connect4.turn == "X":
                Connect4.turn = "Y"
            else:
                Connect4.turn = "X"
        print("\n{}\n{} Wins!".format(self, Connect4.turn))

    def check_win(self, l):
        win_c = [Connect4.turn] * self.win
        x, y = l[::-1]
        # Horizontal
        if list_contains(win_c, Connect4.values[y]):
            return True
        # Vertical
        tmp = []
        for i in range(self.grid_y):
            pass
        return False

    #
    # [[00, 10, 20, 30, 40, 50, 60],
    #  [01, 11, 22, 31, 41, 51, 61],
    #  [02, 12, 22, 32, 42, 52, 62],
    #  [03, 13, 23, 33, 43, 53, 63],
    #  [04, 14, 24, 34, 44, 54, 64],
    #  [05, 15, 25, 35, 45, 55, 65 ]]

    def __str__(self):
        l = []
        for e in Connect4.values:
            for i in e:
                if i is None:
                    i = " "
                l.append(i)
        return " " + (" {}  " * self.grid_x).format(*list(range(self.grid_x))) + "\n" + \
               (("|" + (" {} |" * self.grid_x) + "\n") * self.grid_y).format(*l)

    def player_input(self):
        inp = None
        print("It is {}'s turn".format(Connect4.turn))
        while True:
            inp = input("Please enter your turn:".format(Connect4.turn))
            try:
                inp = int(inp)
                if 0 <= inp < self.grid_x:
                    if Connect4.values[0][inp] is not None:
                        print("Row full, ", end="")
                        raise ValueError

                    for i in range(self.grid_y - 1, -1, -1):
                        if Connect4.values[i][inp] is None:
                            Connect4.values[i][inp] = Connect4.turn
                            return [i, inp]

                else:
                    raise ValueError

            except ValueError:
                print("Invalid input, Try again")


if __name__ == '__main__':
    g = Connect4()
