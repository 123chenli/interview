# 1直接创建
dict1 = {'name': 'earth', 'port': '80'}

# 2 工厂方法
items = [('name', 'earth'), ('port', '80')]
dict2 = dict(items)
print(dict2)

# 3 fromkeys()方法
dict3 = {}.fromkeys(('x', 'y', 'z'), -1)
print(dict3)