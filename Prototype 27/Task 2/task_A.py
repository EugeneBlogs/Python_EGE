import math

file = open("27_A.txt")
k = 2
points = [list(map(float, s.replace(",", ".").split())) for s in file]
clusters = [[] for _ in range(k)]

for x, y in points:
    if y < 12:
        clusters[0].append([x, y])
    else:
        clusters[1].append([x, y])

best_anticentroids = [[] for _ in range(k)]
for i in range(k):
    max_sum_dist = 0
    for x1, y1 in clusters[i]:
        sum_dist = 0
        for x2, y2 in clusters[i]:
            sum_dist += math.dist([x1, y1], [x2, y2])
        if sum_dist > max_sum_dist:
            max_sum_dist = sum_dist
            best_anticentroids[i] = [len(clusters[i]), x1, y1]

print(int(min(best_anticentroids)[1] * 10_000))
print(int(max(best_anticentroids)[2] * 10_000))
