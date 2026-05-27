# from time import sleep
# def parent(func):
#     def retry(max_retries, delay):
#         for i in range(max_retries):
#             a=func()
#             print(f'попытка подключения: {i+1}')
#             if a:
#                 print('успешно')
#                 return True
#             print('переподключение')
#             sleep(delay)
#         return False
#     return retry
#
# @parent
# def test():
#     return False
# print(test(3,3))

# def recursion(num):
#     return recursion(num*2)

# school=[[['1','2','3','4','5'],['1','2','3','4','5'],['1','2','3','4','5']],[
#         ['1','2','3','4','5'],['1','2','3','4','5'],['1','2','3','4','5']]]
# summ=0
# def school_ref(school):
#     global summ
#     if len(school)==1:
#         summ+=1
#
#     for i in school:
#         return school_ref(i,summ)
#
# print(school_ref(school))

# a=[1,2,3,4,5,
# 6,7,8,9,10,
# 11,12,13,14,15]
# def rec(b):
#     # if type(b)==int:
#     #     return b+
#     if b==1:
#         return 1
#     return b + rec(b-1)
# g=rec(10)
# # print(g)
# def reverse_str(s):
#     result=''
#     for char in s:
#         result=char+result
#     return result
# def reverse_rec(s):
#     if len(s)<=1:
#         return s
#     return reverse_rec(s[1:])+s[0]
# print(reverse_rec('hello')
# from time import time
# def factor_r(s):
#     if s<=1:
#         return 1
#     return s*factor_r(s-1)
# s=250
# start=time()

#
# from time import time
# def factor_r2(s):
#     a=1
#     for i in range


