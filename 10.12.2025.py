# with open('902.txt','r')  as f:
#     counter = 0
#     s=[]
#     for line in f:
#         s=line.split()
#         for i in s:
#             s.append(int(i))
#         s=sorted(s)
#         counter_amount=0
#         for i in range(len(s)):
#             counter_cash=-1
#             for j in range(len(s)):
#                 if s[i]==s[j]:
#                     counter_cash+=1
#             if counter_cash>1:
#                 counter_amount+=1
#             if counter_amount!=1:
#         if s[-1]>sum(s[:-1]) and counter_amount==1:
#             counter += 1

# with open('903.txt','r') as file:
#     amount_lines=0
#     cnt=0
#     for line in file:
#         numbers=line.split('\t')
#         s=[]
#         for i in numbers:
#             s.append(int(i))
#         first=[]
#         second=[]
#         for i in s:
#             if s.count(i)!=1:
#                 first.append(i)
#                 continue
#             second.append(i)
#         if len(set(s)) == 4 and sum(first)**2 > sum(second)**2:
#             amount_lines+=1
#         print(amount_lines)

# with open('905.txt','r') as file:
#     amount_lines=0
#     for line in file:
#         numbers=line.split('\t')
#         s=[]
#         for i in numbers:
#             s.append(int(i))
#         f=[]
#         sd=[]
#         for i in s:
#             if s.count(i)!=1:
#                 f.append(i)
#                 continue
#             sd.append(i)
#             a=sorted(set(f))
#         if len(set(s))==3 and f[-1]>sd:
#             amount_lines+=1
#     print(amount_lines)




