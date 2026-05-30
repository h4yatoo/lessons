# def max_area(heights):
#     l=0
#     r=len(heights)-1
#     max_water=0
#     while l<r:
#         current=(r-l)*min(heights[l],heights[r])
#         max_water=max(max_water,current)
#         if heights[l]<heights[r]:
#             l+=1
#         else:
#             r-=1
#     return max_water
# print(max_area([1,8,6,2,5,4,8,3,7]))




# nums = [-4,-1,0,3,10]
# kvnums=[]
# for i in nums:
#     a=i**2
#     kvnums.append(a)
# print(sorted(kvnums))


nums=[2,3,1,2,4,3]
target = 7

def massiv(nums,target):
    l=0
    min_lenght=100000
    summ=0
    for r in range(len(nums)):
        summ+=nums[r]
        while l<=r and summ>=target:
            min_lenght=min(min_lenght,r-l+1)
            summ-=nums[l]
            l+=1
    return min_lenght if min_lenght!=100000 else 0


print(massiv(nums,target))



