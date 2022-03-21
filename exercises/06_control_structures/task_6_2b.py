# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
flag = False
while flag == False :
    try:
        ip = input('Введите адрес: ')
        list_ip = ip.split('.')
        check = 1/(4-len(list_ip))
        flag = False
    except (ZeroDivisionError) :
        flag = True
        try:
            first_octet = int(list_ip[0])
            for i in range(0,4):
                if int(list_ip[i]) > 255 or int(list_ip[i]) < 0:
                    flag = False
                    break
        except(ValueError):
            flag = False
    finally:
        if flag == False:
            print('Неправильный IP-адрес')       
        
if flag :
    if first_octet in range(1,224) :
        print ('unicast')
    elif first_octet in range(224,240) :
        print ('multicast')
    elif ip == '255.255.255.255' :
        print ('local broadcast')
    elif ip == '0.0.0.0' :
        print ('unassigned')
    else :
        print ('unused')
