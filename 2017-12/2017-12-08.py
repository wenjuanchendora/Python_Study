# python 处理 csv 文件

import os

# print(os.getcwd())   # 获得当前文件路径

filepath = os.path.join(os.getcwd(), 'data', 'userinfo.csv')

# open csv file
f = open(filepath)
reader = csv.reader(f)










