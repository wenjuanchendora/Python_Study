"""
将生成的裴波那切数列写入到 csv 文件中
"""

import csv

x = int(input('enter a number: ')) 
def fio(num): 
	n1,n2=0,1 
	list = [n1,n2] 
	nth=0 
	for i in range(0,x): 
		nth = n1 +n2 
		if nth <= x: 
			n1 = n2 
			n2 = nth 
			list.append(nth) 
		#print(nth) 
	return (list) 

def write_csv(list):
    with open('data.csv',mode='w') as f:
        w = csv.writer(f)
        w.writerow(list)

    f.close()

list = fio(x)
write_csv(list)