"""
A linked list is given such that each node contains an
additional random pointer which could point to any node
in the list or null.
Return a deep copy of the list.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        top = head
        # create copy of node, insert between node and next
        while top:
            copy = Node(top.val, top.next, None)
            top.next = copy
            top = copy.next
        top = head
        # assign orig random ref to orig next (copied node)
        while top:
            copy = top.next
            if top.random:
                copy.random = top.random.next
            top = copy.next
        top, copy, tmp = head, None, None
        # separate orig and copy lists
        while top:
            if not copy:
                copy = tmp = top.next
            if tmp:
                top.next = tmp.next
                tmp.next = tmp.next.next if tmp.next else None
                tmp = tmp.next
            top = top.next
        return copy

if __name__ == "__main__":
    s = Solution()
    l_0 = Node(1, None, None)
    l_1 = Node(2, None, None)
    l_0.next = l_1
    l_0.random = l_1
    l_1.random = l_1
    ex_0 = s.copyRandomList(l_0)
    ex_1 = s.copyRandomList(None)
    ex_2 = s.copyRandomList(l_1)
    pass