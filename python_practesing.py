# # 1. Не используя библиотеки для парсинга,
# # распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # path = '(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)'
# # r = requests.get(path)
# # print(r.text)
# # soup = (BeautifulSoup(r.text,'lxml'))
# # soup.find('<remote_addr>').find('<request_type>').find('<requested_resource>')
# #
# # data = []
# # data.append([soup.find])





# задание 3
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби : (hobby.csv)
# скалолазание,охота
# горные лыжи

# //создала 2 отдельных файла
#
# //users.csv
# //names = [Иванов Иван Иванович','Петров Петр Петрович']
#
# //hobby.csv
# //hobby = ['скалолазание,охота','горные лыжи']


import json

# file1 = open('users.csv', 'r', encoding='UTF-8')
# data1 = file1.read()
# a = print(data1)
#
# file1.close()
#
# file2 = open('hobby.csv', 'r', encoding='UTF-8')
# data2 = file2.read()
# b = print(data2)
# file2.close()
#
# x = dict(list(a.items()) + list(b.items()))
# print(x)


###2й вариант
# contents = []
# json_dir_name1 = "users.csv"
# json_dir_name2 = "hobby.csv"
#
# json_pattern = json.join(json_dir_name1,json_dir_name2)
#
# for file in json_pattern:
#   contents.append(read(file))






# generators
import random


#
# a = [random.randint(-10,10) for i in range(10)]
# print(a)
# b = [elem for elem in a if elem%2==0]
# print(b)
#

# с помощбю генератора выведем 10  списков из 6 едениц
# n = 10
# m = 6
#
# a = [[1]*6 for i in range(n)]
# for i in a:
#     print(i)


# a = [1,2,3,4,5]
# b = iter(a)
# print(next(b))


# найдем факториал при помощи функции.
# Памяти тут занимается больше чем в генераторе
# def fact(n):
#     pr = 1
#     a = []
#     for i in range(1, n+1):
#         pr = pr*i
#         a.append(pr)
#     return a
#
# print(fact(5)) ##[1, 2, 6, 24, 120]



# # найдем факториал при помощи генератора.
# def factorial(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr = pr*i
#         yield pr
# #вместо того чтобы создавать новое значение и присваивать ей число факториала ,
# # а потои писать 5 раз next
# for i in factorial(5):
#     print(i, end= ' ')
#


#
# a = ['Aishat','the','best']
# v = sorted(a,reverse=False)
# print(v)
# # b = list(map(len,a))
# # print(b)
#
# # # получим наоборот
# c = list(map(lambda x: x[::-1],a))
# print(c)

# тоже самое только генератором
# s = [i[::-1] for i in a]
# print(s)

# y = [10,20,30,40,500,600,70,800,900,100000]
# def s(i):
#     return i%100  #т.е выбирает по возрастаию у кого 2 нуля
# print(sorted(y, key = s))



# c = list(map(int, input().split()))
# print(c)

# a = [2,[],'hello']
# # s = list(filter(bool,a)) # [2, 'hello']
# # s = list(map(bool,a)) #[True, False, True]
# # print(s)
#
# d = 'hshsjsksol788789329xz'
# n = list(filter(str.isdigit, d))
# print(n) # ['7', '8', '8', '7', '8', '9', '3', '2', '9']
# m = list(filter(str.isalpha,d)) # ['h', 's', 'h', 's', 'j', 's', 'k', 's', 'o', 'l', 'x', 'z']
#

# print(m)

# mbt = {
#        'abdurahman': 'director',
#        'Rustamhan':  'syetolog',
#        'h': 40,
#        'k': 33
# }
#
# # g = list(filter(lambda x: mbt[x] > 20, mbt))
# # print(g)
# o = list(filter(lambda x:  x , mbt))
# print(o)

#
# r = [12,34,5,65,79,18]
# def ostatok(x):
#     return x%13
# print(sorted(r, key = ostatok)) #[65, 79, 5, 18, 34, 12] как???

# отсортировать список по возостанию цифр
# o = ['trerr 4', 'njfvhu 9', 'oooo 9','aaaaa 1','AAAA 0']
# print(sorted(o, key=lambda x: int(x.split()[1]) )
#
# print(sorted(o, key=lambda x: (int(x.split()[1]), x.split()[0].lower()) )) #в лямбде можно передавать только одну()



a = list(range(1,20))
print(a)
del a[3::4] ##### [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19]
print(a)