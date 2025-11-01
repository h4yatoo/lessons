# a=input()
# if not(a.isalpha()):
#     print(a.upper())
# if not(a.isalnum()):
#     print(a.replace(' ','*'))
# else:
#     print(a)

# a=input()
# b='aeiuoyAEUIOY'
# alp=''
# maxim=0
# for i in b:
#     nex_maxim=a.rfind(i)
#     if maxim<nex_maxim:
#         maxim=nex_maxim
#         alp=i
# print(maxim,alp)

# a='abcd defg ghij'
# a=a.replace(' ','')
# for i in a:
#     if a.count(i)>1:
#         a=a.replace(i,'')
# print(a)

# from random import choice
# a=input()
# k=[' ', ',', '.','!', '?', ':', ';']
# while a!='':
#     s=choice(a)
#     a.replace('s','')
#     print(d)

a=input()
k='АВЕКМНОРСТУХ'
if len(a)==6:
    numbers=a[1:4]
    alpha=a[:1]+a[4:]
    print(numbers.isdigit() and alpha[0] in k and alpha[1] in k and alpha[2] in k)
else:
    ('false')




