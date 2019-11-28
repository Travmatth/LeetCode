"""
Given a linked list, remove the n-th node from the end of list and return its head.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not n:
            return head
        runner = head
        top = head
        for i in range(n):
            if not runner.next:
                if i == n - 1:
                    head = head.next
                return head
            runner = runner.next
        while runner.next:
            runner = runner.next
            top = top.next
        top.next = top.next.next
        return head

def make_ll(list):
    nodes = [ListNode(x) for x in list]
    for i in range(len(list) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def make_list(ll):
    list = []
    while ll:
        list.append(ll.val)
        ll = ll.next
    return list

if __name__ == "__main__":
    s = Solution()
    ll_0 = make_ll([1, 2, 3, 4, 5])
    ex_0 = s.removeNthFromEnd(ll_0, 2)
    if make_list(ex_0) != [1, 2, 3, 5]:
        print("Error")
    ll_1 = make_ll([1])
    ex_1 = s.removeNthFromEnd(ll_1, 1)
    if make_list(ex_1) != []:
        print("Error")
    ll_2 = make_ll([1, 2])
    ex_2 = s.removeNthFromEnd(ll_2, 2)
    if make_list(ex_2) != [2]:
        print("Error")
    ll_3 = make_ll([1, 2])
    ex_3 = s.removeNthFromEnd(ll_3, 1)
    if make_list(ex_3) != [1]:
        print("Error")
    pass