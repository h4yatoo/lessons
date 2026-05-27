# def make_string_builder():
#     result=''
#     def a(b):
#         nonlocal result
#         result+=b+' '
#         return result
#     return a
# d=make_string_builder()
# print(d('hi'))
# print(d('hi'))
# print(d('hi'))

# def make_product_accumulator():
#     s=['1']
#     def a(b):
#         nonlocal s
#         s*=b
#         return s
#     return a
# d=make_product_accumulator()
# print(d(8))
