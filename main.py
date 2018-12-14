from copy import deepcopy
from game3125 import Game3125


def print_field(game, field):

    print("Счет: ", game.score)
    cell_width = len(str(max(cell for row in field for cell in row )))
    print('\n'.join(' '.join(str(cell).rjust(cell_width) for cell in row ) for row in field ))
    print("W, A, S, D - играть", "Q - выход", sep='\n')


def main():

    game = Game3125()
    game.add_random_cell()
    game.add_random_cell()
    while True:
        old_field = deepcopy(game.field)
        print_field(game, old_field)

        if not game.can_move():
            print("Не возможно совершить движение. Игра окончена.")
            break

        while True:
            button_char = str(input())
            if button_char in ('a', 'A'):
                game.move_left()
                break
            elif button_char in ('d', 'D'):
                game.move_right()
                break
            elif button_char in ('w', 'W'):
                game.move_up()
                break
            elif button_char in ('s', 'S'):
                game.move_down()
                break
            elif button_char in ('q', 'Q'):
                exit()

        if game.check_empty() and game.field != old_field:
            game.add_random_cell()


if __name__ == '__main__':
    main()
