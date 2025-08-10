import math

file = open("../27_B.txt")
file.readline()
points = [list(map(float, s.replace(",", ".").split())) for s in file]
clusters = []
epsilon = 1

while points:
    clusters.append([points[0]])
    del points[0]

    for p1 in clusters[-1]:
        for p2 in points[:]:
            if math.dist(p1, p2) < epsilon:
                clusters[-1].append(p2)
                points.remove(p2)

# Визуализируем данные для проверки

from turtle import *

k = 80
colors = ["red", "blue", "green", "yellow", "cyan", "pink", "purple", "brown", "black"]
screensize(2000, 2000), tracer(0), penup()

for i in range(len(clusters)):
    for x, y in clusters[i]:
        setpos(x * k, y * k)
        dot(5, colors[i])
done()

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

P_x = (sum([x for x, y in best_centroids]) / len(clusters)) * 10_000
P_y = (sum([y for x, y in best_centroids]) / len(clusters)) * 10_000
print(int(P_x), int(P_y))
