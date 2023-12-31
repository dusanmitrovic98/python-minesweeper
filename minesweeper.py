import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.mine_locations = []

    def place_mines(self):
        mines = 0
        while mines < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != 'X':
                self.board[y][x] = 'X'
                self.mine_locations.append((x, y))
                mines += 1

    def get_adjacent_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (
                    x + i >= 0 and x + i < self.width and
                    y + j >= 0 and y + j < self.height and
                    self.board[y + j][x + i] == 'X'
                ):
                    count += 1
        return count

    def reveal_cell(self, x, y):
        if self.board[y][x] != ' ':
            return

        if (x, y) in self.mine_locations:
            self.board[y][x] = 'X'
            return

        mines = self.get_adjacent_mines(x, y)
        if mines > 0:
            self.board[y][x] = str(mines)
        else:
            self.board[y][x] = ' '

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if (
                        x + i >= 0 and x + i < self.width and
                        y + j >= 0 and y + j < self.height
                    ):
                        self.reveal_cell(x + i, y + j)

    def print_board(self, reveal=False):
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        print('  +' + '-' * (2 * self.width - 1) + '+')

        for i in range(self.height):
            row = str(i) + ' |'
            for j in range(self.width):
                cell = self.board[i][j]
                if cell == 'X' and not reveal:
                    row += '  '
                else:
                    row += f' {cell}'

            row += ' |'
            print(row)

        print('  +' + '-' * (2 * self.width - 1) + '+')

    def play(self):
        self.place_mines()
        game_over = False

        while not game_over:
            self.print_board()

            x = int(input("Enter the x coordinate: "))
            y = int(input("Enter the y coordinate: "))

            if (x, y) in self.mine_locations:
                print("Game over! You hit a mine.")
                self.print_board(reveal=True)
                game_over = True
            else:
                self.reveal_cell(x, y)

                if all(
                    self.board[y][x] != ' ' or
                    (x, y) in self.mine_locations
                    for y in range(self.height)
                    for x in range(self.width)
                ):
                    print("Congratulations! You won!")
                    self.print_board(reveal=True)
                    game_over = True

game = Minesweeper(8, 8, 10)
game.play()
