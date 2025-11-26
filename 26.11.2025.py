# #название функций уникальны ( строятся как и переменнные
# def name_func(first_arg,*, second_arg):#функция  # * звездочка ограничивает все элементы после звездочки
#     #тело функции
#     for i in range(first_arg,second_arg):
#         print(i)
#     #конец тела функции

# name_func(10,15)#вызов функции
# def name_func_2(x, y,/):
#     print(x,y)
#     pass#ничего(заглушка)
# name_func_2(x=5, y=2)
# name_func_2(5,2)# можно c /

#кортеж - args
# def name_func_3(*args):
#     print(args)
# name_func_3(1,2,3,4,'23123')

#словарь - kwargs
# def name_func_4(**kwargs):
#     print(kwargs)
#     #для удаления использовать pop
# name_func_4(name1=1,name2=2)

# x=10#глобальная область видимости
# def local_func():
#     # global x
#     x=10
#     print(x)
#
#     return x,x,x #возвращаем значение
# print(local_func()[0]+25)
# print(x)

# def a():
#     x=10 #охватывающая область
#     def b():
#         # nonlocal x
#         x=5
#         print(x)
#     b()
#     print(x)
# a()

# type(x)==int -> isinstance(x,int)

def is_even(n):
    return n % 2 == 0
print(is_even(10))