# 1







# 2
# with open('access.txt.txt') as f:
#     lines = f.readlines()
# logi=[]
# for line in lines:
#     a=line.split()
#     c=a[0]
#     s=a[-1]
#     logi.append((c,s))
# c_200=[]
# c_401=[]
# c_403=[]
# c_404=[]
# c_500=[]
# for c,s in logi:
#     if s=='200':
#         c_200.append(c)
#     elif s=='401':
#         c_401.append(c)
#     elif s=='403':
#         c_403.append(c)
#     elif s=='404':
#         c_404.append(c)
#     elif s=='500':
#         c_500.append(c)
# print('Код 200:', c_200)
# print('Код 401:', c_401)
# print('Код 403:', c_403)
# print('Код 404:', c_404)
# print('Код 500:', c_500)   #я мог принты через словарь списков и цикл, но не хотел ковыряться

# 3
# with open("triples.txt") as f:
#     lines = f.readlines()
# s=[]
# for line in lines:
#     s.append(int(line.strip()))
# cnt = 0
# for i in range(len(s) - 2):
#     a = s[i]
#     b = s[i + 1]
#     c = s[i + 2]
#     min_val = min(a, b, c)
#     if (a % 5 == min_val) or (b % 5 == min_val) or (c % 5 == min_val):
#         cnt += 1
# print("Количество троек:", cnt)

# def log_action(func):
#     def wrapper(*args):
#         print(f'выполняется {func.__name__}')
#         result = func(*args)
#         print(f'функция {func.__name__} завершена')
#         return result
#     return wrapper
# @log_action
# def read_sales():
#     with open('transactions.txt',encoding='utf-8') as f:
#         s=[]
#         for line in f:
#             a=line.split(',')
#             print(a[0],a[1],a[2])
#             s.append((a[0],a[1],a[2].strip('\n')))
#     return s
# @log_action
# def get_total_by_category(category):
#     with open('transactions.txt', encoding='utf-8') as f:
#         s=0
#         for line in f:
#             a = line.split(',')
#             if a[1]==category:
#                 s+=float(a[2].strip('\n'))
#     return s
# @log_action
# def get_average_sale():
#     with open('transactions.txt', encoding='utf-8') as f:   #я запутался

