# s=input().split()
# a=[]
# for w in s:
#     a.append(w[::-1])
# print("Исходная строка: ",' '.join(s))
# print("Изменённая: ",' '.join(a))

#all - and
#any - or

# b=[10,20,30,40,50]
# a=[]
# for i in b:
#     a.append(i>0)
# print(all(a))

# b=['', 'hello', '', 'world']
# print(any(b))

#enumerate(последовательность, начальный индекс = 0)
# print(list(enumerate(['h','e','l','l'],start=0)))

# nums = [10, 25, 30, 15, 40, 5, 50]
# for i, value in enumerate(nums):
#     if value > 20:
#         print(i, value)

# words = ['python', 'java', 'c', 'javascript', 'go', 'rust', 'php']
# for i, word in enumerate(words):
#     if 'a' in word and len(word) > 3:
#         print(i, word)

# n=['alex','mary','ivan']
# a=[25,30,22]
# for n,a in zip(n,a):
#     print(f'{n}:{a}')

# students = ['Анна', 'Борис', 'Виктор']
# subjects = ['Математика', 'Физика', 'Химия']
# grades = [5, 4, 5]
# for student, subject, grade in zip(students, subjects, grades):
#     print(f' {student} - {subject} - {grade}')

# prices = [100, 200, 150, 300]
# discounts = [10, 15, 5, 20]
# for price, discount in zip(prices, discounts):
#     final_price = price - price * discount / 100
#     print(final_price)