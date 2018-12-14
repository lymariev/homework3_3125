import random


class Game3125:

    def __init__(self):
        self.field = [[0] * 4 for _ in range(4)]
        self.num_row = len(self.field)
        self.num_col = max(len(row) for row in self.field)
        self.score = 0

    def move_horizontal(self, param):

        for row in range(self.num_row):
            for col in range(param[0], param[1], param[2]):
                for col_pair in range(col + param[3], param[4], param[2]):
                    if self.field[row][col_pair] > 0 and self.field[row][col] == self.field[row][col_pair] > 0:
                        self.field[row][col] *= 5
                        self.field[row][col_pair] = 0
                        self.score += self.field[row][col]
                        break
                    elif self.field[row][col_pair] > 0:
                        break

        for row in range(self.num_row):
            for col_em in range(param[0], param[1], param[2]):
                if self.field[row][col_em] == 0:
                    for col in range(col_em + param[3], param[4], param[2]):
                        if self.field[row][col] > 0:
                            self.field[row][col_em] = self.field[row][col]
                            self.field[row][col] = 0
                            break

    def move_vertical(self, param):

        for col in range(self.num_col):
            for row in range(param[0], param[1], param[2]):
                for row_pair in range(row + param[3], param[4], param[2]):
                    if self.field[row][col] == self.field[row_pair][col] > 0:
                        self.field[row][col] *= 5
                        self.field[row_pair][col] = 0
                        self.score += self.field[row][col]
                        break
                    elif self.field[row_pair][col] > 0:
                        break

        for col in range(self.num_col):
            for row_em in range(param[0], param[1], param[2]):
                if self.field[row_em][col] == 0:
                    for row in range(row_em + param[3], param[4], param[2]):
                        if self.field[row][col] > 0:
                            self.field[row_em][col] = self.field[row][col]
                            self.field[row][col] = 0
                            break

    def move_left(self):
        self.move_horizontal([0, self.num_col - 1, 1, 1, self.num_col])

    def move_right(self):
        self.move_horizontal([self.num_col - 1, 0, -1, -1, -1])

    def move_up(self):
        self.move_vertical([0, self.num_row - 1, 1, 1, self.num_row])

    def move_down(self):
        self.move_vertical([self.num_row - 1, 0, -1, -1, -1])

    def check_empty(self):
        for row in range(self.num_row):
            for col in range(self.num_col):
                if self.field[row][col] == 0:
                    return True
        return False

    def can_move(self):
        for row in range(self.num_row - 1):
            for col in range(self.num_col - 1):
                if self.field[row][col] == self.field[row][col + 1] or self.field[row][col] == self.field[row + 1][col]:
                    return True

        for col in range(self.num_col - 1):
            if self.field[self.num_row - 1][col] == self.field[self.num_row - 1][col + 1]:
                return True

        for row in range(self.num_row - 1):
            if self.field[row][self.num_col - 1] == self.field[row + 1][self.num_col - 1]:
                return True

        return False

    def add_random_cell(self):
        if random.randint(1, 10) == 1:
            new_num = 25
        else:
            new_num = 5

        while True:
            random_index = random.randrange(0, self.num_row * self.num_col)
            row = random_index // self.num_col
            col = random_index % self.num_col
            if self.field[row][col] == 0:
                self.field[row][col] = new_num
                break
