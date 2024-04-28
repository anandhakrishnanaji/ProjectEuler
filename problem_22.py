BASE_ASCII = 64


score = lambda pos, name: pos * sum(map(lambda x: ord(x) - BASE_ASCII, name))


with open("data/0022_names.txt", "r") as f:
    print(
        sum(
            map(
                lambda tup: score(tup[0] + 1, tup[1].strip('"')),
                enumerate(sorted(f.read().split(","))),
            )
        )
    )
