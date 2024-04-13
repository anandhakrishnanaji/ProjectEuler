TEXT_DICT = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    1000: 11,
}


def count_letters(n):
    if n in TEXT_DICT.keys():
        return TEXT_DICT[n]

    n_string = str(n)

    if len(n_string) == 3:
        TEXT_DICT[n] = TEXT_DICT[n // 100] + 7 + (n % 100 and 3) + TEXT_DICT[n % 100]
    if len(n_string) == 2:
        TEXT_DICT[n] = TEXT_DICT[n - (n % 10)] + TEXT_DICT[n % 10]

    return TEXT_DICT[n]


if __name__ == "__main__":
    print(sum(count_letters(x) for x in range(1, 1001)))
