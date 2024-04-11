GRID_SIZE = 20
SIZE = GRID_SIZE + 1

dp = [[0] * SIZE for i in range(SIZE)]
dp[SIZE - 1][SIZE - 1] = 1


def is_valid(i, j):
    return i < SIZE and j < SIZE and i >= 0 and j >= 0


def is_final_state(i, j):
    return i == SIZE - 1 and j == SIZE - 1


def count(i, j):
    if not is_valid(i, j):
        return 0

    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = count(i + 1, j) + count(i, j + 1)

    return dp[i][j]


print(count(0, 0))
