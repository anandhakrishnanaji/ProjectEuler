MAX_SIZE = 2_000_000

status = [
    True,
] * MAX_SIZE

status[0] = status[1] = False
count_sum = 0

for i in range(2, MAX_SIZE):
    if status[i]:
        count_sum += i
        for j in range(i * i, MAX_SIZE, i):
            status[j] = False

print(count_sum)
