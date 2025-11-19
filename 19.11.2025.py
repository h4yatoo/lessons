# d={'key1':'value'}
# print('key2' not in d)
# d['key2']=1000
# d['key1']=10
# print(d)

# d={"key1":"value1","key2":"value2"}
# for i in d:
#     print(i)

# d={"key1":"value1","key2":"value2"}
# print(list(d.items()))#получает все элементы словаря как список кортежей
# for i,j in d.items():
#     print(i,j)

# print(list(d.values()))#возвращает список значений

# print(list(d.keys()))#список ключей

# print(d.get("key3",10))#get(key, value if not exists

# print(d.pop("key3",10),d)#удаляет элемент и возвращает значение

# print(d.popitem())#удаляет и возвращает последний элемент

# d.update({"key3":"value3"})
# print(d)

# d.clear()#удаляет все элементы

# d={"key1":"value1","key2":"value2"}
# a=d
# a=d.copy()#создает копию элемента в памяти
# a["key3"]="value100"
# print(d,a)

# keys=['key1', 'key2', 'key3']
# new_dict=dict.fromkeys(keys,'value')
# print(new_dict)

# d={}
# d['name']='alica'
# print(d)

# k={'x':10}
# print(k.get('y'),10)

# books = {"романы": 10, "детективы": 5}
# books.update({'фантастика':'8'})
# print(books)

# marks = {"Информатика": 5,"Математика":5,"Русский":3, "История":4, "Физика":4}
# sr=sum(marks.values())/len(marks)
# print(sr)

# a=input().split()
# s={}
# for i in a:
#     key,value=i.split(':')
#     s[key]=int(value)
# print(s)

students = ["Анна", 5, "Борис", 4, "Вера", 5]
s={}
for i in range(0,len(students),2):
    a=students[i]
    b=students[i+1]
    s[a]=b
print(s)