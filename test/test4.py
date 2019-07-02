####### LIST SET DICTIONARY COMPREHENSIONS (REMOVE THE COMENT TO RUN THIS BLOCK PROGRAM)
#
# list = []
# for i in range(10):                         #inset value to list using loop
#     result = i
#     list.append(result)
# print (list)
# list2 = [x for x in range(10)]              # another way to insert value using loop
# print(list2)
#
#
# print ("=================this is set===================")
# set = {x for x in range(5)}
# print(set)
# print(type(set))
#
# print ("===============this is Dictionary=============")
# dict = {z : z for z in range(15)}
# print(dict)
# print(type(dict))

####### LAMBDA FUNCTION (REMOVE THE COMENT TO RUN THIS BLOCK PROGRAM)
####simple example
# a = lambda e : print(e)
# print(a)
# print(type(a))
# angka = a(5)
# print(angka)

####### MAP() AND FILTER()(REMOVE THE COMENT TO RUN THIS BLOCK PROGRAM)
# def production10(a):
#     return a * 10
#
# r1 = range(10)
# maps = map(production10,r1)
# listmaps = list(map(production10,r1))
# print(maps,"\n", listmaps)
#
# list(filter((lambda a: a>5),r1))                        #using filter function

####### ITERATORS, GENERATORS AND DECORATORS(REMOVE THE COMENT TO RUN THIS BLOCK PROGRAM)
print("===============iterators===============")
my_list = [1,2,3,4,5,6]
# for element in my_list:
#     print(element)
#
# my_iter = iter(my_list)
# print(type(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))                        # value must be stop in here because out of the iteration

print("===============generators===============")
#
# def my_gen(x, y):
#     for i in range(x):
#         print("x is", x)
#         print ("i is", i)
#         print("y is ", y)
#         print("i+y =" )
#         yield i + y                            #yield is return value when using generators
#
# my_object= my_gen(2, 4)
# print(type(my_object))
# print(next(my_object))
# print(next(my_object))                         # the generators stop in here
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))
# print(next(my_object))

print("============Decorators=========")
# def my_decorator(target_function):
#     def function_wrapper():
#         return "ini adalah fungsi tetap dan " + target_function() + "Python"
#     return function_wrapper()
#
# @my_decorator
# def target_function():
#     return "ini adalah function tambahan di "
#
# a = target_function
# print(a)


####### THEREDING(REMOVE THE COMENT TO RUN THIS BLOCK PROGRAM)
# import threading
# import time
#
# def myfunction():
#     print ("start a thread")
#     time.sleep(3)
#     print("End a thread")
#
# threads = []
#
# for i in range(5):              #runs 5 concurrent sessions of myfunction()
#     th = threading.Thread(target = myfunction)
#     th.start()
#     threads.append(th)
#
# for th in threads:
#     th.join()
#
#
# for i in range(5):              #this command will be print one by one threading using sleep time after print one thread
#     myfunction()