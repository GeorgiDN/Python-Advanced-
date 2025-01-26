player_one = None
player_two = None
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def take_name_player_input(player_one_name):
    while True:
        player_two_name = input('Player two name: ').strip()
        if not player_two_name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        if player_two_name == player_one_name:
            print("Your opponent's name is the same. Please choose a different name.")
            continue
        return player_two_name


def take_player_sign(player_one_name):
    while True:
        player_one_sign = input(f'{player_one_name}, would you like to use "X" or "O"? ').strip().upper()
        if player_one_sign in ['X', 'O']:
            return player_one_sign
        print(f'Invalid input. Please select "X" or "O".')


def setup():
    global player_one, player_two
    while True:
        player_one_name = input("Player one name: ").strip()
        if player_one_name:
            break
        print("Name cannot be empty. Please enter a valid name.")

    player_two_name = take_name_player_input(player_one_name)
    player_one_sign = take_player_sign(player_one_name)
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]

    print('This is the numeration of the board:')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    print(f'{player_one_name} starts first!')


def draw_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join(row), end=' |\n')


def take_cell_number():
    while True:
        try:
            choice = int(input(f'{current[0]}, choose a free position [1-9]: ').strip())
            if 1 <= choice <= 9:
                return choice
            else:
                print("Invalid input. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 9.")


def check_if_won(current, board):
    global loop
    first_row = all(x == current[1] for x in board[0])
    second_row = all(x == current[1] for x in board[1])
    third_row = all(x == current[1] for x in board[2])
    first_column = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_column = all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_column = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[2][0], board[1][1], board[0][2]])

    if any([first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal,
            second_diagonal]):
        print(f'{current[0]} won!')
        loop = False


def check_for_draw(board):
    global loop
    for row in board:
        if ' ' in row:
            return
    print('DRAW!')
    loop = False


def play(current, board):
    while True:
        choice = take_cell_number()
        row = (choice - 1) // 3
        col = (choice - 1) % 3
        if board[row][col] == ' ':
            board[row][col] = current[1]
            break
        else:
            print("Position already taken. Please choose another.")
    draw_board(board)
    check_if_won(current, board)
    check_for_draw(board)


setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board)
    current, other = other, current
