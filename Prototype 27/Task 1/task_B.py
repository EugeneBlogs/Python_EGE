# СПОСОБ 2

'''
В файле Excel необходимо построить диагрумму кластеров (выделяем столбцы A и B, "Вставка" - "Диаграммы" - "Точечная")
Заметим, что если y > 7, то это первый кластер.
Если 3 <= y <= 7, то это второй кластер.
Если y < 3, то это третий кластер.
'''

import math
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Функция, которая возвращает центроид одного кластера
def recalculate_centroid(claster):
    final_centroids = []
    min_sum_distance = 10**10
    # Проходимся по всем центроидам в кластере
    for centroid in claster:
        sum_distance = 0
        # Проходимся по всем точкам в кластере
        for point in claster:
            sum_distance += euclidean_distance(centroid, point) # Добавляем Евклидова расстояние от центроида до точки
        if sum_distance < min_sum_distance:
            min_sum_distance = sum_distance
            final_centroids = centroid
    return final_centroids

file = open("demo_2025_27_B.txt")
file.readline()
points = [list(map(float, s.replace(",", ".").split())) for s in file]
k = 3  # Количество кластеров (в условии задачи)
clusters = [[] for _ in range(k)]  # Создаём список кластеров, и каждый раз создаём пустой список
for x, y in points:  # Проходимся по всем точкам
    if y > 7: # Если y > 7, то добавляем точку в нулевой кластер
        clusters[0].append([x, y])
    elif y > 3: # Если y < 3, то добавляем точку в первый кластер
        clusters[1].append([x, y])
    else: # Остальные точки добавляем во второй кластер
        clusters[2].append([x, y])
final_centroids = [recalculate_centroid(clusters[i]) for i in range(k)] # Массив из центроидов всех кластеров
# То же самое, что и в задаче А, только делим на k (количество кластеров)
P_x = int(sum([x for x, y in final_centroids]) / k * 10_000)
P_y = int(sum([y for x, y in final_centroids]) / k * 10_000)
print(P_x, P_y)
