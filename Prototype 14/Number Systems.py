# Перевод из 10 системы счисления в "N"

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
base = int(input("Система счисления: "))
number = int(input("Число: "))
while number > 0:
    result += alphabet[number % base]
    number //= base
result = result[::-1]
print(result)

# Перевод из "N" системы счисления в 10

base = int(input("Система счисления: "))
number = input("Число: ")
print(int(number, base))
