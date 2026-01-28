# def make_stats_tracker():
#     numbers=[]
#     total=0
#     def add(v):
#         nonlocal total
#         numbers.append(v)
#         # total+=v
#         print(f'добавлен новыйэлемент {v}')\
#         def maxim:
#             return max(numbers)
#         def minim():
#             return min(numbers)
#
#         def avg():
#             return sum(numbers)/len(numbers)
#
#         def get_stats():
#             return numbers
#
#     return add, get_stats, avg
# add_value,get_func_numbers=make_stats_tracker()
# add_value(1)
# print(get_func_numbers()) #не успел дописать

#без лога
# def add(a,b):
#     return a+b
# def mul(a,b):
#     return a*b

#с логом
# def add_with_logging(a,b):
#     result = add(a,b)
#     print(f'выполнилась функция add {a}+{b}={a+b}')
#     return result
# def mul_with_logging(a,b):
#     result = mul(a,b)
#     print(f'Выполнилась функция mul {a}*{b}={a + b}')
#     return result

# def create_logging_wraper(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         print(f'вызвана функция {func.__name__} с аргументом {args}, результат:{result}')
#         return result
#     return wrapper
# add_with_logging=create_logging_wraper(add)
# mul_with_logging=create_logging_wraper(mul)
# print(add_with_logging(1,2))
# print(mul_with_logging(1,2))

# add_with_loging(1,2)
#a=mul(2,2)

# @create_logging_wraper
# def add(a,b):
#     return a+b
# @create_logging_wraper
# def mul(a,b):
#     return a*b
# print(add(2,3))



# import time
# start = time.time()
# print(start)
# a=1+1
# end = time.time()
# print(end)
# print(end-start)


# from time import time
# def timeit_func(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result=(func([1,2,23,34]))
#         print(time()-start)
#         return result
#     return wrapper
# @timeit_func
# def add(nums:list=[]):
#     summ=0
#     for num in nums:
#         summ+=num
#     return summ
# @timeit_func
# def mull(nums:list=[]):
#     mull=1
#     for num in nums:
#         mull*=num
#     return mull
#
# a=mull([1,2,3,4,5])
# print(a)

# import time
# def lg_time(func):
#     @lg_time
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res=func(*args, **kwargs)
#         end = time.time()
#         print(f'Результат: {res}')
#         print(f'Время: {end-start}')
#         return res
#     return wrapper