from timeit import timeit
# s='ab'*50000
# def count_func():
#     s.count('ab')
#     return s
#
# def srez_func():
#     cnt=0
#     for i in range(len(s)):
#         if s[i:i+2]=='ab'
#             cnt+=1
#     return cnt
#
# def split_func():
#     return len(s.split('ab'))
# print('count()',timeit.timeit('count_func()',number=100,globals=globals()))
# print('loop()',timeit.timeit('srez_func()',number=100,globals=globals()))
# print('split',timeit.timeit('split_func()',number=100,globals=globals()))


# s='a'*199996 +'abcde'
# def one():
#     'abcde' in s

# def two():
#     s.find('abcde')
#
#
# def three():
#     len(s.split('abcde')) >1
#
# def four():
#     for i in range(len(s)):
#         if s[i:i + 5] == 'abcde':
#             return True
# print('in()',timeit('one()',number=100,globals=globals()))
# print('find()',timeit('two()',number=100,globals=globals()))
# print('split',timeit('three()',number=100,globals=globals()))
# print('hand',timeit('four()',number=100,globals=globals()))


# nums=[1,3,5,6,5,123,2,5]
# target=5
# s=-1
# for i in range(len(nums)):
#     if nums[i]==target:
#         s=i
#         break
# print(s)

def find_target(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            l=m+1
        else:
            r=m-1
    return -1











