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
