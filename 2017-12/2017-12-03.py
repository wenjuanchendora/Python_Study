
score=int(input("请输入分数: "))

if 90<score<=100:
	print("优秀")
elif 60<=score<=90:
	print("及格")
elif 0<=score<60:
	print("不及格")
else:
	print("不合法分数输入")
	
	
	
string1="qwertyuiopasdfghjklzxcvbnm"
print(string1[:3])
print(string1[1:-1])
print(string1[::2])



a=10; b=20
a,b=b,a
print(a,b)

a=10; b=20
c=a+b
a=c-a
b=c-b
print(a,b)
