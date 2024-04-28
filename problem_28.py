LIMIT = 1001

diagonal_sum = 1
num = 1
cd = 2

for i in range(1, LIMIT, 2):
    diagonal_sum += 2 * (num + cd + num + cd * 4)
    num += cd * 4
    cd += 2


print(diagonal_sum)
