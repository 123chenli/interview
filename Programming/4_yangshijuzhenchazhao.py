"""
在一个m行n列的二维数组中，每一行都按照从左到右
递增的顺序排序，每一列都按照从上到下递增的顺序
排序。请完成一个函数，输入这样一个二维数组和一个
整数，判断数组中是否含有该整数。
考点：使用Step-wise线性搜索
"""


def get_value(l, r, c):
    return l[r][c]


def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n
    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c -= 1
        elif value < x:
            r = r+1
        return False