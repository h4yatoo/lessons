# s=input()
# a=s.split(',')
# for i in a:
#     print(i.strip())
# b=''
# for i in s:
#     if i.isdigit():
#         b+=i
# print(b)
import numbers

# nums=list(map(int,input().split()))
# b=[]
# s=False
# for n in nums:
#     if not(n%13==0 and n%2==0):
#          b.append(n)
#     else:
#         s=True
#         break
# if not s:
#     print('нету')
# else:
#     print(sum(b))

# nums=list(map(int,input().split()))
# b=[]
# for n in nums:
#     if nums.index(n)%2==0:
#         b.append(n)
# print(nums)
# print(nums.index(min(nums)))
# print(b)
# nums.remove(max(nums))
# print(nums)
# print(sorted(nums,reverse=True))

# list_1=[1,2,3,4,2,3,4,6,8]
# list_2=list(map(int,input().split()))
# print(tuple((set(list_1)).intersection(list_2)))

s=input()
f=''
for i in s:
    if 'A'<=i<='Z':
        f+=chr(ord(i)+32)
    else:
        f+=i
print(f)


