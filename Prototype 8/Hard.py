# Условие задания КИМ 8 (Умскул):
'''
Математик Артур составляет пятибуквенные слова, используя буквы
"М", "А", "Л", "Й", "И", "Н", "К". Он знает, что ровно три буквы находятся на тех же
позициях, что и в слове "АЙЛИН".
Сколько различных слов может составить Артур?
'''

from itertools import product

p = product("МАЛЙИНК", repeat=5)
word = "АЙЛИН"
count = 0
for x in p:
    correct = 0
    for i in range(len(x)):
        if x[i] == word[i]:
            correct += 1
    if correct == 3:
        count += 1
print(count)
