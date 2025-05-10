'''
Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Укажите минимальное значение "S", когда такая ситуация возможна.
'''


def F(s, h):
    if h == 3 and s >= 42:
        return 1
    elif (h == 3 and s < 42) or (h != 3 and s >= 42):
        return 0
    else:
        if h % 2 == 0:
            return F(s + 1, h + 1) or F(s + 5, h + 1) or F(s * 3, h + 1)
        else:
            return F(s + 1, h + 1) or F(s + 5, h + 1) or F(s * 3, h + 1)


for s in range(1, 42 + 1):
    if F(s, 1):
        print(s)
        break
