"""
python 数据写入 csv 文件
"""


import csv

with open('data.csv',mode='w') as f:
    w = csv.writer(f)
    w.writerow(['1', '2'])

f.close()