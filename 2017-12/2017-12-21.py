"""
利用生成器写入 csv 文件
"""

import csv

# def fibon(n):
#     a = b =1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# def write_csv(list):
#     with open('data.csv',mode='a',newline="") as f:
#         w = csv.writer(f)
#         w.writerow(list)

#     f.close()
        
# for x in fibon(10):
#     write_csv([str(x)])



def fibon(n):
    a = b =1
    for i in range(n):
        yield a
        a, b = b, a + b
        
# 此方法比定义函数要快速
with open('data.csv',mode='a',newline="") as f:
    w = csv.writer(f)
    for x in fibon(10):
        w.writerow([str(x)])

    f.close()
        
