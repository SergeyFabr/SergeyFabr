import random


class GameTicTacToe:
    wining_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 3, 6), (1, 4, 7), (2, 5, 8),
                           (0, 4, 8), (2, 4, 6))

    def __init__(self, y_1='1', y_2='2', y_3='3', y_4='4', y_5='5', y_6='6', y_7='7', y_8='8', y_9='9'):
        self. teams = [y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9]

    def print_table(self):
        print(f' {self.teams[0]} | {self.teams[1]} | {self.teams[2]}')
        print('-----------')
        print(f' {self.teams[3]} | {self.teams[4]} | {self.teams[5]}')
        print('-----------')
        print(f' {self.teams[6]} | {self.teams[7]} | {self.teams[8]}')

    def motion_comp(self):
        while True:
            number = random.randint(1, 9)
            if str(number) in self.teams:
                self.teams[number - 1] = 'O'
                break

    def motion_player(self):
        while True:
            answer = int(input('\nКуда поставим "X"? '))
            if str(answer) in self.teams:
                self.teams[answer - 1] = 'X'
                break
            else:
                print('Эта клеточка уже занята')
        game.motion_comp()

    def check_win(self):
        for i_elem in self.wining_combinations:
            if self.teams[i_elem[0]] == self.teams[i_elem[1]] == self.teams[i_elem[2]]:
                return self.teams[i_elem[0]]


game = GameTicTacToe()
print('Для игры используйте цифры 1-9, расположение цифр приведено ниже в таблице:')
game.print_table()

for i_num in range(5):
    if game.check_win() == 'X':
        print('Ты выиграл!')
        break
    elif game.check_win() == 'O':
        print('Ты проиграл!')
        break
    elif i_num == 4:
        print('Ничья')
    game.motion_player()
    game.print_table()



1

