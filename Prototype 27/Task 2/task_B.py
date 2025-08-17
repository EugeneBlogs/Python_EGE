import math

file = open("27_B.txt")
k = 3  # Количество кластеров
# Считываем данные: построчно, заменяя запятые на точки, разделяем числа по пробелам и конвертируем в дробные
points = [list(map(float, s.replace(",", ".").split())) for s in file]
clusters = [[] for _ in range(k)]  # Кластеры (пока пустые)
# Проходим по точкам и кластеризуем их
'''
Для разделения по кластерам мы переносим значения в Excel, создаём точечную диаграмму
и ищем значения координат, по которым можно разделять точки по кластерам.
'''
for x, y in points:
    if y < 10:
        clusters[0].append([x, y])
    elif x < 17:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

best_anticentroids = [[] for _ in range(k)]  # Список антицентроидов (на каждый кластер - свой антицентроид)
# Проходимся по каждому кластеру
for i in range(k):
    max_sum_dist = 0  # Максимальное суммарное расстояние
    # Проходимся по всем точкам какого-то кластера
    for x1, y1 in clusters[i]:
        sum_dist = 0  # Суммарное расстояние от точки до остальных точек
        # Ищем расстояние до всех точек этого кластера от текущей точки (включая саму себя)
        for x2, y2 in clusters[i]:
            # Евклидово расстояние с помощью библиотеки
            sum_dist += math.dist([x1, y1], [x2, y2])
        # Если текущее суммарное расстояние больше максимума, то обновляем значения
        if sum_dist > max_sum_dist:
            max_sum_dist = sum_dist
            '''
            В новый антицентроид добавляем его координаты и число точек кластера,
            чтобы позже использовать данную информацию для сортировки.
            '''
            best_anticentroids[i] = [len(clusters[i]), x1, y1]

# Абсцисса (идёт второй после количества, поэтому 1) антицентра кластера с наименьшим числом точек
print(int(min(best_anticentroids)[1] * 10_000))
# Ордината (идёт третий после абсциссы, поэтому 2) антицентра кластера с наибольшим числом точек
print(int(max(best_anticentroids)[2] * 10_000))

'''
Дополнительный вопрос (из другой задачи):
Для файла "Б" определите координаты центра каждого кластера, затем найдите два числа:
"Qx" - разность абсцисс центров кластеров с минимальным и максимальным количеством точек;
"Qy" - разность ординат центров кластеров с минимальным и максимальным количеством точек;
'''

# Находим центроиды, так как по условию данной задачи мы находили антицентроиды
best_centroids = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = 10 ** 10
    for x1, y1 in clusters[i]:
        sum_dist = 0
        for x2, y2 in clusters[i]:
            sum_dist += math.dist([x1, y1], [x2, y2])
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroids[i] = [x1, y1]

# Находим ID кластеров с минимальным и максимальным количеством точек
min_points, max_points = min([len(c) for c in clusters]), max([len(c) for c in clusters])
min_ID, max_ID = 0, 0
for i in range(len(clusters)):
    if len(clusters[i]) == min_points:
        min_ID = i
    if len(clusters[i]) == max_points:
        max_ID = i

# Вычисляем значения
Q_x = int(abs(best_centroids[max_ID][0] - best_centroids[min_ID][0]) * 10_000)
Q_y = int(abs(best_centroids[max_ID][1] - best_centroids[min_ID][1]) * 10_000)
print(Q_x, Q_y)
