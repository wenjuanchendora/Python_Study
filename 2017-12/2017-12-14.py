# 迭代器
import sys

list = [1,2,3,4,5]
# for x in list:
#     print(x)

it = iter(list)
# print(it)
# print(next(it))

# for x in it:
#     print("it == ", x)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()