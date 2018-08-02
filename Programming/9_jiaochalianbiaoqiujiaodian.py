"""
交叉链表求交点：
可以从尾部开始比较两个链表，如果相交，
尾部开始必然一致，只要从尾部开始比较，
直至不一致的地方即为交叉点
"""

# 使用a、b两个list来模拟链表，可以看出交叉点是7
a = [1, 2, 3, 7, 9, 1, 5]
b = [4, 5, 7, 9, 1, 5]
for i in range(1, min(len(a), len(b))):
    if i == 1 and (a[-1] != b[-1]):
        print('no')
        break
    else:
        if a[-i] != b[-i]:
            print('交叉点：', a[-i+1])
            break
        else:
            pass


# 另一种比较正规的方法，构造链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def node(l1, l2):
    len1, len2 = 0, 0
    # 求两个链表的长度
    while l1.next:
        l1 = l1.next  # 尾节点
        len1 += 1
    while l2.next:
        l2 = l2.next  # 尾节点
        len2 += 1

    # 若相交
    if l1.next ==  l2.next:
        # 长链表先走
        if len1 > len2:
            for _ in range(len1-len2):
                l1 = l1.next
            return l1  # 返回交点
        else:
            for _ in range(len2-len1):
                l2 = l2.next
            return l2  # 返回交点
    # 如果不相交
    else:
        return
