COINS = [200, 100, 50, 20, 10, 5, 2, 1]
COIN_COUNT = 8


def count_combination(amount, pos):
    if not amount:
        return 1

    count = 0
    for i in range(pos, COIN_COUNT):
        if COINS[i] <= amount:
            count += count_combination(amount - COINS[i], i)

    return count


if __name__ == "__main__":
    print(count_combination(200, 0))
