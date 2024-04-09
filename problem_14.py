TARGET = 1_000_000

dp = {1: 1}


def chain_length(n):
    if n not in dp.keys():
        dp[n] = chain_length(3 * n + 1 if n % 2 else n // 2) + 1
    return dp[n]


if __name__ == "__main__":
    max_length = 0
    max_index = 0

    for i in range(1, TARGET):
        if (c_len := chain_length(i)) > max_length:
            max_length, max_index = c_len, i

    print(max_index, max_length)
