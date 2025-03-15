import random

class Minesweeper:
    def __init__(self, width=10, height=10, num_mines=10):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != -1:
                self.board[y][x] = -1
                mines_placed += 1

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == -1:
                    continue
                count = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < self.height and 0 <= nx < self.width and self.board[ny][nx] == -1:
                            count += 1
                self.board[y][x] = count

    def print_board(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if self.revealed[y][x]:
                    if self.board[y][x] == -1:
                        row.append('*')
                    else:
                        row.append(str(self.board[y][x]))
                else:
                    row.append('.')
            print(' '.join(row))

    def reveal(self, x, y):
        if self.board[y][x] == -1:
            self.game_over = True
            return
        if self.revealed[y][x]:
            return
        self.revealed[y][x] = True
        if self.board[y][x] == 0:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        self.reveal(nx, ny)

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1 and not self.revealed[y][x]:
                    return False
        return True

def main():
    game = Minesweeper()
    while not game.game_over:
        game.print_board()
        try:
            x = int(input("輸入X座標: "))
            y = int(input("輸入Y座標: "))
            game.reveal(x, y)
            if game.check_win():
                print("你贏了！")
                break
        except ValueError:
            print("請輸入有效的數字。")
    game.print_board()
    if game.game_over:
        print("你踩到地雷了！遊戲結束。")

if __name__ == "__main__":
    main()
