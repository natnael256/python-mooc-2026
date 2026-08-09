# Write your solution here
def play_turn(board: list, x: int, y: int, piece: str):

    for i in range(len(board)):

        for j in range(len(board)):
            # check low and up bound 
            if x > 2 or y > 2 or x < 0 or y < 0:
                return False
                
            if board[y][x] =="":
                board[y][x] = piece
                return True
            else:
                return False

    


if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 1, -1, "X"))
    print(game_board)