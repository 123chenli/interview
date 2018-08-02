"""
1->2->3->4
2->1->4->3
"""


class ListNode:
    '''
    定义链表
    '''
    def __init__(self):
        self.val = None
        self.next = None


class Solution:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        print(head)
        return head


if __name__ == '__main__':
    l = Solution()
    l_list = [1, 2, 3, 4]
    for i in l_list:
        l.add(i)