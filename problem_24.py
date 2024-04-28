import math

PERMUTATION_LENGTH = 10
PERMUTATION_LIMIT = 1_000_000

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
total_permutations = math.factorial(PERMUTATION_LENGTH)
permutation = ""
limit = PERMUTATION_LIMIT - 1


while (curr_length := len(permutation)) < PERMUTATION_LENGTH:
    balance_length = PERMUTATION_LENGTH - curr_length
    slot_length = total_permutations // balance_length
    digit = limit // slot_length

    permutation += digits[digit]
    limit -= slot_length * digit
    total_permutations //= balance_length
    digits.pop(digit)

print(permutation)
