# 元组 (不支持更改元素)

tup1 = ('one', 'two', 100, 10000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
# print(tup3)
# tup = ()
# print(tup)
tup = (10,)
# print(tup)
# print("tup1[0]: ", tup1[0])
# print("tup2[1:5]: ", tup2[1:5])
# tup4 = tup1 + tup2
# print(tup4)
# del tup       # 删除元组
# print(tup)

# print(len(tup1))
# print(tup1 + tup2, tup3 * 3)
# print(1 in tup2)
# for a in tup3:
#     print("a")

list1 = ["one", "two", 100, 200]
tup = tuple(list1)
print(tup)

tup4 = tuple("hello world")
print(tup4)


"""
元组和列表之间相同与不同之处
相同点：可通过切片获取元素
不同点：元组 -- () ;  不可修改
       列表 -- [] ;  可以修改
"""
