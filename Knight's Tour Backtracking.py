# Python3 program to solve Knight Tour problem using Backtracking

# Chessboard Size
n = 8


def is_empty(x, y, board):
    '''
        A utility function to check if i,j are valid indexes
        for N*N chessboard
    '''
    if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
        return True
    return False


def print_solution(n, board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


# def write_file(n, board):
#     with open("result.txt","w") as f:
#         for i in range(n):
#             for j in range(n):
#                 f.write(str(board[i][j]))
#                 f.write(" ")
#             f.write("\n")


def solve(n):
    '''
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than one solutions,
        this function prints one of the feasible solutions.
    '''

    # Initialization of Board matrix
    board = [[-1 for i in range(n)] for i in range(n)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # The Knight is initially block
    board[0][0] = 0

    # Step counter for knight's position
    pos = 1

    # Checking if solution exists or not
    if not solve_knight_tour(n, board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        print_solution(n, board)
        # write_file(n, board)


def solve_knight_tour(n, board, curr_x, curr_y, move_x, move_y, pos):
    if pos == n ** 2:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_empty(new_x, new_y, board):
            board[new_x][new_y] = pos
            if solve_knight_tour(n, board, new_x, new_y, move_x, move_y, pos + 1):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False


# Driver Code
if __name__ == "__main__":
    # Function Call
    solve(n)

