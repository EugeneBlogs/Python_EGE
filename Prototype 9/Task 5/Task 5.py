file = open("5.txt")
data = file.readlines()
count = 0
for el in data:
    numbers = [int(i) for i in el.split()]
    srednee = sum(numbers) / len(numbers)
    zametnye = [c for c in numbers if c > srednee]
    zametnye_chet = [c for c in zametnye if c % 2 == 0]
    zametnye_nechet = [c for c in zametnye if c % 2 != 0]
    chet = [c for c in numbers if c % 2 == 0]
    nechet = [c for c in numbers if c % 2 != 0]
    if len(zametnye_chet) > len(zametnye_nechet) and sum(chet) < sum(nechet):
        count += 1
print(count)
