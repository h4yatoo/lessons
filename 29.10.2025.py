
#math - библиотека для мат вычислений
#random - библиотека для генерации псевдослучайных чисел

# import math #импорттируем модуль (как коробку)
# from math import sqrt #импортируем инструмент from math
# import math as mth #меняем название модуля и импортируем

# import math
# print(math.sqrt(25))

# from math import pow,sqrt
# from math import * #* - все инстурменты из модуля
# print(pow(10,10))

# import math as mth
# print(mth.pow(10,10))

# from random import randint,choice # choice - рандомно выбирает эллемент
# index=(randint(1,5)) # от какого до какого числа сделать
# l=['a','b','c','d','e','f']
# print(l[index])



# a=input()
# print(a[int(len(a)/2):]+a[:int(len(a)/2)])

# a=input()
# j=a[::2]
# i=a[1::2]
# print(j+i[::-1])

# a=input()
# for i in range(len(a)-2):
#     print(a[i:i+3])



#a="шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс".split(", ")
# for i in a:
#     if i==i[::-1]:
#         print(i)


a=input()
setter=set(a)
b=max(a,key=a.count)
c=a.count(b)
print(b,c)
print(a[::3])
maxim=0
indexes=''
for i in setter:
    if a.count(i)==1:
        continue
    z=a.rfind(i)
    x=a.find(i)
    if z-x>maxim:
        maxim=z-x
        indexes=a[z:x]
    print(indexes)



