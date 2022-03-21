# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input()
list_ip = ip.split('.')
if len(list_ip) == 4 :
    for i in range(4) :
        if list_ip[i].isdigit() :
            if int(list_ip[i]) in range(0,256) :
                flag = True
            else :
                flag = False
                break
        else :
            flag = False
            break
else : 
    flag = False
if flag == False :
    print('неправильный IP-адрес')
else:
    if int(ip.split('.')[0]) in range(1,223)  :
        print ('unicast')
    elif int(ip.split('.')[0]) in range(224,239) :
        print ('multicast')
    elif ip == '255.255.255.255' :
        print ('local broadcast')
    elif ip == '0.0.0.0' :
        print ('unassigned')
    else :
        print ('unused')