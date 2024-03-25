MAX_SIZE = 200_000

status = [
    True,
] * MAX_SIZE

status[0] = status[1] = False
count = 0
prime_10001 = 0

for i in range(2, MAX_SIZE):
    if status[i]:
        count += 1
        if count == 10_001:
            prime_10001 = i
            break
        for j in range(i * i, MAX_SIZE, i):
            status[j] = False

print(prime_10001)
