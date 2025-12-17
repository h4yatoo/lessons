# a,b,c=input().split()   1
# print('Значение переменной a:',a)
# print('Значение переменной b:',b)
# print('Значение переменной c:',c)

# a,b,c,d=map(int,input().split())   2
# print(a+c,b+d)

# a=input()   3
# b=1
# for i in a:
#     b*=int(i)

# a=input().split()   4
# s=int(a[0])
# b=int(a[1])
# f1=s+b*3
# f2=b-s%2
# print('Первое число:',f1)
# print('Второе число:',f2)

# a=int(input())    5
# if a%2!=0:
#     print('Удвоенное число:',a*2)
# elif a%2==0:
#     print('Число без изменений:',a)

# a=int(input())   5
# b1=a//100
# b2=a%10
# if b2%2!=0 or b1%2==0:
#     a=a+1
# elif b2==3 or b2==7 or b2==9:
#     a =a-1
# print(a)

# x=int(input())    7
# if x>0:
#     y=3*x+1
# elif x==0:
#     y=x
# else:
#     y=x*x+2
# print(y)

# a=input()    8
# b=int(a,16)
# d=bin(b)[2:]
# print('Введённое число в двоичной СС:',d)
# print('Количество единиц:',d.count('1'))

# a=(input())    9
# s1=int(a[0])
# s2=int(a[1])
# s3=int(a[2])
# s4=int(a[3])
# s5=int(a[4])
# print('Введённое число:',a)
# print('Сумма всех разрядов:',s1+s2+s3+s4+s5)

# s=input().split()   11
# a=[]
# for w in s:
#     a.append(w[::-1])
# print("Исходная строка: ",s)
# print("Изменённая: ",a)

# nums=list(map(int,input().split()))    13
# b=[]
# for n in nums:
#     if n%2==0:
#         b.append(n)
# print("Список:",nums)
# print("Только чётные числа:",b)
# print("Сумма всех оставшихся:",sum(b))

# list_1=[1,2,3,4,2,3,4,6,8]     16
# list_2=list(map(int,input().split()))
# s=[]
# for i in list_1:
#     if i in list_2 and i not in s:
#         s.append(i)
# print(tuple(s))

# words=input().split()     17
# d={}
# for w in words:
#     d[w]=len(w)
# print("Словарь:",d)
# print("Список:",words)
asd



















