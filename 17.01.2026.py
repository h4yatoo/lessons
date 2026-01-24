#lambda аргументы: тело функции (выражение)
# a=lambda x: x**2 #только то что уместится в 1 строчку (типо ген и тд)
# print(a(3))

# numbers=[-1,2,-3,4,5]
# def dp(num):
#     if num>0:
#         return num*2
#     return num

# dp=lambda num: num*2 if num>0 else num
# posd=[dp(i) for i in numbers]
# print(posd)

# posd=list((lambda num: num*2 if num>0 else num)(number)for number in numbers)
# print(posd)

# dict_students=[{'name':'John','age':25,'grade':10},
#                {'name':'Michael','age':10,'grade':1},
#                {'name':'Keehl','age':30,'grade':4}]
# gname=lambda student: student.get('name')
# gage=lambda student: student.get('age')
# ggrade=lambda student: student.get('grade') if student.get('grade')>3 else None
# names=[gname(student) for student in dict_students]
# ages=[gage(student) for student in dict_students]
# grades=[ggrade(student) for student in dict_students if ggrade(student)]
# print(names)
# print(ages)
# print(grades)

# unstl=[5,4,3,2,1]
# print(sorted(unstl))

# unsts='ZV-bc-aA'
# print(sorted(unsts))

# unstd={4:'mary',
#        2:'ivan',
#        1:'jon',
#        3:'sarah'}
# print(sorted(unstd))

# word=['daniel','my','name']
# sorted_list = sorted(word,key=len)
# print(sorted_list)

# nums = [14,5,29,57,38]
# sort_nums=sorted(nums,key=lambda x: x%10)
# print(sort_nums)

# student=[('john',98),
#          ('jane',99),
#          ('sarah',97),
#          ('bob',85),]
# print(sorted(student, key=lambda x:x[1]))

# dict_students=[{'name':'John','age':25,'score':98},
#                {'name':'Michael','age':10,'score':77},
#                {'name':'Keehl','age':30,'score':92}]
# a=sorted(dict_students,reversed=True, key=lambda student: student['score'])


