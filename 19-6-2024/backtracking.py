def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []

    def backtrack(board, col):
        if col == N:
            result.append([''.join(row) for row in board])
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'

    backtrack(board, 0)
    return result


N1 = 4
result1 = solve_n_queens(N1)
print(f"Solution for Example 1 with N = {N1}:")
for solution in result1:
    print(solution)
print()

N2 = 1
result2 = solve_n_queens(N2)
print(f"Solution for Example 2 with N = {N2}:")
for solution in result2:
    print(solution)
