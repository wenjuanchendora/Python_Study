# 字典

stu=["xiaoming", "xiaohong", "xiaoli"]
nums=[1001, 1002, 1003]
print("xiaoming num: ", nums[stu.index("xiaoming")])

nums = {'xiaoming': '1001', 'xiaohong': '1002', 'xiaoli': '1003'}
print(nums['xiaohong'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First', 'Age': 9}
# print("dict['Alice']: ", dict['Alice'])
# dict['Age'] = 8; # update existing entry
# print("dict['Age']: ", dict['Age'])

# dict.clear()  # 删除字典元素
# del dict      # 删除整个字典
# print(dict)
# print(len(dict))
# print(str(dict))
# print(type(dict))
# print(dict.copy())
# print(dict.fromkeys('Name'))
# print(dict.get('Age'))
# print(dict.get('Ae'))
# print('Name' in dict)
# print(dict.items())
# print(dict.keys())
# print(dict.values())
# dict.setdefault('Name')
# dict.setdefault('Address', 'China')
# print(dict)
# dict.update(nums)
# print(dict)
# dict.pop('Name')
# print(dict)
print(dict.popitem())
print(dict)


