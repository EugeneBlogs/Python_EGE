# Условие задания КИМ 8 (Гусева Марина Альфонсовна):
'''
Все 5 буквенные слова, составленные из букв "А", "К", "Р", "У", записаны в алфавитном порядке.
Вот начало списка:
1. ААААА
2. ААААК
3. ААААР
4. ААААУ
5. АААКА
...
Укажите номер первого слова, которое начинается с буквы "У".
'''

from itertools import product  # Используем именно эту библиотеку, так как буквы повторяются

# Все перестановки из данных букв (Буквы в алфавитном поряде обязательно; "repeat=..." обязательно)
p = product("АКРУ", repeat=5)
count = 1  # Счётчик с 1, так как ищем номер
for x in p:
    str = "".join(x)  # Преобразуем кортеж в строку (разделитель отсутствует)
    if str[0] == 'У':  # Прописываем нужные условия: первая буква "У"
        # Выводим номер и завершаем цикл
        print(count)
        break
    count += 1

'''
Все 6 буквенные слова, составленные из букв "С", "В", "Е", "Т", записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
1. ВВВВВB
2. ВВВВВЕ
3. ВВВВВС
4. ВВВВВТ
5. ВВВВЕВ
Под каким номером стоит первое из слов, которое начинается с буквы "Т"?
'''
from itertools import product

p = product("ВЕСТ", repeat=6)
count = 1
for x in p:
    str = "".join(x)
    if str[0] == 'Т':
        print(count)
        break
    count += 1
