"""
Python 练习_01
date: 2017-11-28
"""
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is", c)

c = a - b
print ("Line 2 - Value of c is", c)

c = a * b
print ("Line 3 - Value of c is", c)

c = a / b
print ("Line 4 - Value of c is", c)

c = a % b
print ("Line 5 - Value of c is", c)

a = 2
b = 3
c = a**b
print ("Line 6 - Value of c is", c)


a = 10
b = 5
c = a//b
print ("Line 7 - Value of c is", c)


a = 21
b = 10
c = 0

if (a == b):
    print ("Line 1 - a is equal to b")
else:
    print ("Line 1 - a is not equal to b")

if (a != b):
    print ("Line 2 - a is not equal to b")
else:
    print ("Line 2 - a is equal to b")
    
# if (a <> b):
#     print ("Line 3 - a is not equal to b")
# else:
#     print ("Line 3 - a is equal to b")
    
if (a < b):
    print ("Line 4 - a is less than b")
else:
    print ("Line 4 - a is not less than b")
    
if (a > b):
    print ("Line 5 - a is greater than b")
else:
    print ("Line 5 - a is not greater than b")


a = 5
b = 20  

if (a <= b):
    print ("Line 6 - a is either less than or equal to b")
else:
    print ("Line 6 - a is neither less than nor equal to b")
    
if (a >= b):
    print ("Line 7 - b is either greater than or equal to b")
else:
    print ("Line 7 - b is neither greater than nor equal to b")



a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is", c)

c += a
print ("Line 2 - Value of c is", c)

c *= a
print ("Line 3 - Value of c is", c)

c /= a
print ("Line 4 - Value of c is", c)

c = 2
c %= a
print ("Line 5 - Value of c is", c)

c **= a
print ("Line 6 - Value of c is", c)

c //= a
print ("Line 7 - Value of c is", c)



a = 60              # 60 = 0011 1100
b = 13              # 13 = 0000 1101
c = 0

c = a & b;
print ("Line 1 - Value of c is", c)

c = a | b;
print ("Line 2 - Value of c is", c)

c = a ^ b;
print ("Line 3 - Value of c is", c)

c = ~a;
print ("Line 4 - Value of c is", c)

c = a << 2;
print ("Line 5 - Value of c is", c)

c = a >> 2
print ("Line 6 - Value of c is", c)



a = 10
b = 20
c = 0

if (a and b):
    print ("Line 1 - a and b are true")
else:
    print ("Line 1 - either a is not true or b is not true")

if (a or b):
    print ("Line 2 - either a is true or b is true or both are true")
else:
    print ("Line 2 - neither a is true nor b is true")

a = 0   
if (a and b):
    print ("Line 3 - a and b are true")
else:
    print ("Line 3 - either a is not true or b is not true")
    
if (a or b):
    print ("Line 4 - either a is true or b is true or both are true")
else:
    print ("Line 4 - neither a is true nor b is true")
    
if not(a and b):
    print ("Line 5 - a and b are true")
else:
    print ("Line 5 - either a is not true or b is not true")