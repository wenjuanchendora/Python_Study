# 裴波那切数列

# num = int(input("请输入你要获得的数列元素个数："))
# n1 = 0
# n2 = 1
# counter = 2

# if num == 0:
#     print("输入值不合法")
# elif num == 1:
#     print(n1)
# else:
#     print("裴波那切数列：")
#     print(n1,",",n2,end=" , ")
#     while num > counter:
#         nth = n1 + n2
#         print(nth,end=" , ")
#         n1 = n2
#         n2 = nth
#         counter += 1


# num = int(input("请输入数列元素的最大范围："))
# n1, n2 = 0, 1
# list1 = [n1, n2
# while True:
#     nth = n1 + n2
#     if nth > num:
#         break
#     n1, n2 = n2, nth
#     list1.append(nth)
# print(list1)

# def function1(max_num):
#     n1, n2 = 0, 1
#     list1 = [n1, n2]
#     while True:
#         nth = n1 + n2
#         if nth > max_num:
#             break
#         n1, n2 = n2, nth
#         list1.append(nth)
#     print(list1)

# function1(100)


# x = int(input('enter a number: ')) 
# def test1(): 
# 	n1,n2=0,1 
# 	list = [n1,n2] 
# 	nth=0 
# 	for i in range(0,x): 
# 		nth = n1 +n2 
# 		if nth <= x: 
# 			n1 = n2 
# 			n2 = nth 
# 			list.append(nth) 
# 		#print(nth) 
# 	print (list) 
	
# test1()


"""
next 利用迭代器解决阿姆斯特朗数
"""
# import sys

# num = int(input("Please input a number which is larger than 0："))

# if num < 0:
#     print("number can't smaller than 0")

# n = len(str(num))
# list = list(str(num))
# it = iter(list)
# sum = 0
# while True:
#     try:
#         sum += int(next(it))**n
#     except StopIteration as identifier:
#         if num == sum:
#             print("num %d is 阿姆斯特朗数" % num)
#         else:
#             print("num %d is not 阿姆斯特朗数" % num)
#         sys.exit()








