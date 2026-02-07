#одновреммено/функции
import asyncio


# def a():
#     print('hello')
# a()
# print('world')
# процессы (ресурсы / память / соединения) ->
# потоки -> (ресурсы от процесса / быстрее создаюся и преключаются / могут обмениваться данными)


#конкурентность
#важность процессов ->
#сварить макароны - пожарить мясо
#варить макароны 4мин
#пожарить мясо 4мин
#8минут

#варить макароны - 2мин
#пожарить мясо в течении макарон -> (3мин)

#параллелизм


# import asyncio
# # # async with
# # # async for
# # async def f():
# #     print('hello')
# #     await asyncio.sleep(1)
# #     print('world')
# # asyncio.run(f())
#
# async def one():
#     print('f_1 start')
#     await asyncio.sleep(20999)
#     print('f_1 end')
#
# async def two():
#     print('f_2 start')
#     await asyncio.sleep(2)
#     print('f_2 end')
#
# async def main():
#     task1 = asyncio.create_task(one())
#     task2 = asyncio.create_task(two())
#     # while True:
#     #     await asyncio.sleep(1)
#     #     task1.cancel()
#     # result = await asyncio.gather(task1, task2)
#     # await one()
#     # await two()
#
# asyncio.run(main())
# import time
# start=time.time()
# import asyncio
# async def make_coffee():
#     print("Making coffee")
#     await asyncio.sleep(2)
#     print("Coffee is ready")
# async def make_toast():
#     print("Making toast")
#     await asyncio.sleep(2)
#     print("Toast is ready")
# async def main():
#     await make_coffee()
#     await make_toast()
# end = time.time()
# asyncio.run(main())
# print(f'время:{end - start}')