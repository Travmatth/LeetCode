"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def split_list(self, head):
        n = 0
        left, right = head, head
        while right:
            right = right.next
            n += 1
        prev, right = None, head
        n //= 2
        while n:
            prev = right
            right = right.next
            n -= 1
        prev.next = None
        return left, right

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left, right = self.split_list(head)
        left, right = self.sortList(left), self.sortList(right)
        out, tail = None, None
        if left and right and left.val < right.val:
            out = tail = left
            left = left.next
        elif left and right:
            out = tail = right
            right = right.next
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
            tail.next = None
        tail.next = right if right else left
        return out

def make_ll(list):
    nodes = [ListNode(x) for x in list]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def get_list(ll):
    out = []
    while ll:
        out.append(ll.val)
        ll = ll.next
    return out

if __name__ == "__main__":
    s = Solution()
    l_0 = make_ll([4,2,1,3])
    ex_0 = s.sortList(l_0) 
    if get_list(ex_0) != [1,2,3,4]:
        print("Error")
    l_1 = make_ll([-1,5,3,4,0])
    ex_1 = s.sortList(l_1) 
    if get_list(ex_1) != [-1,0,3,4,5]:
        print("Error")
    pass