MARK_X = "X"
MARK_O = "O"
raw_input = " " * 9
input_ = list(raw_input)



def print_state():
    print("---------")
    print("|", input_[0], input_[1], input_[2], "|")
    print("|", input_[3], input_[4], input_[5], "|")
    print("|", input_[6], input_[7], input_[8], "|")
    print("---------")


def count_of_mark(matrix, symbol):
    return len([x for x in matrix if x == symbol])


def check_impossible():
    count_of_mark_x = count_of_mark(input_, MARK_X)
    count_of_mark_o = count_of_mark(input_, MARK_O)
    return abs(count_of_mark_x - count_of_mark_o) > 1


def check_row_full(mark):
    success_rows = [[input_[0], input_[1], input_[2]],
                    [input_[3], input_[4], input_[5]],
                    [input_[6], input_[7], input_[8]],
                    [input_[0], input_[4], input_[8]],
                    [input_[2], input_[4], input_[6]],
                    [input_[0], input_[3], input_[6]],
                    [input_[1], input_[4], input_[7]],
                    [input_[2], input_[5], input_[8]]]
    x = [rw for rw in success_rows if rw[0] == rw[1] == rw[2] == mark]
    return len(x) > 0


print_state()


def check_state():
    global stop_asking_for_input
    x_is_winner = check_row_full(MARK_X)
    o_is_winner = check_row_full(MARK_O)

    if check_impossible():
        print("Impossible")
    elif x_is_winner and o_is_winner:
        print("Impossible")
        stop_asking_for_input = True
    elif x_is_winner:
        print("X wins")
        stop_asking_for_input = True
    elif o_is_winner:
        print("O wins")
        stop_asking_for_input = True
    elif " " not in input_:
        print("Draw")
        stop_asking_for_input = True
    elif " " in input_:
        print("Game not finished")


user_input_y = 0
user_input_x = 0
stop_asking_for_input = False
active_player = MARK_X
while not stop_asking_for_input:
    try:
        user_input_y, user_input_x = [int(x) for x in input().split()]
    except Exception:
        print("You should enter numbers!")
    else:
        if max(user_input_y, user_input_x) > 3 or min(user_input_y, user_input_x) < 0:
            print("Coordinates should be from 1 to 3!")
        else:
            position = (user_input_y - 1) * 3 + user_input_x - 1
            if input_[position] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                input_[position] = active_player
                active_player = MARK_O if active_player == "X" else MARK_X
                print_state()
                check_state()
