# Разложение числа на простые множители
def p(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return [i] + p(x // i)
    return [x]


n = int(input("Введите число: "))
print(f"Разложение числа {n}: {p(n)}")
