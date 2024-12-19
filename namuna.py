# from collections.abc import set_iterator
#
# set_a={1,2,3,4,5,6,7,8,9}
# set_iter=iter(set_a)
#
# print(next(set_iterator))
# from audioop import reverse
#
#
# class Person:
#     def __init__(self,strat, stop):
#         self.start=strat
#         self.stop=stop
#
#     def __iter__(self):
#         return self
#
#
#     def __next__(self):
#         self.list
#
#
#
#         if self.list<self.son:
#             return self.list
#         raise StopIteration
#
# for etim in Person(1,50):
#
#    reverse(etim)
# print(etim)
#
# def kvadratlar():
#     yield 1 ** 2
#     yield 2 ** 2
#     yield 3 ** 2
#     yield 4 ** 2
#     yield 5 ** 2
#
# kvadrat = kvadratlar()
#
# print(next(kvadrat))
# print(next(kvadrat))
# print(next(kvadrat))
# print(next(kvadrat))
# print(next(kvadrat))
#
#
# def yigindi_generator(a,b):
#    s = 0
#    for i in range( a, b,-1):
#        s+= i
#        yield s
#
# d=yigindi_generator(20,10)
# for item in d:
#     print(item)
#
#
# juft_4karrali_generator = (sana for sana in range(1,51) if sana % 4 ==0)
#
# for son in juft_4karrali_generator:
#     print(son)