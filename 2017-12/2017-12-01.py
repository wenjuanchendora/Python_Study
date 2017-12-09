"""
通用序列操作
"""


# 1.1 索引
a = "helloworld"
print(a[0])
print(a[1])
print(a[5])
print(a[-1])
print(a[-2])
print("------------------------------------")


#1.2 切片
b = "0123456789"
print(a[1:5])
print(a[3:-2])
print(a[5::-2])
print(a[4::-2])
print(a[4::2])
print("------------------------------------")


# 1.3 序列相加
x = [1,3,4]
y = [2,4,6]
a = "hello"
b = "world"
print(a+b)
print(x+y)
print("------------------------------------")


# 1.4 乘法
a = [1,3,5]
b = [2,4,6]
c = 5
x = "hello"
print(a*c)
print(c*x)
print("------------------------------------")


# 1.5 成员资格
a = [1,2,3,4,5,6,7,8,9]
b = "greeting"
print(1 in a)
print(10 in a)
print("get" in b)
print("et" in b)