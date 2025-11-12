# values=(1,2,3,4,5)
# x=1
# y=2
# x,y=y,x
# s0,*s2,s3=values
# print(s0,s2,s3)
#
# s=(1,2,3)
# s1=(4,5)
# print(*s,*s1)
# s3=(*s,*s1)
# print(s3)
#
#
# next_tuple=(1,(2,3,4),5)
# s1,(s2,*s4),s3=next_tuple
# print(s4)
# s=((1,2),(3,4),(5,6))
# for i,j in s:#подчиняется правилам распаковки
#     print(i,'+',j,'=',i + j)
#
# next=[([1,2],3),['xy',6]]
# # ([s,s1],s2),[s3,s4]=next
# # print(s,s1,s2,s3,s4)
# for ((i,b),j) in next:
#     print(i,b,j)
#
# #set - {} уникализирует последовательность и тд
# a={1,2,3,4,5,6}
# b=[1,2,3,5]
# print(set(b))
# print(a)
#
# s={(1,2),(3,4)}
# # s={[1,2],[3,4]} - error
# print(s)
#
# s.add((5,6))#добавление элемента во множество
# print(s)
#
# s.remove((1,2))#удаление элемента множества
# print(s)

# a=(1,2,3)
# s,s1,s2 = a
# print(s,s1,s2)

# a=input().split()
# a=(tuple(a))

# a=(1,2,3,4)
# b=(5,6,7,8)
# c=()
# for i in range (len(a)):
#     c+=(a[i]+b[i],)
# print(c)

a=input()
b=set(a)
print(b,len(b))
if len(b)<len(a):
    print('есть повтор')
else:
    print('нет повтор')
