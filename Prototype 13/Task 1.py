# Условие задания КИМ 13 (Умскул):
'''
В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети.
Адрес сети получается в результате применения поразрядной коньюнкции к заданному адресу узла и маске сети.
Сеть задана IP-адресом 231.168.192.142 и маской сети 255.255.255.240.
Сколько в этой сети IP-адресов, для которых сумма единиц в двоичной записи IP-адреса чётна?
В ответе укажите только число.
'''

from ipaddress import *

ip_net = ip_network("231.168.192.142/255.255.255.240", False)  # IP-адрес/Маска сети
answer = 0

for ip_add in ip_net:
    # 1 способ перевода в двоичную запись
    ip_add = f"{ip_add:b}"
    if ip_add.count("1") % 2 == 0:
        answer += 1
print(answer)

# Условие задания КИМ 13 (Умскул):
'''
В терминологии сетей ТСР/IP маской сети называют двоичное число, которое показывает,
какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети.
Адрес сети получается в результате применения поразрядной коньюнкции к заданному адресу узла и маске сети.
Сеть задана IP-адресом 192.168.32.176 и маской сети 255.255.255.240.
Сколько в этой сети IP-адресов, для которых сумма единиц в двоичной записи IР-адреса нечётна?
В ответе укажите только число.
'''

from ipaddress import *

ip_net = ip_network("192.168.32.176/255.255.255.240", False)
answer = 0

for ip_add in ip_net:
    # 2 способ перевода в двоичную запись
    ip_add = bin(int(ip_add))[2:]
    if ip_add.count("1") % 2 != 0:
        answer += 1
print(answer)
