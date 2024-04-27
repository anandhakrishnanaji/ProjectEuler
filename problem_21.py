import math

dp = [-1, 0, 1]
amicable_nums = []


def find_divisor_sum(n):
    dp.append(1)
    root = math.ceil(math.sqrt(n))
    for i in range(2, root):
        if not n % i:
            dp[n] += i + n // i
    if not n % root:
        dp[n] += root

    return dp[n]


for i in range(3, 10000):
    find_divisor_sum(i)

if __name__ == "__main__":
    for i in range(3, 10000):
        try:
            if i != dp[i] and i == dp[dp[i]]:
                amicable_nums.append(i)
        except:
            continue

    print(sum(amicable_nums))
