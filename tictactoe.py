'''
This Tic-Tac-Toe is a two-player game where players complete turns and enter X or O in a 3x3 grid
Author: Erik Galstian
'''

def main():
    # Function to toggle between X and O
    def switch_player(now):
        if now == "" or now == "O":
            return "X"
        if now == "" or now == "X":
            return "O"

    # Function to initiate board
    def initiate_board():
        board = []
        for square in range(9):
            board.append(square + 1)
        return board

    # Function to start game
    def start_game(board):
        for square in range(9):
            if board[square] != "X" and board[square] != "O":
                return False
        return True

    # Function to show board
    def show_board(board):
        print()
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print("-----")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("-----")
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print()

    # Function to determine if there is a winner
    def winner(board):
        return (board[0] == board[1] == board[2] or
                board[0] == board[3] == board[6] or
                board[0] == board[4] == board[8] or
                board[1] == board[4] == board[7] or
                board[2] == board[5] == board[8] or
                board[2] == board[4] == board[6] or
                board[3] == board[4] == board[5] or
                board[6] == board[7] == board[8])

    # Function to move to next turn
    def next_turn(player, board):
        square = int(input(f"{player}'s turn to play, please select a square between 1-9: "))
        board[square - 1] = player

    # Calling the functions
    player = switch_player("")
    board = initiate_board()
    while not (winner(board) or start_game(board)):
        show_board(board)
        next_turn(player, board)
        player = switch_player(player)
    show_board(board)
    print(f"Good game. Have a good luck next time!")


if __name__ =="__main__":
    main()