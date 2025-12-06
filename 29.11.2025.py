# def d(n):
#     s=n.count('.')+n.count('?')+n.count('!')
#     w=len(n.split(' '))
#     sy=len(n)
#     return (s,w,sy)
# print(d('hello.hello!'))

# def calculate_area(shape='rectangle', length=0, width=0, radius=0):
#     if shape == 'rectangle':
#         return length * width
#     elif shape == 'circle':
#         return 3.14 * radius**2

# def format_name(first, last, middle="", title=""):
#     s=[]
#     if title:
#         s.append(title)
#     if first:
#         s.append(first)
#     if last:
#         s.append(last)
#     if middle:
#         s.append(middle)
#     return " ".join(s)

def a(*args):
    b=list(set(args))
    return b
