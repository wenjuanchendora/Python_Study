# 阿姆斯特朗数

# num = int(input("请输入数值："))
# n = len(str(num))
# counter = 0
# sum = 0
# for i in range(n):
#     sum += int(str(num)[i]) ** n
#     counter += 1

# if sum == num:
#     print(num," 是阿姆斯特朗数")
# else:
#     print(num," 不是阿姆斯特朗数")


# max_num = int(input("请输入最大数值："))
# list1 = []
# for num in range(max_num+1):
#     sum = 0
#     counter = 0
#     n = len(str(num))
#     for i in range(n):
#         sum += int(str(num)[i]) ** n
#         counter += 1
#     if sum == num:
#         list1.append(sum)
# print(list1)
    


# 裴波那切数列

# n1 = 0
# n2 = 1
# list1 = [n1,n2]
# max_num = int(input("请输入数列内元素个数："))
# counter = 0
# while True:
#     n3 = n1 + n2
#     list1.append(n3)
#     if len(list1) == max_num:
#         break
#     counter += 1
#     n1, n2 = n2, n3
# print(list1)