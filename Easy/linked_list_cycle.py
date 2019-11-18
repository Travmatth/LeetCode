"""
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an
integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there
is no cycle in the linked list.
Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def make_ll(list, cycle):
    nodes = [ListNode(val) for val in list]
    for i in range(1, len(list)):
        nodes[i - 1].next = nodes[i]
    if cycle != -1:
        nodes[-1].next = nodes[cycle]
    return nodes[0]

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        runner_1 = head
        runner_2 = head
        while True:
            if not head or not runner_1 or not runner_2:
                return False
            if not head.next or not runner_1.next or not runner_2.next:
                return False
            runner_1 = runner_2.next
            runner_2 = runner_1.next
            if head == runner_1 or head == runner_2:
                return True
            head = head.next

if __name__ == "__main__":
    s = Solution()
    ll_1 = make_ll([3,2,0,-4], 1)
    ex_1 = s.hasCycle(ll_1)
    if ex_1 != True:
        print("ERROR")
    ll_2 = make_ll([1,2], 0)
    ex_2 = s.hasCycle(ll_2)
    if ex_2 != True:
        print("ERROR")
    ll_3 = make_ll([1], -1) 
    ex_3 = s.hasCycle(ll_3)
    if ex_3 != False:
        print("ERROR")
    pass