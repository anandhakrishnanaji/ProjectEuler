for i in range(1, 1000):
    for j in range(i, 1000):
        k = 1000 - i - j
        if k > 0 and i**2 + j**2 == k**2:
            print(i * j * k)
            break
    else:
        continue
    break
