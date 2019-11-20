"""
Write a program to find the node at which the intersection
of two singly linked lists begins.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a, len_b = 0, 0
        first, second = headA, headB
        while first:
            len_a += 1
            first = first.next
        while second:
            len_b += 1
            second = second.next
        if len_a > len_b:
            diff = len_a - len_b
            longer = headA
            shorter = headB
        else:
            diff = len_b - len_a
            longer = headB
            shorter = headA
        while diff:
            longer = longer.next
            diff -= 1
        while longer or shorter:
            if not longer or not shorter:
                return None
            elif shorter == longer:
                return shorter
            shorter = shorter.next
            longer = longer.next

def make_intersecting_ll(l_1, l_2, skipA, skipB):
    first = [ListNode(val) for val in l_1[:skipA]]
    second = [ListNode(val) for val in l_2[:skipB]]
    tail = [ListNode(val) for val in l_1[skipA:]]
    for i in range(1, len(first)):
        first[i - 1].next = first[i] 
    for i in range(1, len(second)):
        second[i - 1].next = second[i] 
    for i in range(1, len(tail)):
        tail[i - 1].next = tail[i] 
    if tail:
        first[-1].next = tail[0]
        second[-1].next = tail[0]
    return first[0], second[0]

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.getIntersectionNode(*make_intersecting_ll([4,1,8,4,5], [5,0,1,8,4,5], 2, 3))
    if ex_0.val != 8:
        print("Error")
    ex_1 = s.getIntersectionNode(*make_intersecting_ll([0,9,1,2,4], [3,2,4], 3, 1))
    if ex_1.val != 2:
        print("Error")
    ex_3 = s.getIntersectionNode(*make_intersecting_ll([2,6,4], [1,5], 3, 2))
    if ex_3:
        print("Error")
    pass
