# from time import time
# start = time()
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(10))
# print(time()-start)
#10->55


# from time import time
# start = time()
# s={}
# def fib(n):
#     if n in s:
#         return s[n]  ->мемоизация
#     if n < 2:
#         return n
#     result=fib(n-1) + fib(n-2)
#     s[n]=result   ->кеширование
#     return result
# print(fib(10))
# print(time()-start)

import time
# from functools import lru_cache
# import time
# @lru_cache()
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
# start=time.perf_counter()
# print(fib(999))
# end=time.perf_counter()
# print(end - start)

#стек - LIFO - Last In First Out - пирамида - он заменяет при добавлении первый, потом второй и тд

#очередь - FIFO - First In First Out - 0 1 2 3 4 - он заменяет при добавлении последний и тд

#библиотека - LFU - Least Frequensy Used - чаще всего > сохраняются, реже всего > удаляются  (кол-во, на сколько часто обращаются)

# LRU - Least Resently Used - наименее недавно использованный (время, самый старый удаляется)
# import sys
# sys.setrecursionlimit(10000)
# def F(n):
#     if n<5:
#         return n
#     return 2*n*F(n-4)
# print((F(13766)-9*F(13762))/F(13758))
# import sys
# sys.setrecursionlimit(10000)
# def F(n):
#     if n==1:
#         return 1
#     if n>1:
#         return 2*n*F(n-1)
# print((F(2024)//16-F(2023))/F(2022))

# from functools import lru_cache
# @lru_cache()
# def t(n):
#     if n<2:
#         return n
#     if n==2:
#         return 1
#     return t(n-1)+t(n-2)+t(n-3)
# print(t(10))

from functools import lru_cache
@lru_cache()
def s(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return s(n-1)+s(n-2)
print(s(100))

