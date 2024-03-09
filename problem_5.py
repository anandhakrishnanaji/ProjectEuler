from pydash import reduce_


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


numbers = list(range(1, 21))

lcm = reduce_(numbers, lcm, 1)

print(lcm)
