# Условие задания КИМ 24 (Решу ЕГЭ):
'''
Текстовый файл содержит только заглавные буквы латинского алфавита ("ABC...Z").
Определите символ, который чаще всего встречается в файле сразу после буквы "A".
'''

f = open("10.txt")
s = f.readline()
# Создаём большой массив, который работает по принципу:
# count[код символа в таблице ASCII] = количество символа в строке
count = [0] * 100
for i in range(1, len(s)):
    # Если предыдущий символ - "A"
    if s[i - 1] == "A":
        # По номеру символа в таблице ASCII прибавляем 1
        count[ord(s[i])] += 1
maximim = max(count)  # Максимальное число встреч
element = count.index(maximim)  # Индекс максимума
letter = chr(element)  # Буква по идексу
print(letter)
