# a=(1,1,1,1,1,2,2,2,3,1,2,2,3,3)
# count=1
# maxim=0
# for i in range (1,len(a)):
#     if a[i]==a[i-1]:
#         count+=1
#     else:
#         if maxim<count:
#             maxim=count
#         count=1
# print(maxim)

# cart = [("яблоки", 100), ("хлеб", 50), ("молоко", 80), ("яблоки", 100)]
# s=[]
# a=[]
# z=[]
# for item in cart:
#     if item[1]>70:
#         s.append(item)
#     a.append(item[1]*2)
# for item in set(cart):
#     g,h=item
#     z.append([g,h/2])
#
# print(a)
# print(s)
# print(z)

# books = [("Война и мир", 1865), ("1984", 1949), ("Гарри Поттер",1997), ("Война и мир", 1865)]
# a=[]
# z=[]
# c=[]
# for book in books:
#     if book[1]>1900:
#         a.append(book)
# for book in books:
#     z.append(book[1]-100)
# for book in books:
#     if book[1]>1950:
#         g,h=book
#         c.append(['Классика'+g,h])

# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
# three=math_students&physics_students&chemistry_students
# print(three)
# math=math_students-physics_students-chemistry_students
# print(math)
# mf=(math_students|physics_students)-chemistry_students
# print(mf)

