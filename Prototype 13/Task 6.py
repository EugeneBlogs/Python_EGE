# Условие задания КИМ 13 (Умскул):
'''
В терминологии сетей ТСР/IP маской сети называется двоичное число, определяющее,
какая часть IР-адреса узла сети относится к адресу сети, а какая - к адресу самого узла в этой сети.
При этом в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места - нули.
Обычно маска записывается по тем же правилам, что и ІР-адрес, - в виде четырёх байтов,
причём каждый байт записывается в виде десятичного числа.
Адрес сети получается в результате применения поразрядной коньюнкции к заданному IP-адресу узла и маске.
Для узла с IP-адресом 244.55.138.100 адрес сети равен 244.55.138.96.
Чему равно наименьшее значение последнего (самого правого) байта маски?
Ответ запишите в виде десятичного числа.
'''

from ipaddress import *

ip_add = ip_address("244.55.138.100")
for mask in range(33):
    try:  # Пробуем создать сеть (нужно обработать ошибку, которая может возникнуть)
        ip_net = ip_network(f"244.55.138.96/{mask}")
        if ip_add in ip_net:
            # Выводим последний минимальный байт (делим для этого по точке маску сети)
            print(str(ip_net.netmask).split(".")[-1])
            break
    except:
        continue  # При ошибке - просто пропускаем данное значение и идём дальше

# Условие задания КИМ 13 (Умскул):
'''
В терминологии сетей ТСР/IP маской сети называется двоичное число, определяющее,
какая часть IР-адреса узла сети относится к адресу сети, а какая - к адресу самого узла в этой сети.
При этом в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места - нули.
Обычно маска записывается по тем же правилам, что и ІР-адрес, - в виде четырёх байтов,
причём каждый байт записывается в виде десятичного числа.
Адрес сети получается в результате применения поразрядной коньюнкции к заданному IP-адресу узла и маске.
Для узла с IP-адресом 244.55.138.100 адрес сети равен 240.0.0.0.
Чему равно максимально возможное значение первого (самого левого) байта маски?
Ответ запишите в виде десятичного числа.
'''

from ipaddress import *

ip_add = ip_address("244.55.138.100")
for mask in range(32, -1, -1): # Максимальное, поэтому идём в обратную сторону
    try:
        ip_net = ip_network(f"240.0.0.0/{mask}")
        if ip_add in ip_net:
            print(str(ip_net.netmask).split(".")[0])
            break
    except:
        continue

# Условие задания КИМ 13 (Умскул):
'''
В терминологии сетей TCP/IP маска сети - это двоичное число, меньшее 2^32;
в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места нули.
Маска определяет, какая часть IP-адреса узла сети относится к адресу сети,
а какая - к адресу самого узла в этой сети. Обычно маска записывается по тем же правилам,
что и IP-адрес - в виде четырёх байт, причём каждый байт записывается в виде десятичного числа.
Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла
и маске.
Для узла с IP-адресом 42.118.219.133 адрес сети равен 42.118.216.0.
Каково наибольшее возможное количество единиц в разрядах маски?
'''

from ipaddress import *

ip_add = ip_address("42.118.219.133")
for mask in range(32, -1,- 1):
    try:
        ip_net = ip_network(f"42.118.216.0/{mask}")
        if ip_add in ip_net:
            print(bin(int(ip_net.netmask)).count("1"))
            break
    except:
        continue

# Условие задания КИМ 13 (Умскул):
'''
В терминологии сетей TCP/IP маска сети - это двоичное число, меньшее 2^32;
в маске сначала (в старших разрядах) стоят единицы, а затем с некоторого места нули.
Маска определяет, какая часть IP-адреса узла сети относится к адресу сети,
а какая - к адресу самого узла в этой сети. Обычно маска записывается по тем же правилам,
что и IP-адрес - в виде четырёх байт, причём каждый байт записывается в виде десятичного числа.
Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла
и маске. Например, если IP-адрес узла равен 231.32.255.131, а маска равна 255.255.240.0,
то адрес сети равен 231.32.240.0.
Для узла с IP-адресом 148.228.120.242 адрес сети равен 148.228.112.0.
Чему равен третий слева байт маски? Ответ запишите в виде десятичного числа.
'''

from ipaddress import *

ip_add = ip_address("148.228.120.242")
for mask in range(33):
    try:
        ip_net = ip_network(f"148.228.112.0/{mask}")
        if ip_add in ip_net:
            print(str(ip_net.netmask).split(".")[-2])
    except:
        continue

# Условие задания КИМ 13 (Умскул):
'''
Два узла, находящиеся в одной сети, имеют IP-адреса 121.171.15.70 и 121.171.3.68.
Укажите наибольшее возможное значение третьего слева байта маски сети.
Ответ запишите в виде десятичного числа.
'''

'''
Третий байт первого IP-адреса равен 15 (10 сс) = 00001111 (2 сс),
а третий байт второго IP-адреса 3 (10 сс) = 00000011 (2 сс).
Максимально совпадают старшие четыре бита. Значит наибольшее значение третьего байта маски сети может быть
11110000 (2 сс) = 240 (10 сс).

Ответ: 240.
.
'''