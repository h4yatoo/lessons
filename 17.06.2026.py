#replace
# data='CBAAAABABCBAAABCBBAB'
# pairs=['AB','CB']
# for i in pairs:
#         data=data.replace(i,'*')
# for i in 'ABC':
#     data=data.replace(i,' ')
# data=data.split()
# print(len(max(data,key=len)))

#линейный способ
# data='CBAAAABABCBAAABCBBAB'
# pairs=['AB','CB']
# i=0
# cnt=0
# max_len=0
# while i<len(data)-1:
#     pair=data[i]+data[i+1]
#     if pair in pairs :
#         cnt+=1
#         i+=2
#         max_len=max(max_len,cnt)
#     else:
#         cnt = 0
#         i+=1

# print(max_len)


#window
# data='CBAAAABABCBAAABCBBAB'
# pairs=['AB','CB']
# l=r=0
# max_len=0
# while r<len(data)-1:
#     if data[r]+data[r+1] in pairs:
#         max_len=max(max_len,(r-l+1)//2)
#         r+=2
#     else:
#         l=r
#         r+=1
# print(max_len)

# data='CBAAAABABCBAAABCBBAB'
# pairs=['AB','CB']
# r=0
# breaks=[0]
# while r<len(data)-1:
#     if data[r] + data[r + 1] not in  pairs:
#         breaks.append(r)
#         r+=1
#     else:
#         r+=2
# breaks.append(len(data)-1)
# max_len=0
# for i in range(len(breaks)-1):
#     lenght=(breaks[i+1]-breaks[i]) // 2
#     max_len = max(max_len, lenght)
# print(max_len)

from string import digits, ascii_uppercase,printable
# alph=digits + ascii_uppercase


data='XZ1234AZZ'
g=digits + ascii_uppercase

# bad=g[16:]
# for i in bad:
#     data=data.replace(i,' ')
# data=data.split()
# print(len(max(data,key=len)))

good=g[1:16]
cnt=1
max_len=0
for i in good:
     data=data.replace(i,'*')
for i in range(1,len(data)):
    if data[i]==data[i-1]:
        cnt+=1
        max_len=max(max_len,cnt)
    else:
        cnt=1
print(max_len)








