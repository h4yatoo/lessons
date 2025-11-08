# from random import randint
# a=[randint(1,100),randint(1,100),randint(1,100),randint(1,100)]
# maxim=0
# minim=1000000
# for i in a:
#     if i>maxim:
#         maxim=i
#     if minim>i:
#         minim=i
# print(a,maxim,minim)

# s=input().strip()
# count=0
# les_s=len(s)
# for i in range(les_s):
#     for j in range(i+1,les_s):
#         if s[i] == s[j] and j - i > 1:
#             count+=1
# print(count)

# a=[1,2,3]
# iterator=iter(a)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# k=[1,2,3]
# k[0]=0
# for i in range (0,len(k)):
#     k[i]+=1
# print(k)

# k=[1,2,3]
# l=[4,5,6]
# #z=k+l
# k.extend(l) # расширяет один объект другим
# print(k)

# from random import randint
# k=[]
# for i in range(5000):
#     #добавляется новый элемент в конец списка
#     k.append(randint(0,100))
# print(k)

# k=['раз', 'три']
# j='два'
# k.insert(1,j) #всталяет перед необходимым индексом значение
# print(k)

# k=[1,2,3,4,5,2,6,7,8,9,10,11,12,13,14,15]
# k.remove(2) #удаляет первый найденный запрашиваемый элемент
# print(k)

# k=[1,2,3,4,5]
# k.clear() # чистит список
# print(k)

# k=[1,2,3,4,2,5]
# k.pop(4) # удаляет элемент по индексу
# print(k)

# k=[5,4,3,2,1,2,3,4,5]
# k=['a','n','c','d','e','f','g','h']
# #k.sort()
# k.sort(reverse=False) # переворачивает список
# print(k)

# k=[1,2,3,4,5]
# print(max(k))
# print(min(k))
# print(sum(k))

# k=[1,2,3,4,5]
# for i in k:
#     print(i*2)

# k=[1,2,3,4,5]
# iterator=iter(k)
# counter=0
# for i in range(len(k)):
#     s=next(iterator)
#     counter+=s
#     print(counter)

# k=[1,2,3,4,5]
# l=[6,7,8,9,10]
# for i in range (len(k)):
#     print(k[i]+l[i],end=" ")

# a=['asd','asdgsgsg','hello','homeassistant']
# for i in a:
#     count=0
#     for j in i:
#         count+=1
#     if count%2==0:
#         print(i)

from random import randint
s=randint(1,100000)
for _ in str(s):print('разряд')


