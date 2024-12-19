# # birinchi usul
# list bilan
# my_list=[1,2,3,4,5,6]
# my_list=iter(my_list)
# print(next(iter(my_list)))
# print(next(iter(my_list)))
# print(next(iter(my_list)))
# print(next(iter(my_list)))
# print(next(iter(my_list)))
# print(next(iter(my_list)))

# ikkinchi usul(birniki)

 # set bilan
# my_set = {1, 2, 3, 4, 5}
# my_iter = iter(my_set)
#
# print(next(my_iter))
# print(next(my_iter))




# 2-usul: o'z iterator yaratish
# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         self.current += 1
#         return self.current - 1
#
# my_iter = MyIterator(1, 5)
# for i in my_iter:
#     print(i)



# 3-usul: generator bilan
# def my_generator(start, end):
#     while start < end:
#         yield start
#         start += 1
#
# my_iter = my_generator(1, 10)
# for i in my_iter:
#     print(i)




# 4-usul: deque bilan
# from collections import deque
#
# my_deque = deque([1, 2, 3, 4, 5])
# my_iter = iter(my_deque)
# print(next(my_iter))
# print(next(my_iter))
#
