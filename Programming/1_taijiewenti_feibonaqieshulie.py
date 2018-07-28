"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。
求该青蛙跳上一个n级台阶总共有多少中跳法
"""


# 1、第一种记忆方法
fib = lambda n: n if n <= 2 else fib(n-1) + fib(n-2)


# 2、第二种记忆方法
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib1(i):
    if i < 2:
        return 1
    num = fib(i-1) + fib(i-2)
    print(num)
    return num


# 3、第三种方法
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    print(a, b)
    return b


if __name__ == '__main__':
    fib1(20)
    fib2(20)