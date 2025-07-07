def prostoe(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


count = 0
for x in range(3120341, 3120451 + 1):
    if prostoe(x):
        count += 1
        print(count, x)
