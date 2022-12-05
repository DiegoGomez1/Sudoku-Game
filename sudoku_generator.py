import random
import math


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def get_board(self):
        return self.board

    def valid_in_row(self, row, num):
        for numbers in self.board[row]:
            if numbers == num:
                return False
        else:
            return True

    def valid_in_col(self, col, num):
        for rows in self.board:
            if num == rows[col]:
                return False
        else:
            return True

    def valid_in_box(self, row_start, col_start, num):
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                if num == self.board[row_start+box_row][col_start+box_col]:
                    return False
            else:
                return True

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and \
               self.valid_in_box(row_start=row - row % 3, col_start=col - col % 3, num=num)

    def fill_box(self, row_start, col_start):
        numbers = [1,2,3,4,5,6,7,8,9]
        random.shuffle(numbers)
        counter = 0
        for l in range(0, 3):
            for j in range(0, 3):
                self.board[row_start + l][col_start + j] = numbers[counter]
                counter += 1

    def fill_diagonal(self):
        for box_number in range(0,3):
            self.fill_box(box_number*3,box_number*3)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False


    def remove_cells(self):
        coordinates_of_removed =[]
        i =0
        while i < self.removed_cells:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if [x,y] not in coordinates_of_removed:
                self.board[x][y] = 0
                coordinates_of_removed.append([x, y])
                i +=1
            else:
                x = random.randint(0, 8)
                y = random.randint(0, 8)


    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)



def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
