#это первый созданный комментарий asdds

#int - целочисленный тип данных
# a=10
# print(type(a)) # type(obj) - выводит тип данных объекта
# float - число с точкой
# a=10.23
# print(type(a))
#str - строковый тип данных
# a='awsd'
# print(type(a))
#bool - логический тип 0/1 или True/False
# a=True
# print(type(a))
#list - список
# a=[1,2,3]
# print(type(a))

#set - набор уникальных значений (в фигурных скобочках{})
# a={1,2,3,4,5,6,6}
# print(type(a),a)
#tuple - кортеж (набор неизменяемых данных)
# a=(1,2,3,4,5)
# print(type(a),a)
#dict - словарь с элементами ключь: значение
# a={'a':1234}
# print(type(a))

# a=10
# print(a,a,a,a,sep='')
#sep - разделитель при выводе


#a=input()#input - возвращает введенную в консоли str строку
#print(a)

#a=int(input())#перевод из str v int
#print(a+1)


#a=list('hello world')
#print(a)

#a=int(float(input()))
#print(a+1)

#a='\tPrivet\ndrug'#\t - отступ на 4 пробела или 1 таб \n - переход на новую строку
#print(a)

#все элементы начинаются с 0
# a=[1,2,3]
# b='abcd'
# c=(1,2,3)
# print(c[0])
# c=list(c)
# c[0]=10
# print(c[0])

# Задача1
# a={'Имя':'Иван', 'Фамилия':'Иванов', 'Возраст':17, 'Класс':'11A'}
# print(a)


# Задача2
# a=45
# b=str(a)
# print('Число в строке:',b)

#Задача 3
# a='asd'
# b='wqwe'
# c='ghj'
# print(a,b,c,sep=',')


#Задача 4
# a='\tПривет, \nFuture step'
# print(a)


#Задача 5
# a,b=int(float(input())),int(float(input()))
# print(a+b)


# a=input()
# b=a.split(' ')#делит строку по разделителю, возварщает list
# c=int(float(b[0]))
# d=int(float(b[1]))
# print(c+d)


#+ складывает
# - вычитает
# / делит
# * умножает
#% остаток от деления
# // челочисленное деление
# () объединение
# ** возведение в степень

# #and - логическое и
# print(True and 1)
# #or - логическое или
# print(1 or 0)
# #not - не
# print(not(True))
#
# #числа и объекты
# #== - сравнение (эквиваленность)
# print(1==1)
# #!= - сравнение (отрицание)
# print(5!=5)
#
# #числа
# #>= <= < >
# print(10>=10)

# a=bool(input('Идет ли дождь?:'))
# if a:
#     print('Да идет')

# a=input('Идет ли дождь?:')
# if a=='yes':
#     print('Да идет')
# elif a=='no':
#     print('нет, не идет')
# else:
#     print('МБ не МБ да')
# a=input('Введите слово:')
# match a:
#     case 'no':
#         print('why no')
#     case 'yes':
#         print('why yes')
#     case _:
#         print(' any 23')

#Задача 1
# a=int(input())
# if a%2==0:
#     print('Четное')
# else:
#     print('Нечетное')

#Задача 2
# a=int(input())
# if a>0 and a%2==0:
#     print('Положительное и четное')
# elif a > 0 and a % 2 == 1:
#     print('Положительное и нечетное')
# elif a>0 and a%10==0:
#     print('Положительное и оканчивается на 0')
# elif a<0:
#     print('Отрицательное')

#Задача 3
# a=int(input())
# if a%3==0 and a%5==0:
#     print('FizzBuzz')
# elif a%3:
#     print('Fizz')
# elif a%5:
#     print('Buzz')
# else:
#     print('a')

