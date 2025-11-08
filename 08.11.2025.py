# a=[10,2,1,10,1000,999,5,10,15,5]
# minim=1023952345778743598
# count=0
# for i in a:
#     if i<minim:
#         minim=i
#         count+=1
# print(minim,count-1)

# from random import randint
# a=[]
# for i in range(5):
#     a.append(randint(0,9))
#
# print(a)
# a[0],a[-1]=a[-1],a[0]
# print(a)

# nums=[1,2,3,4,5,6]
# s=int(sum(nums)/len(nums))
# for i in nums:
#     if s==i:
#         nums.remove(s)
# print(nums)

# a=[1,2,3,2,2395959,1383283832]
# k=[]
# for i in range (1,len(a)-1):
#     if a[i-1] < a[i] > a[i+1]:
#         k=[a[i],i]
#         break
# print(k[0],k[1],a.index(k[0]))

# a=input().split(' ')
# b=[]
# for i in a:
#     if i not in b and a.count(i)<2:
#         b.append(i)
# print(b)

# a=[2,4,2,9,8,3,4,2,1,9,3,2,8,5,9]
# b=0
# c=[]
# for i in range(len(a)):
#     s=[]
#     for j in range(i,len(a)):
#         if a[j] in s:
#             break
#         s.append(a[j])
#     if len(s)>b:
#         b=len(s)
#         c=s
# print(b,sum(c),c)