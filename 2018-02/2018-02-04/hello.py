def hello(fn):
    def wrapper():
        print('hello')
        fn()
        print('goodbye')
    return wrapper

@hello    # 装饰器
def hi():
    print('abc')
hi()


# def hi():
#     print('abc')
# hi = hello(hi)

# hi()