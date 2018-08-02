"""
去除列表中的重复元素
"""


# 1 用集合
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list(set(l1))
print(l2)


# 2 用字典
l3 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l4 = {}.fromkeys(l3).keys()
print(l4)


# 3 用字典并保持顺序
l5 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l6 = list(set(l5))
l6.sort(key=l5.index)
print(l6)


# 4 列表推导式
l7 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l8 = []
[l8.append(i) for i in l7 if i not in l8]
print(l8)