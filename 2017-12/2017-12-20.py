"""
生成器
"""

# def generator_func():
#     for i in range(10):
#         yield i

# for x in generator_func():
#     print(x)

def fibon(n):
    a = b =1
    for i in range(n):
        yield a
        a, b = b, a + b
        
for x in fibon(100):
    print(x)