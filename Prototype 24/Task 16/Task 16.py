# Условие задания КИМ 24 (Гусева Марина Альфонсовна, "Сайт Константина Полякова"):
'''
Текстовый файл состоит не более чем из 10^6 символов и содержит только заглавные буквы латинского алфавита ("ABC...Z").
Текст разбит на строки различной длины.
Необходимо найти строку, содержащую самую длинную цепочку стоящих подряд одинаковых букв.
Если таких строк несколько, надо взять ту, которая в файле встретилась раньше.
Определите, какая буква встречается в этой строке реже всего (но присутствует!).
Если таких букв несколько, надо взять ту, которая стоит позже в алфавите.
Запишите в ответе эту букву, а затем - сколько раз она встречается во всем файле.
'''

f = open("16.txt")
data = f.readlines()
max_len = 0
id = 0
for i in range(len(data)):
    el = data[i]
    count = 1
    max_count = 0
    for j in range(len(el) - 1):
        if el[j] == el[j + 1]:
            count += 1
            max_count = max(max_count, count)
        else:
            max_count = max(max_count, count)
            count = 1
    if max_count > max_len:
        max_len = max_count
        id = i
result = data[id]
alphabet = [0] * 100
for s in result:
    if s.isalpha():
        alphabet[ord(s)] += 1
min_number = 10 ** 10
id_letter = 0
for i in range(len(alphabet) - 1, -1, -1):
    if alphabet[i] < min_number and alphabet[i] != 0:
        min_number = alphabet[i]
        id_letter = i
text = "".join(data)
print(chr(id_letter), text.count(chr(id_letter)))
