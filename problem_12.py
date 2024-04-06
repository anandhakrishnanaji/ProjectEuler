import math

digit = 1
iteration = 2

while True:
    divisor_count = 2
    limit = int(math.sqrt(digit))
    for i in range(2, limit):
        divisor_count += 0 if digit % i else 2
    if divisor_count > 500:
        break
    digit += iteration
    iteration += 1

print(digit)
