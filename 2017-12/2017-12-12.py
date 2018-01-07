# 阿姆斯特朗数

# number = int(input("Please enter number: "))
# length = len(str(number))
# sum = 0
# for x in range(length):
#     sum += int(str(number)[x])**length
# if sum == number:
#     print("%d is an AMSTL number" % number)
# else:
#     print("%d is not an AMSTL number" % number)

# minnum = int(input("Please enter min number: "))
# maxnum = int(input("Please enter max number: "))
# print("AMSTL numbers between %d ~ %d: " % (minnum, maxnum))
# for number in range(minnum, maxnum + 1):
#     sum = 0 
#     length = len(str(number))
#     for x in range(length):
#         sum += int(str(number)[x])**length
#     if sum == number:
#         print(number, end=" ")


# number = int(input("Please enter number: "))
# length = len(str(number))
# sum = 0
# var = number
# while var > 0:
#     digit = var % 10
#     sum += digit ** length
#     var //= 10
# if sum == number:
#     print("%d is an AMSTL number" % number)
# else:
#     print("%d is not an AMSTL number" % number)


# minnum = int(input("Please enter min number: "))
# maxnum = int(input("Please enter max number: "))
# print("AMSTL numbers between %d ~ %d: " % (minnum, maxnum))
# for number in range(minnum, maxnum + 1):
#     sum = 0
#     length = len(str(number))
#     var = number
#     while var > 0:
#         digit = var % 10
#         sum += digit ** length
#         var //= 10

#     if sum == number:
#         print(number, end=" ")