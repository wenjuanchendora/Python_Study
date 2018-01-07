# 99 乘法表

# for x in range(1,10):
#     for y in range(1,x+1):
#         print("{} * {} = {}\t".format(y,x,x*y),end="")
#     print()



# 求从10到100之间能被3或5整除的数之和
# sum = 0
# for x in range(10,101):
#     if x % 3 ==0 or x % 5 ==0:
#         sum = sum + x
print(sum)

# 求从1到100之间的奇数之和
# sum = 0
# for x in range(1,101):
#     if x % 2 != 0:
#         sum += x
# print(sum)

# 随机生成一个手机号码 (13x xxxx xxxx, 15x xxxx xxxx, 17x xxxx xxxx, 18x xxxx xxxx)
import random

list1 = ['13', '15', '17', '18']
a = random.choice(list1)+"".join(random.choice("0123456789") for x in range(9))
print(a)
    