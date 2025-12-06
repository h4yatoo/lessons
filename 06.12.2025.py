# from random import randint
# d={'a':10,'b':20,'c':30}
# c={}
# c.update({
#     randint(100,999):d['a'],
#     randint(100,999):d['b'],
#     randint(100,999):d['c']})
# with open('test.txt','w+') as file:
#     for key,value in c.items():
#         file.write(str(key))+':'+str(value) + '\n'
#     with open('test.txt','r') as file:

# s='qwertyuiosdfghjklxcvbnm'
# import string
# print(string.punctuation)
# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# g=':'
# print(f'hello{g}world')

# from random import choice
# import string
# c=[]
# for i in range(100):
#     c.append(choice(string.ascii_uppercase)+choice(string.digits)+'\n')
# with open('test.txt','w+') as file:
#     file.writelines(''.join(c))
# with open('test.txt','r') as file:
#     for line in file:
#          if int(line[1])%2==0 and line[1]!='0':
#             print(line)
#             break
# with open('test.txt','r') as file:
#     coun=0
#     for j in file:
#         if j[0]=='A':
#             coun+=1
#     print(coun)

# from random import choice
# import string
# c=[]
# for i in range(150):
#     c.append(f'{choice(string.ascii_letters)}-{choice(string.digits)}\n')
# with open('test.txt','w+') as file:
#     file.writelines(''.join(c))
# with open('test.txt','r') as file:
#     cnt=0
#     for line in file:
#          if int(line[2])>5:
#             cnt+=1
#     print(cnt)
with open('903.txt','r') as file:
    cnt=0
    for line in file:
        numbers=line.split('\t')
        maxim = 0
        minim = 99999
        for i in numbers:
            if int(i) > maxim:
                maxim = int(i)
            if int(i) < minim:
                minim = int(i)



    #     if max(line)+min(line)<=int(line)-max(line)+min(line):
    #         cnt+=1
    # print(cnt)
















