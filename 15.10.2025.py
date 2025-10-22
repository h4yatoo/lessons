#пока условие
#бесконечный цикл если True
# while True:#while условие, например (a>10)
#     print('hello')

#for переменная in итерируемый объект
#list
#1:1
#3:3
#2:2
#string
#в переменную i записываются элементы посимвольно
#для каждой итерации цикл
#range (начало,конец,шаг)
#print(list(range(0,10)))
# for i in range(10):
#     print(i)

#break- останавливает выполнение цикла
#continue- останавливает итерацию цикла
# counter=0
# counter2=0
# while True:
#     counter +=1
#     if counter == 100:
#         break
#     if counter%3!=0:
#         counter2+=1
#         continue
#     print('наше значение:',counter)
# print('это число не кратное трех', counter2)

# a=[[1,2,3],[1,2,3],[1,2,3]]
# # for i in a:
# #     for j in i:
# #         print(j)
# #len(object) - возращает длинну object
# #a[-1] отрицательный индекс получет элемент с обратной стороны
# i=0
# j=0
# while  i<len(a):
#     while j<len(a[0]):
#         print(a[i][j])
#         j=j+1
#     i+=1

#1
# for i in range(0,11):
#     print(i)

#2
# a=int(input())
# for i in range(1,a):
#     print(i**2)

#3

# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)
# print('gotovo')

#4
# for i in range(1,16):
#     if i==10:
#         continue
#     print(i)
# else:
#     print('цикл завершен')




